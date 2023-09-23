{{
  config(
    materialized = 'ephemeral',
    )
}}

with
    position_remuneration_json (id, json) as (values
{%- for dict_item in get_json_field("position_remuneration", ref("src_job_listings") ) -%}
    ({{loop.index}}, '{{dict_item[1:-1]}}' :: jsonb){{ ", " if not loop.last else "" }}
{%- endfor -%}
)


select
prj.id
, "MinimumRange" as minimum_range
, "MaximumRange" as maximum_range
, "Description" as time_period


from
position_remuneration_json ,
lateral jsonb_to_record(prj.json) as (
    "MinimumRange" numeric(8,2)
    , "MaximumRange" numeric(8,2)
    , "Description" text
    )




