import mysql.connector

def connect_to_mysql(host, port, user, password, database, auth_plugin='mysql_native_password'):

    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
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
