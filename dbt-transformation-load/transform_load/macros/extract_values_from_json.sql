{% macro get_json_field(column_name, model) %}

{% set json_query %}
select {{ column_name }} from {{ model }}
{% endset %}

{% set results = run_query(json_query) %}

{% if execute %}
{# Return the first column #}
{% set results_list = results.columns[0].values() %}
{% else %}
{% set results_list = [] %}
{% endif %}

{{ return(results_list) }}

{% endmacro %}
