#!/bin/bash
set -e

pip install dbt-postgres==1.9.0

airflow db migrate

airflow users create \
    --username steven \
    --firstname YongLin \
    --lastname Liang \
    --email stevenxxxxx@gmail.com \
    --role Admin \
    --password steven

exec airflow standalone