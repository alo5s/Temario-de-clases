import os
import mysql.connector
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

def get_db_connection():
    try:
        db_connection = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST'),
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            port=os.environ.get('MYSQL_PORT'),
            connect_timeout=3600 # Timeout en segundos
        )
        print("Conexión exitosa a la base de datos.")
        return db_connection
    except mysql.connector.Error as err:
        print("Error de conexión a la base de datos:", err)
        return None
    except Exception as e:
        print("Error desconocido:", e)
        return None


