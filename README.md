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