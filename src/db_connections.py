from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL as sa_URL
from snowflake.sqlalchemy import URL

load_dotenv()  

def get_postgres_engine():
    url = sa_URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("db_user"),
        password=os.getenv("db_password"),
        host=os.getenv("db_host"),
        port=int(os.getenv("db_port")),
        database=os.getenv("db_database"),
        query={"sslmode": "require"}
    )
    return create_engine(url)


def get_snowflake_engine():
    url = URL(
        account=os.getenv('snowflake_account'),
        user=os.getenv('snowflake_user'),
        password=os.getenv('snowflake_password'),
        database=os.getenv('snowflake_database'),
        schema=os.getenv('snowflake_schema'),
        warehouse=os.getenv('snowflake_warehouse')
    )
    return create_engine(url)