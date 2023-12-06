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

# Transforming heart rate data by aggregating values into minute averages.
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

# Display the updated heart_rate data frame and its shape
print(heart_rate.head())
print("Heart Rate:",heart_rate.shape)

# Creating new columns TotalHoursAsleep and TotalTimeInBedHour, and renaming TotalTimeInBed' to 'TotalTimeInBedMin'
# Create 'TotalHoursAsleep' by converting 'TotalMinutesAsleep' to hours
sleepday['TotalHoursAsleep'] = sleepday['TotalMinutesAsleep'] / 60

# Create 'TotalTimeInBedHour' by converting 'TotalTimeInBed' to hours
sleepday['TotalTimeInBedHour'] = sleepday['TotalTimeInBed'] / 60

# Rename 'TotalTimeInBed' to 'TotalTimeInBedMin'
sleepday.rename(columns={'TotalTimeInBed': 'TotalTimeInBedMin'}, inplace=True)
sleepday.columns

# Creating new columns in the daily_activity DataFrame
# For 'TotalActiveMinute' column, sum all the active minutes ('VeryActiveMinutes', 'FairlyActiveMinutes', and 'LightlyActiveMinutes') 
# For the 'TotalMinute', sum the "TotalActiveMinute' and the''SedentaryMinute''
daily_activity["TotalActiveMinutes"] = daily_activity["VeryActiveMinutes"] + daily_activity["FairlyActiveMinutes"] + daily_activity["LightlyActiveMinutes"]
daily_activity["TotalMinutes"] = daily_activity["TotalActiveMinutes"] + daily_activity["SedentaryMinutes"]
daily_activity["TotalActiveHours"] = round(daily_activity["TotalActiveMinutes"] / 60)


