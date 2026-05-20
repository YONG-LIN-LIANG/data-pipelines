{{
  config(
    materialized='table'
  )
}}

SELECT
  city,
  date(weather_time_local) as date,
  round(temperature)::numeric as avg_temperature,
  round(wind_speed)::numeric as avg_wind_speed
FROM {{ref('stg_weather_data')}}