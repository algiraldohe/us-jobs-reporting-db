-- Create DEV Database to store the data
-- Check if database exists
SELECT 1 as output_ FROM pg_database WHERE datname = 'dev_us_jobs'

-- -- Create db
CREATE DATABASE dev_us_jobs;

-- -- Create schemas
CREATE SCHEMA raw;
CREATE SCHEMA dev;
