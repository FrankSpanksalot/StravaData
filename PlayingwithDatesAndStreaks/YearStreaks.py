import pandas as pd
from io import StringIO
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pytz
import os, sys

os.system("cls")
my_cols =['id','name', 'distance','moving_time','type',
          'average_speed','start_date','total_elevation_gain','gear_id',
          'average_heartrate','elapsed_time','kilojoules','calories','average_cadence','average_watts','weighted_average_watts']

date_format = '%Y-%m-%dT%H:%M:%S%z'

fn = "demo2.csv"
df = pd.read_csv(fn)
# Ensure 'start_date' is a datetime object
df['start_date'] = pd.to_datetime(df['start_date'])
est = pytz.timezone('US/Eastern')

df['start_date'] = df['start_date'].dt.tz_convert(est)
# Filter for 'Ride' or 'VirtualRide'
ride_df = df[df['type'].isin(['Ride', 'VirtualRide'])]

# Extract year and unique dates
ride_df['year'] = ride_df['start_date'].dt.year
ride_df['unique_date'] = ride_df['start_date'].dt.date

# Remove duplicates within the same day
unique_rides = ride_df[['unique_date', 'year']].drop_duplicates()

# Group by year to calculate streaks
streaks_by_year = []
for year, group in unique_rides.groupby('year'):
    # Get unique dates for the year
    unique_dates = sorted(group['unique_date'].unique())
    
    # Calculate differences in days
    date_differences = pd.Series(unique_dates).diff().dt.days
    
    # Identify streaks
    streaks = (date_differences != 1).cumsum()
    
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