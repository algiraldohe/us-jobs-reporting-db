with
  json_extracted_data (id, json) as (values
{%- for dict_item in get_json_field("position_remuneration") -%}
    ({{loop.index}}, '{{dict_item[1:-1]}}' :: jsonb){{ ", " if not loop.last else "" }}
{%- endfor -%}
)

select
id
, "MinimumRange" as minimum_range
, "MaximumRange" as maximum_range
, "Description" as time_period

from
json_extracted_data,
lateral jsonb_to_record(json_extracted_data.json) as (
    "MinimumRange" numeric(8,2)
    , "MaximumRange" numeric(8,2)
    , "Description" text
    )
