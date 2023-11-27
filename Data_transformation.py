# Check Data type

print("Daily Activity data type is", daily_activity["ActivityDate"].dtypes, "data type")
print("Sleepday data type is", sleepday["SleepDay"].dtypes, "data type")
print("Weight Log data type is", weight_log["Date"].dtypes, "data type")
print("Heart Rate data type is", heart_rate["Time"].dtypes, "data type")

# Transform Date to DateTime data type

daily_activity["ActivityDate"] = pd.to_datetime(daily_activity["ActivityDate"])
sleepday['SleepDay'] = pd.to_datetime(sleepday['SleepDay'])
weight_log['Date'] = pd.to_datetime(weight_log['Date'])
heart_rate['Time'] = pd.to_datetime(heart_rate['Time'])

# Check the changes
print("Daily Activity data type is", daily_activity["ActivityDate"].dtypes, "data type")
print("Sleepday data type is", sleepday["SleepDay"].dtypes, "data type")
print("Weight Log data type is", weight_log["Date"].dtypes, "data type")
print("Heart Rate data type is", heart_rate["Time"].dtypes, "data type")

# Checking duplicates
print(daily_activity['ActivityDate'].duplicated().any())
print(sleepday['SleepDay'].duplicated().any())
print(weight_log['Date'].duplicated().any())
print(heart_rate['Time'].duplicated().any())


# Checking missing values
print(daily_activity['ActivityDate'].isnull().any())
print(sleepday['SleepDay'].isnull().any())
print(weight_log['Date'].isnull().any())
print(heart_rate['Time'].isnull().any())

# Handling missing value and removing duplicates
# 1. daily_activity:
daily_activity.dropna(inplace=True)  # Handle missing values by removing rows with missing values
daily_activity.drop_duplicates(inplace=True)  # Remove duplicates based on all columns

# 2. sleep_day:
sleepday.dropna(inplace=True)  # Handle missing values by removing rows with missing values
sleepday['TotalMinutesAsleep'] = sleepday['TotalMinutesAsleep'] / 60  # Convert 'TotalMinutesAsleep' from minutes to hours
sleepday.drop_duplicates(inplace=True)  # Remove duplicates based on the combination of 'TotalMinutesAsleep' and 'TotalTimeInBed' columns to ensure that only unique sleep records are kept in the dataset

# 3. weight_log:
weight_log.fillna(method='ffill', inplace=True)  # Handle missing values by imputing with the previous non-missing value
weight_log.drop_duplicates(inplace=True)  # Remove duplicates based on the 'LogId' column since it represents unique log entries
weight_log.dropna(subset=['Fat', 'BMI', 'IsManualReport'], inplace=True)  # Drop rows with missing values in specified columns

# 4. heart_rate:
heart_rate.fillna(method='ffill', inplace=True)  # Handle missing values by imputing with the previous non-missing value
heart_rate.drop_duplicates(inplace=True)  # Remove duplicates based on the 'Id' column since it represents unique log entries

# Rename the column 'TotalMinutesAsleep' to 'TotalHoursAsleep'

sleepday.rename(columns={'TotalMinutesAsleep': 'TotalHoursAsleep'}, inplace=True)

# Replace date/time column names with 'ActivityDate' in the daily_activity dataframe
daily_activity = daily_activity.rename(columns={'ActivityDate': 'ActivityDate'})

# Replace date/time column names with 'ActivityDate' in the sleepday dataframe
sleepday = sleepday.rename(columns={'SleepDay': 'ActivityDate'})

# Replace date/time column names with 'ActivityDate' in the weight_log dataframe
weight_log = weight_log.rename(columns={'Date': 'ActivityDate'})

# Replace date/time column names with 'ActivityDate' in the heart_rate dataframe
heart_rate = heart_rate.rename(columns={'Time': 'ActivityDate'})


# Check the dataframe columns
print("Daily Activity:",daily_activity.columns)
print("Sleepday:",sleepday.columns)
print("Weight Log:",weight_log.columns)
print("Heart Rate:",heart_rate.columns)

# Creating new columns in the daily_activity DataFrame

# For 'TotalActiveMinute' column, sum all the active minutes ('VeryActiveMinutes', 'FairlyActiveMinutes', and 'LightlyActiveMinutes') 
# For the 'TotalMinute', sum the "TotalActiveMinute' and the''SedentaryMinute''
daily_activity["TotalActiveMinutes"] = daily_activity["VeryActiveMinutes"] + daily_activity["FairlyActiveMinutes"] + daily_activity["LightlyActiveMinutes"]
daily_activity["TotalMinutes"] = daily_activity["TotalActiveMinutes"] + daily_activity["SedentaryMinutes"]
daily_activity["TotalActiveHours"] = round(daily_activity["TotalActiveMinutes"] / 60)

Concatenate the DataFrames

# Step 1: Concatenate the DataFrames vertically to combine all the data
combined_df = pd.concat([daily_activity, sleepday, weight_log, heart_rate], ignore_index=True)

# Step 2: Sort the combined DataFrame by "ActivityDate" 
combined_df.sort_values(by='ActivityDate', inplace=True)

# Step 3: Merge the data using forward fill (ffill) to fill NaN values in subsequent columns
combined_df.ffill(inplace=True)

print(combined_df)

# Handle Missing Values
# Replace missing values in numeric columns with their mean
numeric_cols = ['TotalSteps', 'TotalDistance', 'TrackerDistance', 'LoggedActivitiesDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance', 'SedentaryActiveDistance', 'Calories', 'TotalActiveMinutes', 'TotalMinutes', 'TotalActiveHours', 'SedentaryMinutes', 'TotalSleepRecords', 'TotalHoursAsleep', 'TotalTimeInBed', 'WeightKg', 'WeightPounds', 'Fat', 'BMI', 'MinuteAverage', 'HourlyAverage']
combined_df[numeric_cols] = combined_df[numeric_cols].fillna(combined_df[numeric_cols].mean())

# Reset the index after dropping rows
combined_df.reset_index(drop=True, inplace=True)

# Check if any missing values remain
print(combined_df.isnull().sum())

