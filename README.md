<!-- Login DB -->

docker exec -it pipeline-postgres-db psql -U db_user -d analytics_db

<!-- 建立一個 Python 虛擬環境。 -->

python -m venv .venv

<!-- 啟動虛擬環境。 -->

source .venv/bin/activate

<!-- Install packages in virtual env -->

python -m pip install requests



<!-- Problem faced and solved -->
*Problem* - Couldn't connect to Postgres hosted in Docker Container
*Solution* - The port 5432 was occupied by local Postgres, so the Postgres in Docker should be ported to the port except 5432 (I set it 5433)


<!-- Airflow in container will communicate with Postgres in the container, so in the db connection setting it should be the db config in container -->


<!-- To modify the duration that system log user out simply set up healthcheck interval in docker-compose.yml  -->


<!-- Create Admin User for Airflow -->
docker compose exec airflow airflow users create --username steven --firstname YongLin --lastname Liang --email steven841221@gmail.com --role Admin --password steven

<!-- Create Admin user for Superset By defaule username: admin; password: admin -->
docker compose exec superset superset fab create-admin --username steven --firstname YongLin --lastname Liang --email steven841221@gmail.com --password steven