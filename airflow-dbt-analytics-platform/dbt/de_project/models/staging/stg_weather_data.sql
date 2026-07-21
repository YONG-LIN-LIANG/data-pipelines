{{ config(
  materialized='table',
  unique_key=['country', 'city']
) }}

WITH source AS (
  SELECT * 
  FROM {{source('weatherstack', 'local_weather')}}
)

SELECT
  country,
  city,
  temperature,
  wind_speed,
  local_time::timestamp as weather_time_local
FROM source
