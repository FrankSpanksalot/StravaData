import pandas as pd
from io import StringIO
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os, sys,pytz

os.system("cls")
my_cols =['id','name', 'distance','moving_time','type',
          'average_speed','start_date','total_elevation_gain','gear_id',
          'average_heartrate','elapsed_time','kilojoules','calories','average_cadence','average_watts','weighted_average_watts']

date_format = '%Y-%m-%dT%H:%M:%S%z'

fn = "demo2.csv"

df = pd.read_csv(fn)
df['start_date'] = pd.to_datetime(df['start_date']).dt.date
est = pytz.timezone('US/Eastern')

df['start_date'] = df['start_date'].dt.tz_convert(est)
#print(f"ride end date {df.tail(10)['start_date']}")
ride_df = df[df['type'].isin(['Ride', 'VirtualRide'])]
unique_dates= sorted(ride_df['start_date'].unique())
date_differences = pd.Series(unique_dates).diff().dt.days
streaks = (date_differences != 1).cumsum()
streak_lengths = pd.Series(streaks).value_counts()
longest_streak = streak_lengths.max()

# Get the details of the longest streak
streak_index = streak_lengths.idxmax()
longest_streak_dates = pd.Series(unique_dates)[streaks == streak_index]

print(f"Longest streak of consecutive rides (any type): {longest_streak} days")
print("Dates in the longest streak:")
streak_details = (
    pd.DataFrame({"streak_id": streaks, "date": unique_dates})
    .groupby("streak_id")
    .agg(start_date=("date", "min"), streak_length=("streak_id", "size"))
    .sort_values(by="streak_length", ascending=False)
)
exit()
# Get the top 5 streaks
top_5_streaks = streak_details.head(10)
print("Top 5 streaks with their start dates:")
print(top_5_streaks)
exit()
  # Calculate streak lengths
streak_details = (
        pd.DataFrame({"streak_id": streaks, "date": unique_dates})
        .groupby("streak_id")
        .agg(
            start_date=("date", "min"),
            streak_length=("streak_id", "size")
        )
    )
    
    # Get the longest streak for the year
longest_streak = streak_details.sort_values(by="streak_length", ascending=False).head(1)
longest_streak['year'] = year
streaks_by_year.append(longest_streak)

# Combine results for all years
streaks_by_year_df = pd.concat(streaks_by_year).reset_index(drop=True)

print("Longest streaks by year:")
print(streaks_by_year_df)


cycling_df = df[df['type'].isin(['Ride','VirtualRide'])].sort_values(by='start_date')
print(f"ride end date {cycling_df[['start_date']].tail(10)}")
print(len(cycling_df))
# Calculate the difference in days between consecutive activities
cycling_df['days_diff'] = cycling_df['start_date'].diff().dt.days

# Identify streaks (where days_diff == 1)
cycling_df['streak'] = (cycling_df['days_diff'] != 1).cumsum()

# Count the length of each streak
streak_lengths = cycling_df.groupby('streak').size()

# Find the longest streak
longest_streak = streak_lengths.max()
print(f"Longest streak {longest_streak}")
# Get the details of the longest streak
longest_streak_details = cycling_df[cycling_df['streak'] == streak_lengths.idxmax()]

print("Longest streak of consecutive rides and virtual rides:", longest_streak)
print("Details of the longest streak:")
print(longest_streak_details[['start_date', 'type', 'name']])

#print(df.head(3))
#df['start_date'] = pd.to_datetime(df['start_date'])
#df['start_date'] = df['start_date'].dt.date
#datetime.strptime(lastDate, date_format)

#print(df.head(10))
#df = df.sort_values(by=['type','start_date'])
#print(df.head(10))
# df['days_between'] = df.groupby('type')['start_date'].diff().dt.days.fillna(0)
# df['year'] = df['start_date'].dt.year

#print(df[['type','days_between','year']].head(10))

#max_days_by_type_year = df.groupby(['type', 'year'])['days_between'].max().fillna(0).reset_index()
#ride_max_days = max_days_by_type_year[max_days_by_type_year['type'] == 'Ride']
#print(ride_max_days)


#three_ago = datetime.now()-relativedelta(years=4)
#print(three_ago)