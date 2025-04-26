import pandas as pd
fp = "demo2.csv"
df = pd.read_csv(fp)
my_cols =['id','name', 'start_date','distance','moving_time','type', 'sport_type','elapsed_time','gear_id'] 
df["name"] = df["name"].astype(str)

mask = (df["name"].str.contains("gravel", case=False, na=False))  & \
       (~df["name"].str.contains("zwift", case=False, na=False)) & \
        (df["type"] == "Ride") & \
       (df["sport_type"]=="Ride")

mask = (df["sport_type"].str.contains("mounta", case=False)) & \
        (~df["name"].str.contains("apex", case=False, na=False))

mask =(df["gear_id"].isna()) & \
(df["type"]=="Ride") & \
(~df["name"].str.contains("midland,", case=False))

mask = (df["name"].str.contains("pedals", case=False)) & \
        (df["sport_type"]!="GravelRide")

mask = (df["gear_id"].isna()) & \
        (~df["type"].str.contains("ride", case=False))
print(df[mask][my_cols])
print("*" * 40)
#df.loc[mask,"gear_id"]="b1683032"

#df.loc[mask,["sport_type","type"]]=["GravelRide","Ride"]
#print(df[mask][my_cols])
#df.to_csv(fp, index=False) 