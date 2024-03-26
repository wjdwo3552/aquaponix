#%%
import matplotlib.pyplot as plt
from db.conn import connect_to_mysql, execute_query, close_connection

def data_check_and_visualize(data1, data2):

    conn, cursor = connect_to_mysql(
        host='121.155.34.16',
        port=33063,
        user='sysop',
        password='data001!',
        database='fms'
    )

    query1 = f"SELECT {data1} FROM water_quality_day_tb"
    query2 = f"SELECT {data2} FROM water_quality_day_tb"

    result1 = execute_query(cursor, query1)
    result2 = execute_query(cursor, query2)


    data_list1 = [row[0] for row in result1]
    data_list2 = [row[0] for row in result2]

    close_connection(conn, cursor)


    plt.plot(data_list1, label=data1)
    plt.plot(data_list2, label=data2)

    plt.title('Water Quality Data')
    plt.xlabel('Days')
    plt.ylabel('ph')
    plt.legend()
    plt.show()

data_check_and_visualize('ph', 'temperature')