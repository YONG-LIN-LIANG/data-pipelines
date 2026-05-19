CREATE OR REPLACE FUNCTION weatherstack.ingest_local_weather(
    in_data_json JSONB
)
RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO weatherstack.local_weather (
      country,
      city,
      local_time,
      temperature,
      weather_descriptions,
      wind_speed,
      wind_degree,
      humidity,
      uv_index,
      visibility,
      latitude,
      longitude
    ) VALUES (
      in_data_json #>> '{location,country}',
      in_data_json #>> '{location,name}',
      (in_data_json #>> '{location,localtime}')::timestamp AT TIME ZONE (in_data_json #>> '{location,timezone_id}'),
      (in_data_json #>> '{current,temperature}')::int,
      (in_data_json #>> '{current,weather_descriptions}')::text,
      (in_data_json #>> '{current,wind_speed}')::int,
      (in_data_json #>> '{current,wind_degree}')::int,
      (in_data_json #>> '{current,humidity}')::int,
      (in_data_json #>> '{current,uv_index}')::int,
      (in_data_json #>> '{current,visibility}')::int,
      (in_data_json #>> '{location,lat}')::float,
      (in_data_json #>> '{location,lon}')::float
    )
    ON CONFLICT (country, city) DO UPDATE SET
      local_time = EXCLUDED.local_time,
      temperature = EXCLUDED.temperature,
      weather_descriptions = EXCLUDED.weather_descriptions,
      wind_speed = EXCLUDED.wind_speed,
      wind_degree = EXCLUDED.wind_degree,
      humidity = EXCLUDED.humidity,
      uv_index = EXCLUDED.uv_index,
      visibility = EXCLUDED.visibility,
      latitude = EXCLUDED.latitude,
      longitude = EXCLUDED.longitude,
      modified_ts = CURRENT_TIMESTAMP
END;
$$;