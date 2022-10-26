import requests, pprint

""" actq = "https://www.strava.com/api/v3/athlete/activities"
ac = "761718f405aa6caf24765599ca3ee66c7edcf4b9"
s = f"{actq}?access_token={ac}&per_page=2"
print(s)

d = requests.get(s).json()
pprint.pprint(d) """

cnt =0
for x in range(19):
    cnt=cnt+1
    print(cnt)