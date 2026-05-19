CREATE SCHEMA IF NOT EXISTS weatherstack;
CREATE TABLE weatherstack.local_weather(
  weather_status_id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY,
  country TEXT,
  city TEXT,
  local_time TEXT,
  temperature INT,
  weather_descriptions TEXT,
  wind_speed INT,
  wind_degree INT,
  humidity INT,
  uv_index INT,
  visibility INT,
  latitude FLOAT,
  longitude FLOAT,
  created_ts timestamptz DEFAULT CURRENT_TIMESTAMP,
  modified_ts timestamptz DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT local_weather_PKEY PRIMARY KEY (weather_status_id),
  CONSTRAINT local_weather_unique_key UNIQUE (country, city)
);