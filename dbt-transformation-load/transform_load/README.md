Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


### Notes:

Friday 22-09-2023

- host: had to put localhost as host for dbt to recognise the running instance on docker. Need to check how it would work running from docker.

- sources.yml file: name by default follow the schema only change it if schema and db differ but for postgres db does not need to be stipulated.

- macros: extract_values_from_json.sql
`dbt run-operation get_json_field --args '{column_name: position_remuneration}'`

Saturday 23-09-2023

- Always try to go native, there are ready solutions that doesn't required further development within the tech stack that you're using.
