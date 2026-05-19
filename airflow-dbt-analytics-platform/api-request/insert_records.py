from api_request import mock_fetch_data
import psycopg2
import json

def connect_to_db():
  print("Connecting to the Postgres database")

  try:
    # Localhost testing
    # conn = psycopg2.connect(
    #   host="localhost",
    #   port=5433,
    #   dbname="analytics_db",
    #   user="db_user",
    #   password="password123"
    # )

    # Environment in container
    conn = psycopg2.connect(
      host="postgres",
      port=5432,
      dbname="analytics_db",
      user="db_user",
      password="password123"
    )
    # print(conn)
    return conn
  except psycopg2.Error as e:
    print(f"Database connection failed: {e}")
# print(mock_fetch_data())
    
def create_table(conn):
  print(f"Creating table if not exist...")
  
  try:
    cursor = conn.cursor()
    cursor.execute("""
      CREATE SCHEMA IF NOT EXISTS weatherstack;
      CREATE TABLE weatherstack.local_weather(
        weather_status_id SERIAL PRIMARY KEY,
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
        modified_ts timestamptz DEFAULT CURRENT_TIMESTAMP
      );
    """)
    conn.commit()
    print("Table was created.")
  except psycopg2.Error as e:
    print(f"Failed to create table: {e}")

def insert_records(conn, in_data_json):
  print(f"Creating table if not exist...")
  
  try:
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT weatherstack.ingest_local_weather(%s::jsonb);
        """,
        (json.dumps(in_data_json),)
    )
    conn.commit()
    print("Record was inserted.")
  except psycopg2.Error as e:
    print(f"Failed to insert record: {e}")

def main():
  try:
    data = mock_fetch_data()
    conn = connect_to_db()
    insert_records(conn, data)
  except Exception as e:
    print(f"An error occurred during execution: {e}")
  
  finally:
    if 'conn' in locals():
      conn.close()
      print("Database connection closed.")


main()