CREATE USER superset WITH PASSWORD 'superset';
CREATE DATABASE superset_db OWNER superset;

CREATE USER examples WITH PASSWORD 'examples';
CREATE DATABASE examples_db OWNER examples;

-- 直接提權，降維打擊 Postgres 16 的限制
ALTER USER db_user WITH SUPERUSER;
ALTER USER superset WITH SUPERUSER;
ALTER USER examples WITH SUPERUSER;

\c analytics_db;
GRANT ALL ON SCHEMA public TO db_user;

\c superset_db;
GRANT ALL ON SCHEMA public TO superset;

\c examples_db;
GRANT ALL ON SCHEMA public TO examples;