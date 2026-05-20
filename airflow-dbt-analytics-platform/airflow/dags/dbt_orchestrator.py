import sys
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    "description": "A DAG to orchestrate data",
    # DAG start date
    "start_date": datetime(2026, 5, 18),
    # Prevent backfilling old runs
    "catchup": False,
    "owner": "steven",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="weather_dbt_orchestrator",
    default_args=default_args,

    # Schedule
    # schedule="@daily",
    schedule=timedelta(minutes=5),

    # Tags shown in Airflow UI
    tags=["etl", "transformation"]
) as dag:

  transform_task = BashOperator(
      task_id="transform_data",
      # 直接切換到 Airflow 容器內的 dbt 專案路徑，並執行 dbt run
      # 明確告訴它 profiles.yml 檔案在 /opt/airflow/dbt 底下
      bash_command="cd /opt/airflow/dbt/de_project && dbt run --profiles-dir /opt/airflow/dbt",
  )