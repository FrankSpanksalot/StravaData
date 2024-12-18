import pandas as pd
from io import StringIO
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os, sys

os.system("cls")
my_cols =['id','name', 'distance','moving_time','type',
          'average_speed','start_date','total_elevation_gain','gear_id',
          'average_heartrate','elapsed_time','kilojoules','calories','average_cadence','average_watts','weighted_average_watts']

date_format = '%Y-%m-%dT%H:%M:%S%z'

fn = "demo2.csv"

df = pd.read_csv(fn)
#print(df.head(3))
df['start_date'] = pd.to_datetime(df['start_date'])
#df['start_date'] = df['start_date'].dt.date
#datetime.strptime(lastDate, date_format)

#print(df.head(10))
df = df.sort_values(by=['type','start_date'])
#print(df.head(10))
df['days_between'] = df.groupby('type')['start_date'].diff().dt.days.fillna(0)
df['year'] = df['start_date'].dt.year

print(df[['type','days_between','year']].head(10))

max_days_by_type_year = df.groupby(['type', 'year'])['days_between'].max().fillna(0).reset_index()
ride_max_days = max_days_by_type_year[max_days_by_type_year['type'] == 'Ride']
print(ride_max_days)
sys.exit()

three_ago = datetime.now()-relativedelta(years=4)
print(three_ago)


dateType = df[['start_date','type']].drop_duplicates()
dateType['start_date'] = pd.to_datetime(dateType['start_date'])

dateType = dateType.sort_values(by=['type','start_date'])
dateType = dateType[dateType['start_date']>three_ago]

dateType['previous_date'] = dateType.groupby('type')['start_date'].shift(1) #.diff().dt.days.fillna(0)


dateType['dBetween']= dateType.groupby('type')['start_date'].diff().dt.days.fillna(0)


top3 = dateType.groupby('type').apply(lambda x: x.nlargest(1,'dBetween')).reset_index(drop=True)

print(top3)
maxdb = dateType.loc[dateType.groupby('type')['dBetween'].idxmax()]
print(maxdb[['type','previous_date','start_date','dBetween']][maxdb['type']=='Ride'])

avgDayByType = dateType.groupby('type')['dBetween'].mean().fillna(0)
print("Average Days Between by type")
print(avgDayByType)