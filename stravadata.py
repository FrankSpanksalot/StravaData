import requests, os, json
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import pprint

load_dotenv()
client_id= os.getenv('CLIENT_ID')
client_secret =os.getenv('CLIENT_SECRET')
redirect_url = "http://localhost"

session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

auth_base_url = "https://www.strava.com/oauth/authorize"
session.scope =["activity:read_all","profile:read_all"]
auth_link = session.authorization_url(auth_base_url)

print(auth_link)
print("\n")
print(f"click here {auth_link[0]}")

redirect_response = input("Paste url here ")

token_url = "https://www.strava.com/api/v3/oauth/token"
session.fetch_token(
    token_url=token_url,
    client_id = client_id,
    client_secret=client_secret,
    authorization_response=redirect_response,
    include_client_id=True
)

print(f"\n token :  {session.token}")

athlete = session.get("https://www.strava.com/api/v3/athlete")

data = json.loads(athlete.text)
#pprint.pprint(data)

bikes = data["bikes"]

print("\n")
for bike in bikes:
    print(f" Bike Name : {bike['name']} , id {bike['id']}, miles = {bike['distance']/1609}")

activities_url = "https://www.strava.com/api/v3/athlete/activities"
""" header = {'Authorization': 'Bearer '+ session.token['access_token'] }
param = {'per_page': 200, 'page':1} """
url = f"{activities_url}?access_token={session.token['access_token']}&per_page=2"
print(f"\n {url}")
activities = session.get(url).json()

#trying long form


print(activities)