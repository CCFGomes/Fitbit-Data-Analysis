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

# Check the dataframe shape
print("Daily Activity:",daily_activity.shape)
print("Sleepday:",sleepday.shape)
print("Weight Log:",weight_log.shape)
print("Heart Rate:",heart_rate.shape)

# Checking duplicates
print(daily_activity['ActivityDate'].duplicated().any())
print(sleepday['SleepDay'].duplicated().any())
print(weight_log['Date'].duplicated().any())
print(heart_rate['Time'].duplicated().any())

# Removing duplicates
# 1. daily_activity:
daily_activity.drop_duplicates(inplace=True)  

# 2. sleep_day:
sleepday.drop_duplicates(inplace=True)  

# 3. weight_log:
weight_log.drop_duplicates(inplace=True) 

# 4. heart_rate:
heart_rate.drop_duplicates(inplace=True)  

# Checking missing values
print(daily_activity['ActivityDate'].isnull().any())
print(sleepday['SleepDay'].isnull().any())
print(weight_log['Date'].isnull().any())
print(heart_rate['Time'].isnull().any())

# Renaming Columns for Simplified Merge
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

# Concatenate the DataFrames

# Step 1: Concatenate the DataFrames vertically to combine all the data
combined_df = pd.concat([daily_activity, sleepday, weight_log, heart_rate], ignore_index=True)

# Step 2: Sort the combined DataFrame by "ActivityDate" 
combined_df.sort_values(by='ActivityDate', inplace=True)

# Step 3: Merge the data using forward fill (ffill) to fill NaN values in subsequent columns
combined_df.ffill(inplace=True)

print(combined_df)

# Checking duplicates
print(combined_df.duplicated().any())

# Checking missing values
print(combined_df.isnull().any())

# Handle missing values and duplicates
# Replace missing values in numeric columns with their mean
numeric_cols = ['TotalMinutesAsleep', 'TotalTimeInBedMin', 'TotalHoursAsleep', 'TotalTimeInBedHour', 'WeightKg', 'WeightPounds', 'BMI', 'MinuteAverage', 'HourlyAverage']
combined_df[numeric_cols] = combined_df[numeric_cols].fillna(combined_df[numeric_cols].mean())

# Reset the index after dropping rows 
combined_df.reset_index(drop=True, inplace=True)

# Check if any missing values remain
print(combined_df.isnull().sum())

#Removing duplicates
combined_df.drop_duplicates(inplace=True)

print(combined_df.head())

# Create the "WeekDay" column based on the day of the week (Monday: 0, Sunday: 6)
combined_df.loc[:, "WeekDay"] = combined_df["ActivityDate"].dt.weekday

# Create a new list called new_cols with the desired column order for the combined_df DataFrame
new_cols = ["Id", "ActivityDate", "WeekDay",'TotalSteps', 'TotalDistance', 'TotalActiveMinutes', 'TotalMinutes',
            'TotalActiveHours', 'LightlyActiveMinutes', 'FairlyActiveMinutes',
            'VeryActiveMinutes', 'LightActiveDistance', 'ModeratelyActiveDistance',
            'VeryActiveDistance', 'Calories', 'TotalHoursAsleep',
            'WeightKg', 'Fat', 'BMI', 'MinuteAverage', 'HourlyAverage']

# Reorder the columns of the merged_data DataFrame based on the new_cols list
combined_df = combined_df[new_cols]

print(combined_df)
