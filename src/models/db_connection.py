from playhouse.sqlite_ext import PostgresqlDatabase
from src.env_container import env_container

db = PostgresqlDatabase(
    database='CleverBistro_menu_service_db', 
    user='postgres', 
    password='root',      
    host='127.0.0.1', 
    port=5432
)
