import conn as co
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
    # DF 형태로 만든 후 CSV 파일로 저장
    df = pd.DataFrame(r, columns=['farm_id', 'tank_id', 'date', 'do', 'temperature','ph'])
        # NULL 값 존재하는 경우 해당 열의 평균으로 대체
    df.fillna({"do":df["do"].mean(),"ph":df["ph"].mean()}, inplace=True)

    df.to_csv(r'~/aquaponix/db/table.csv')
    # DF의 NULL값 개수 확인
    #df.info()
    
    # DB 연결 종료
    co.close_connection(conn, cursor)

    return df