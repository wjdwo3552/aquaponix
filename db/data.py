from db import conn as co
import pandas as pd
import numpy as np
def retrieve_and_save_data():
    data = retrieve_data()
    print("데이터 저장됨.")

def retrieve_data():
    #DB 연결
    conn, cursor = co.connect_to_mysql(
        host='121.155.34.16',
        port='33063',
        user='sysop',
        password='data001!',
        database='fms'
    )
    # farm_id, tank_id, date, do, temperature, ph 값 불러오기
    query = "SELECT farm_id, tank_id, date, do, temperature, ph FROM water_quality_day_tb WHERE date > '2023-12-31'"
    r = co.execute_query(cursor, query)


    #data 와 온도만 불러오기
    query = "SELECT date, temperature FROM water_quality_day_tb WHERE date > '2023-12-31'"
    r2 = co.execute_query(cursor, query)
    df2 = pd.DataFrame(r2, columns=['date', 'temperature'])
        # NULL 값 존재하는 경우 해당 열의 평균으로 대체
    df2.to_csv('/Users/smin/visualstudiocode/aquaponix/csv/test.csv', mode='r+', index=False)
    # DF 형태로 만든 후 CSV 파일로 저장
    df = pd.DataFrame(r, columns=['farm_id', 'tank_id', 'date', 'do', 'temperature','ph'])
        # NULL 값 존재하는 경우 해당 열의 평균으로 대체
    df.fillna({"do":df["do"].mean(),"ph":df["ph"].mean()}, inplace=True)

    df.to_csv(r'/Users/smin/visualstudiocode/aquaponix/csv/table.csv')
    # DF의 NULL값 개수 확인
    #df.info()
    
    # DB 연결 종료
    co.close_connection(conn, cursor)

    return df

def rcv_dt():
    conn, cursor = co.connect_to_mysql(
        host='121.155.34.16',
        port='33063',
        user='sysop',
        password='data001!',
        database='fms'
    )
    query = "SELECT farm_id, tank_id, date, do, temperature, ph FROM water_quality_day_tb WHERE date > '2023-12-31'"
    r = co.execute_query(cursor, query)
    print(f'SUCCESS!! : {r.count()}')
    df = pd.DataFrame(r, columns=['farm_id', 'tank_id', 'date', 'do', 'temperature','ph'])
    df.to_csv()

#.Is Sensor alive
def rcv_sensor_status():
    conn, cursor = co.connect_to_mysql()
    query = "SELECT eq_id, status, mea_dt FROM sensor_status_tb"
    r = co.execute_query(cursor, query)
    df = pd.DataFrame(r, columns=['eq_id', 'status', 'mea_dt'] )
    list = df.values.tolist()
    return list
    # 130,1,1,PH 센서
    # 131,1,1,용존산소(DO) 센서
    # 132,1,1,염도센서
    # 133,1,1,수온 센서
    # 142,1,2,PH 센서
    # 143,1,2,용존산소(DO) 센서
    # 145,1,2,염도센서
    # 146,1,2,수온 센서