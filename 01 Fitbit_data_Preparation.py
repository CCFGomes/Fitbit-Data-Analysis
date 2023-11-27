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

# Check Common Identifier (Id) 

# Check for missing values in each dataset
print("Daily Activity Dataset - Missing Values:")
print(daily_activity.isnull().sum())

print("\nSleepDay Dataset - Missing Values:")
print(sleepday.isnull().sum())

print("\nWeight Log Dataset - Missing Values:")
print(weight_log.isnull().sum())

print("\nHeart Rate Dataset - Missing Values:")
print(heart_rate.isnull().sum())

# Check the dataframe columns
print("Daily Activity:",daily_activity.columns)
print("Sleepday:",sleepday.columns)
print("Weight Log:",weight_log.columns)
print("Heart Rate:",heart_rate.columns)

# Check the dataframe shape
print("Daily Activity:",daily_activity.shape)
print("Sleepday:",sleepday.shape)
print("Weight Log:",weight_log.shape)
print("Heart Rate:",heart_rate.shape)

# Convert the 'Time' column to a pandas datetime object
heart_rate['Time'] = pd.to_datetime(heart_rate['Time'])

# Calculate the heart rate by minute, grouping the data by 'Id' and minute, then calculate the average heart rate for each minute
MinuteAverage = heart_rate.groupby(['Id', pd.Grouper(key='Time', freq='1Min')])['Value'].mean().reset_index()
MinuteAverage.rename(columns={'Value': 'MinuteAverage'}, inplace=True)

# Calculate the heart rate by hour, grouping the data by 'Id' and hour, then calculate the average heart rate for each hour
HourlyAverage = MinuteAverage.groupby(['Id', pd.Grouper(key='Time', freq='1H')])['MinuteAverage'].mean().reset_index()
HourlyAverage.rename(columns={'MinuteAverage': 'HourlyAverage'}, inplace=True)

# Drop the 'Value' column as it's no longer needed
heart_rate.drop(columns=['Value'], inplace=True)

# Merge the MinuteAverage and HourlyAverage DataFrames back to the original heart_rate DataFrame
heart_rate = pd.merge(heart_rate, MinuteAverage[['Id', 'Time', 'MinuteAverage']], on=['Id', 'Time'])
heart_rate = pd.merge(heart_rate, HourlyAverage[['Id', 'Time', 'HourlyAverage']], on=['Id', 'Time'])

# Display the updated heart_rate DataFrame with the new columns
print(heart_rate.head())

