import sys
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
# 因為 Airflow 執行 DAG 時，預設通常只有 /opt/airflow/dags 所以 from insert_records import main
# Python 只會找 /opt/airflow/dags/insert_records.py 但檔案其實在 /opt/airflow/api-request/insert_records.py
# 所以必須把這個路徑加進 Python module search path /opt/airflow/api-request/insert_records.py
# 是在告訴 Python：「也去 /opt/airflow/api-request 找 modules」
sys.path.append('/opt/airflow/api-request')
from insert_records import main
# =========================================================
# Default DAG arguments
# =========================================================

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


# =========================================================
# Python task functions
# =========================================================

def extract():
    print("Running extract step...")


def transform():
    print("Running transform step...")


def load():
    print("Running load step...")


# =========================================================
# DAG definition
# =========================================================

with DAG(
    dag_id="weather_api_orchestrator",
    default_args=default_args,

    # Schedule
    # schedule="@daily",
    schedule=timedelta(minutes=5),

    # Tags shown in Airflow UI
    tags=["etl", "postgres"]
) as dag:

    # =====================================================
    # Task 1
    # =====================================================

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=main
    )


    # =====================================================
    # Task 2
    # =====================================================
    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform,
    )

    # =====================================================
    # Task 3
    # =====================================================
    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load,
    )

    # =====================================================
    # Task dependencies
    # =====================================================

    extract_task >> transform_task >> load_task