{% extends "format/record/Default_HTML_detailed_base.tpl" %}

{% block header %}
<!--     {{ bfe_topbanner(bfo, prefix='<div style="padding-left:10px;padding-right:10px">', suffix='</div><hr/>') }}

    <div class="well">
        {{ bfe_title(bfo, separator="<br />") }}
    </div> -->
{% endblock %}

{% block details %}
<div class="row">
    <div class="col-md-9">
    <div class="panel panel-primary">
        <div class="panel-heading lead">{{ bfe_title(bfo, separator="<br />") }}</div>
        <div class="panel-body">
            <div class="table-responsive">
            <table class="table table-striped" style="text-align: left;">
                <tr>
                    <th style="vertical-align: middle; width: 15%;"><i class="fa fa-user fa-fw"></i> Authors</th>
                    <td>
                        <p id="authors_short" class="authors_list collapse in" style='margin-bottom: 0;'>
                            {{ bfe_authors(bfo, relator_code_pattern="$", limit="25", interactive="yes", print_affiliations="no") }}
                        </p>
                        <p id="authors_long" class="authors_list collapse" style='margin-bottom: 0;'>
                            {{ bfe_authors(bfo, relator_code_pattern="$", limit="25", interactive="yes", print_affiliations="yes",
                               separator="<br>", affiliation_prefix="<br><small>", affiliation_suffix="</small>") }}
                        </p>
                        <small>
                            <a href="#" class="text-muted" data-toggle="collapse" data-target=".authors_list">(show affiliations)</a>
                        </small>
                    </td>
                </tr>
                <tr>
                    <th><i class="fa fa-pencil fa-fw"></i> Abstract</th>
                    <td>{{ bfe_abstract(bfo) }}</td>
                </tr>
                <tr>
                    <th><i class="fa fa-tags fa-fw"></i> Descriptors</th>
                    <td>{{ bfe_descriptors(bfo) }}</td>
                </tr>
                <tr>
                    <th><i class="fa fa-calendar fa-fw"></i> Published</th>
                    <td>{{ bfe_publisher(bfo) }}{{ bfe_publication_date(bfo, prefix="</br>") }}</td>
                </tr>
                <tr>
                    <th><i class="fa fa-edit fa-fw"></i> Notes</th>
                    <td>{{ bfe_notes(bfo, note_prefix="") }}</td>
                </tr>
            </table>
            </div>
        </div>
    </div>
    </div>
    <div class="col-md-3">
        {{ format_record(recid, of='HDINFO', ln=g.ln)|safe }}
        <div class="panel panel-default">
            <div class="panel-heading">Actions</div>
            <div class="panel-body">
                <div style="text-align: left;">
                    {{ format_record(recid, of='HDACT', ln=g.ln)|safe }}
                </div>
            </div>
        </div>
    </div>
</div>
<!--     <div class="pull-right">
        {{ bfe_record_type(bfo, suffix="<br />") }}
    </div> -->
    


<!--     {{ bfe_addresses(bfo) }}
    {{ bfe_affiliation(bfo) }}
    {{ bfe_date(bfo, prefix="<br />", suffix="<br />") }}
    {{ bfe_publisher(bfo, prefix="<small>", suffix="</small>") }}
    {{ bfe_place(bfo, prefix="<small>", suffix="</small>") }}
    {{ bfe_isbn(bfo, prefix="<br />ISBN: ") }} -->

{% endblock %}

{% block footer %}
{% endblock %}
