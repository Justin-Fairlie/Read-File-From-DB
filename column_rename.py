import mysql.connector
import os

conn = mysql.connector.connect(
    host='host',
    port= 8080,
    user='user',
    password='password',
    database='database_name',
)
cursor = conn.cursor()


def rename_column():
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        cursor.execute(f"SHOW COLUMNS FROM {table_name} LIKE 'faecal_colifoms'")
        if cursor.fetchone():
            cursor.execute(f"ALTER TABLE {table_name} CHANGE faecal_colifoms faecal_coliforms decimal(6,2)")
            print(f"Column in table {table_name} renamed successfully.")


rename_column()

