from data import retrieve_data
import pandas as pd
import glob
import time
from datetime import datetime
data = retrieve_data()

# files = glob.glob("csv/table.csv")
# df = pd.read_csv(files[0])
# dff = df['date']
# for row in dff.items():
#     t = datetime.strptime(row[1], '%Y-%m-%d')
#     print(t.timestamp())
#     print("\n")

import calendar
#print(calendar.timegm(time.strptime('2000-01-01', '%Y-%m-%d')))