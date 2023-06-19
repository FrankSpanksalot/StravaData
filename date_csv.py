import pandas as pd, os
import numpy as np
from datetime import datetime, timedelta

date_format = '%Y-%m-%dT%H:%M:%S%z'
lastDate = '2023-06-13T23:50:39+00:00'
after_date = (datetime.strptime(lastDate, date_format))+timedelta(hours=-6)
print(after_date)
""" print(datetime.now().strftime('%Y-%m-%d'))

print((datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d'))

fn = "demo1.csv"
if not os.path.isfile(fn):
    print("true")
else:
    print("file exist")

d = pd.read_csv(fn)

lastDate = d.sort_values(by='start_date').iloc[-1]['start_date']


for g in [x for x in d['gear_id'].unique() if not pd.isna(x)]:
    print(g) """