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

fn = "demo2.csv"
df = pd.read_csv(fn)
# Convert start_date to datetime and adjust for timezone
df['start_date'] = pd.to_datetime(df['start_date'])
est = pytz.timezone('US/Eastern')

df['start_date'] = df['start_date'].dt.tz_convert(est)
#df['start_date_et'] = df['start_date'].dt.tz_localize('UTC').dt.tz_convert('US/Eastern')

# Add a column for unique date in Eastern Time
df['unique_date_et'] = df['start_date'].dt.date

# Filter for cycling activities (Ride or VirtualRide)
cycling_activities = df[df['type'].isin(['Ride', 'VirtualRide'])]

# Get unique dates for cycling activities
cycling_dates = cycling_activities.drop_duplicates(subset=['unique_date_et']).sort_values(by='unique_date_et')

# Calculate streaks
cycling_dates['date_diff'] = cycling_dates['unique_date_et'].diff().dt.days
cycling_dates['streak_id'] = (cycling_dates['date_diff'] != 1).cumsum()

# Analyze streaks
streaks = (
    cycling_dates.groupby('streak_id')
    .agg(
        start_date=('unique_date_et', 'min'),
        end_date=('unique_date_et', 'max'),
        streak_length=('streak_id', 'size')
    )
    .sort_values(by='streak_length', ascending=False)
)

# Select top 10 longest streaks
top_10_streaks = streaks.head(10)

# Display the results
print(top_10_streaks)