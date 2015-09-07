
{% if published_in %}
<div class="well metadata">
{% for item in published_in %}
<small class="text-muted">{{item.text}}</small>
<a href="{{item.link}}"><img src="{{ url_for('static', filename=item.image) }}" class="img-thumbnail" width="100%" /></a>{% endfor %}
</div>
{% endif %}

<div class="well metadata" style='text-align: left;'>
  <dl>
    {{ bfe_record_type(bfo, prefix='<dt>Record type:</dt><dd>', suffix='</dd>') }}
    {{ bfe_date(bfo, date_format='%d %B %Y', prefix='<dt>Publication date:</dt><dd>', suffix='</dd>') }}
    
    {{ bfe_isbn(bfo, prefix='<dt>ISBN:</dt><dd itemprop="isbn">', suffix='</dd>') }}
    {{ bfe_report_numbers(bfo, prefix='<dt>Report number(s):</dt><dd>', suffix='</dd>') }}
    {{ bfe_language(bfo, prefix='<dt>Languages:</dt><dd>', suffix='</dd>') }}
    {{ bfe_descriptors(bfo, prefix='<dt>Descriptors:</dt><dd>', suffix='</dd>', keyword_prefix='<span class="label label-default" itemprop="descriptors">', keyword_suffix='</span>', separator=' ') }}
    {% if record.get('subjects') %}
    <dt>Subject:</dt>
    {% endif %}
    {{ bfe_publi_info(bfo, prefix='<dt>Published in:</dt><dd>', suffix='</dd>') }}
    
    {{ bfe_publisher(bfo, prefix='<dt>Publisher:</dt><dd>', suffix='</dd>') }}
    {{ bfe_place(bfo, prefix='<dd>', suffix='</dd>') }}
    {{ bfe_field(bfo, escape="0", tag="536__a", prefix='<dt>Grants:</dt><dd>', suffix='</dd>', instances_separator='<br />') }}
   
    {{ bfe_pagination(bfo, prefix='<dt>Pages:</dt><dd itemprop="numberOfPages">', suffix='</dd>', default='', escape='') }}
   
    {{ bfe_appears_in_collections(bfo, prefix='<dt>Collections:</dt><dd>', suffix='</dd>', separator='</br>') }}

    {% if bfo.field('8560_y') %}
    <dt>Uploaded by:</dt>
    <dd><a href="{{ url_for('yourmessages.write', sent_to_user_nicks=bfo.field('8560_y')) }}">{{bfo.field('8560_y').decode('utf8')}}</a> (on {{ bfe_creation_date(bfo, date_format="%d %M %Y") }})</dd>
    {% else %}
    <dt>Uploaded on:</dt>
    <dd>{{ bfe_creation_date(bfo, date_format="%d %M %Y") }}</dd>
    {% endif %}
  </dl>
</div>