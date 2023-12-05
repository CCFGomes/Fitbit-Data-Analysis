import numpy as np # data arrays
import pandas as pd # data analysis and data manipulation
import datetime as dt #date time
import glob #retrieving file paths
import os #to perform operations related to file and directory handling
import seaborn as sns  # Importing seaborn library for statistical data visualization
import matplotlib.pyplot as plt  # Importing matplotlib.pyplot for creating static visualizations

# Loading data frames using pd.read to read CSV files into a pandas DataFrame
daily_activity = pd.read_csv('../input/fitbit/Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv')
sleepday = pd.read_csv('../input/fitbit/Fitabase Data 4.12.16-5.12.16/sleepDay_merged.csv')
weight_log = pd.read_csv('../input/fitbit/Fitabase Data 4.12.16-5.12.16/weightLogInfo_merged.csv')
heart_rate = pd.read_csv('../input/fitbit/Fitabase Data 4.12.16-5.12.16/heartrate_seconds_merged.csv')

# Check for unique users
print("Daily Activity Dataset:",daily_activity.Id.nunique(), "unique users")
print("SleepDay Dataset:",sleepday.Id.nunique(), "unique users")
print("Weight Log Dataset:",weight_log.Id.nunique(), "unique users")
print("Heart Rate Dataset:",heart_rate.Id.nunique(), "unique users")

# Check for missing values in each dataset
print("Daily Activity Dataset - Missing Values:")
print(daily_activity.isnull().sum())

print("\nSleepDay Dataset - Missing Values:")
print(sleepday.isnull().sum())

print("\nWeight Log Dataset - Missing Values:")
print(weight_log.isnull().sum())

print("\nHeart Rate Dataset - Missing Values:")
print(heart_rate.isnull().sum())

# Check the number of rows in Fat column
total_rows_fat = len(weight_log['Fat'])
print(f"Total number of rows in the 'Fat' column: {total_rows_fat}")

# Since the 'Fat' columns has 67 rows, and 65 of them are missing value, it will be dropped
# Also drop the columns that will not be needed

weight_log = weight_log.drop(columns=['Fat'])
daily_activity = daily_activity.drop(columns=['LoggedActivitiesDistance', 'TrackerDistance'])
sleepday = sleepday.drop(columns=['TotalSleepRecords'])
weight_log = weight_log.drop(columns=['IsManualReport', 'LogId'])

