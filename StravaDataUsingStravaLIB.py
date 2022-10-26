from stravalib.client import Client
from dotenv import load_dotenv
import os
load_dotenv()
client_id= os.getenv('CLIENT_ID')
client_secret =os.getenv('CLIENT_SECRET')

client = Client()
url = client.authorization_url(client_id=client_id, redirect_uri="http://localhost", scope=['read_all','profile:read_all','activity:read_all'])

print(url)

code = input("Paste code here ")
access_token = client.exchange_code_for_token(client_id=client_id, client_secret=client_secret, code=code)

athlete = client.get_athlete()
print("Athlete's name is {} {}, based in {}, {}"
      .format(athlete.firstname, athlete.lastname, athlete.city, athlete.country))

activities = client.get_activities(limit=19)

cnt =0
for activity in activities:
    print(f"{activity.name} {}")
    cnt=cnt+1
print(cnt)