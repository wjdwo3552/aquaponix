import mysql.connector
import logging, logging.handlers

def connect_to_mysql(auth_plugin='mysql_native_password'):
    
    connection = mysql.connector.connect(
        host='121.155.34.16',
        port='33063',
        user='sysop',
        password='data001!',
        database='fms',
        auth_plugin=auth_plugin
    )

    cursor = connection.cursor()

    return connection, cursor

def execute_query(cursor, query):
    cursor.execute(query)

    result = cursor.fetchall()

    return result

def close_connection(connection, cursor):
    cursor.close()
    connection.close()
