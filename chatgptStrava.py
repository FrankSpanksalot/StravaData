import stravalib
import webbrowser
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()
client_id= os.getenv('CLIENT_ID')
client_secret =os.getenv('CLIENT_SECRET')

# Authenticate your application
client = stravalib.client.Client()
#authorize_url = client.authorization_url(client_id=client_id, redirect_uri='http://localhost:8000/authorized')
authorize_url = client.authorization_url(client_id=client_id, redirect_uri="http://localhost", scope=['read_all','profile:read_all','activity:read_all'])

webbrowser.open(authorize_url)
# Visit the authorize_url and authenticate your application

# Fetch activities for the last year
now = datetime.now()
last_year = now - timedelta(days=365)
activities = client.get_activities(after=last_year, limit=200)
print(len(activities))
# The API limits the number of activities returned in a single request, so you might need to make multiple requests
