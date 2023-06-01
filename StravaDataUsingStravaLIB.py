import time, csv, os, pickle, pandas as pd
from stravalib.client import Client, unithelper
from dotenv import load_dotenv
from datetime import datetime, timedelta
load_dotenv()
client_id= os.getenv('CLIENT_ID')
client_secret =os.getenv('CLIENT_SECRET')

client = Client()

with open('access_token.pickle', 'rb') as f:
    access_token = pickle.load(f)
    
print('Latest access token read from file:')
access_token

if time.time() > access_token['expires_at']:
    print('Token has expired, will refresh')
    refresh_response = client.refresh_access_token(client_id=client_id, 
                                               client_secret=client_secret, 
                                               refresh_token=access_token['refresh_token'])
    access_token = refresh_response
    with open('access_token.pickle', 'wb') as f:
        pickle.dump(refresh_response, f)
    print('Refreshed token saved to file')
    client.access_token = refresh_response['access_token']
    client.refresh_token = refresh_response['refresh_token']
    client.token_expires_at = refresh_response['expires_at']
        
else:
    print('Token still valid, expires at {}'
          .format(time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(access_token['expires_at']))))
    client.access_token = access_token['access_token']
    client.refresh_token = access_token['refresh_token']
    client.token_expires_at = access_token['expires_at']

#athlete = client.get_athlete()

cnt =0
miles = 0.0
gear_cols = ['id','name','brand_name','model_name']
my_cols =['id','name', 'distance','moving_time','type',
          'average_speed','start_date','total_elevation_gain','gear_id',
          'average_heartrate','elapsed_time','kilojoules','calories','average_cadence']

data =[]
fn = "demo1.csv"
before_date = (datetime.now()+timedelta(days=1)).strftime('%Y-%m-%d')
if not os.path.isfile(fn):
    with open(fn,'a',encoding='utf-8'):
        print("File Created")
    after_date = datetime.strptime('2009-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
   
else:
    if os.path.getsize(fn)!=0:
        d = pd.read_csv(fn)
        lastDate = d.sort_values(by='start_date').iloc[-1]['start_date']
        date_format = '%Y-%m-%dT%H:%M:%S%z'
        after_date = (datetime.strptime(lastDate, date_format)) # +timedelta(days=1)) #.strftime('%Y-%m-%d')
        gear=[]
        with open('gear.csv', 'w',newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(gear_cols)
            for g in [x for x in d['gear_id'].unique() if not pd.isna(x)]:
                sGear = client.get_gear(gear_id=g)
                writer.writerow([sGear.to_dict().get(x) for x in gear_cols])


print(f'After date {after_date} and before date {before_date}')
#after_date = (datetime.now() + timedelta(days=-32)) #.strftime('%Y-%m-%d')
#before_date = (datetime.now() + timedelta(days=-30)).strftime('%Y-%m-%d')

activities = client.get_activities(after=after_date, before=before_date)

""" for activity in activities:
        activity.name = activity.name.replace("\n","")
        my_dict = activity.to_dict()
        print(my_dict)
        data.append([my_dict.get(x) for x in my_cols])
        print(data)
 """
numberofActivities = len(list(activities))

if numberofActivities==0:
    print("No new Activites found")
    exit()
else:
    print(f"Found {numberofActivities}, adding to file")

with open(fn, 'a',newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    if os.path.getsize(fn)==0:
        writer.writerow(my_cols)
        print("wrote header")
    for activity in activities:
        activity.name = activity.name.replace("\n","")
        my_dict = activity.to_dict()
        data.append([my_dict.get(x) for x in my_cols])
    writer.writerows(data)

#print((datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d'))

#after_date = datetime.strptime('2021-01-01','%Y-%m-%d')
#before_date = datetime.strptime('2023-12-31', '%Y-%m-%d') 

#after_date = (datetime.now() + timedelta(days=-35)).strftime('%Y-%m-%d')
#before_date = (datetime.now() + timedelta(days=-30)).strftime('%Y-%m-%d')
#limit = 10
 #activities = client.get_activities(limit=19)
#activities = client.get_activities(before=before_date,after=after_date)