WITH raw_jobs AS (
    select * from {{ source('public', 'jobs') }}
)

SELECT
    "id",
    "PositionTitle" AS position_title,
    "PositionURI" AS position_uri,
    "PositionRemuneration" AS position_remuneration,
    "PositionLocation" AS position_location,
    "RemoteIndicator" AS is_remote,
    "StorageFile" AS storage_file,
    "DateAdded" AS added_at,
    "UserAdded" AS added_by

from raw_jobs
