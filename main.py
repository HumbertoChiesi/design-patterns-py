import mysql.connector
import psycopg2
from pymongo import MongoClient


def connect_mysql(host, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection


def connect_postgresql(host, user, password, database):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=database
    )
    return connection


def connect_mongodb(host, port, username, password, database):
    client = MongoClient(host, port, username=username, password=password)
    db = client[database]
    return db


DB_CONNECTIONS = {}


def register_db_connector(db_type):
    def decorator(fn):
        DB_CONNECTIONS[db_type] = fn
        return fn

    return decorator


@register_db_connector('mysql')
def mysql_connector(host, user, password, database):
    return connect_mysql(host, user, password, database)


@register_db_connector('postgresql')
def postgresql_connector(host, user, password, database):
    return connect_postgresql(host, user, password, database)


@register_db_connector('mongodb')
def mongodb_connector(host, port, username, password, database):
    return connect_mongodb(host, port, username, password, database)


def get_db_connector(db_type):
    if db_type not in DB_CONNECTIONS:
        raise ValueError(f"{db_type} is not a valid")

    return DB_CONNECTIONS[db_type]


def main():
    mysql_conn = get_db_connector('mysql')('localhost', 'user', 'password', 'mydb')
    postgres_conn = get_db_connector('postgresql')('localhost', 'user', 'password', 'mydb')
    mongodb_conn = get_db_connector('mongodb')('localhost', 27017, 'admin', 'password', 'mydb')


if __name__ == '__main__':
    main()
