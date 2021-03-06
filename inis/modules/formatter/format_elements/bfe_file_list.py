
from invenio.modules.formatter.format_elements.bfe_fulltext import _CFG_BIBFORMAT_HIDDEN_DOCTYPES, get_files


def format_element(bfo, limit=None):
    """
    This is the format for formatting fulltext links in the mini panel.
    @param separator: the separator between urls.
    @param style: CSS class of the link
    @param show_icons: if 'yes', print icons for fulltexts
    @param focus_on_main_file: if 'yes' and a doctype 'Main' is found,
    prominently display this doctype. In that case other doctypes are
    summarized with a link to the Files tab, named"Additional files".
    @param show_subformat_icons: shall we display subformats considered as icons?
    """

    out = ''

    # Retrieve files
    (parsed_urls, old_versions, additionals) = get_files(bfo, distinguish_main_and_additional_files=True,
                                                         include_subformat_icons=True,
                                                         hide_doctypes=_CFG_BIBFORMAT_HIDDEN_DOCTYPES)

    main_urls = parsed_urls['main_urls']
    fulltexts = main_urls['Fulltext']

    if len(fulltexts) == 0:
        return ''

    if limit and len(fulltexts) > limit:
        fulltexts = fulltexts[:limit]

    out += '<ul style="list-style-type:circle; padding-left:15px">'

    for f in fulltexts:
        if len(f[1]) > 37 and f[1].count('-') >= 5:
            out += '<li><a href="%(url)s">%(text)s</a></li>' % {'url': f[0],
                                                                'text': '.'.join([f[1][37:], f[2]])}
        else:
            out += '<li><a href="%(url)s">%(text)s</a></li>' % {'url': f[0],
                                                                'text': '.'.join([f[1], f[2]])}

    out += '</ul>'
    return out


def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
