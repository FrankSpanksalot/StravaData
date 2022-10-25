import json, pprint

f = open('athleteJsonreturn.txt')
data = json.load(f)
#pprint.pprint(data)

print(data["username"])


bikes = data["bikes"]

print(len(bikes))

for bike in bikes:
    print(f" Bike Name : {bike['name']} , id {bike['id']}, miles = {bike['distance']/1609}")

