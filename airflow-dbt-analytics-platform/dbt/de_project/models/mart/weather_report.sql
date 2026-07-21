{{ config(
  materialized='table',
  unique_key=['country', 'city']
)}}

SELECT * FROM {{ref('stg_weather_data')}}