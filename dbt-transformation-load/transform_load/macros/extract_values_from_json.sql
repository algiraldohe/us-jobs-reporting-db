{% macro get_json_field(column_name) %}

{% set json_query %}
select {{ column_name }} from {{ ref("src_job_listings") }}
{% endset %}

{% set results = run_query(json_query) %}

{% if execute %}
{# Return the first column #}
{% set results_list = results.columns[0].values() %}
{% else %}
{% set results_list = [] %}
{% endif %}

{{ log(results_list[:2], info=True) }}

{% for dict_item in results_list[:5] %}
    {# Cut list brackets to parse dict #}
    {% set remuneration_dict = fromjson(dict_item[1:-1]) %}
    {% set min = remuneration_dict['MinimumRange']%}
    {% set max = remuneration_dict['MaximumRange']%}
    {% set period = remuneration_dict['Description']%}
    {{ log([min,max, period], info=True) }}
{% endfor %}


{{ return([]) }}


{% endmacro %}
