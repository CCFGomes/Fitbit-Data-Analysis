# How active are the users along the week?

# Create the "WeekDay" column based on the day of the week names
daily_activity['WeekDay'] = daily_activity['ActivityDate'].dt.day_name()
​
# Check which day people do more exercise
weekday_counts = daily_activity['WeekDay'].value_counts()
​
# Print the count of exercises for each day
print("Exercise counts for each day:")
print(weekday_counts)

# Exercise counts for each day
weekday_counts = {
    'Sunday': 578,
    'Monday': 576,
    'Tuesday': 790,
    'Wednesday': 770,
    'Thursday': 742,
    'Friday': 654,
    'Saturday': 639,
    
}

# Define the order of weekdays based on the provided counts
weekday_order = list(weekday_counts.keys())

# Use a color-blind-friendly palette
colors = sns.color_palette("Set3")

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a bar plot with different colors
bars = plt.bar(weekday_counts.keys(), weekday_counts.values(), color=colors)

# Add labels and title
plt.xlabel('Day of the Week')
plt.ylabel('Exercise Counts')
plt.title('Exercise Counts for Each Day')

# Add numbers on each bar
for bar, count in zip(bars, weekday_counts.values()):
    plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() + 10, str(count), ha='center', color='black')

# Show the plot
plt.show()

# Average Activity Level for Each Day of the Week

active_minutes_columns = ['LightlyActiveMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes']
active_minutes_avg = daily_activity.groupby('WeekDay')[active_minutes_columns].mean().reindex(weekday_order)
​
# Set up the figure with larger size
plt.figure(figsize=(18, 12))
​
# Grouped bar plot with stacked bars for average active minutes
ax1 = plt.subplot(2, 1, 1)
active_minutes_avg.plot(kind='bar', stacked=True, color=['skyblue', 'lightgreen', 'salmon'], ax=ax1)
​
# Adding numbers to each bar for average active minutes
for i, day in enumerate(weekday_order):
    total_height = 0
    for col in active_minutes_columns:
        value = active_minutes_avg.loc[day, col]
        plt.text(i, total_height + value / 2, f'{value:.2f}', ha='center', va='center', color='black')
        total_height += value
​
# Adding legend for average active minutes with more space
ax1.legend(["Light Active Minutes", "Fairly Active Minutes", "Very Active Minutes"], bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., ncol=1)
​
# Adding labels and title for average active minutes
ax1.set_xlabel('Day of the Week')
ax1.set_ylabel('Average Activity Intensity (min)')
ax1.set_title('Average Activity Level for Each Day of the Week')
​
# Average Activity Distance for Each Day of the Week

active_distance_columns = ['LightActiveDistance', 'ModeratelyActiveDistance', 'VeryActiveDistance']
active_distance_avg = daily_activity.groupby('WeekDay')[active_distance_columns].mean().reindex(weekday_order)
​
# Set up the figure with larger size
plt.figure(figsize=(18, 12))
​
# Grouped bar plot with stacked bars for average activity distance
ax2 = plt.subplot(2, 1, 2)
active_distance_avg.plot(kind='bar', stacked=True, color=['skyblue', 'lightgreen', 'salmon'], ax=ax2)
​
# Adding numbers to each bar for average activity distance
for i, day in enumerate(weekday_order):
    total_height = 0
    for col in active_distance_columns:
        value = active_distance_avg.loc[day, col]
        plt.text(i, total_height + value / 2, f'{value:.2f}', ha='center', va='center', color='black')
        total_height += value
​
# Adding legend for average activity distance with more space
ax2.legend(["Light Active Distance", "Moderately Active Distance", "Very Active Distance"], bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., ncol=1)
​
# Adding labels and title for average activity distance
ax2.set_xlabel('Day of the Week')
ax2.set_ylabel('Average Active Distance (km)')
ax2.set_title('Average Active Distance for Each Day of the Week')
​
# Checking the columns of combined_df
combined_df.columns

# Calculate summary statistics for numeric columns
summary_stats = combined_df.describe()

# Display the summary statistics
(summary_stats)


# Checking if users meet WHO guidelines

# Aggregate data at the user level
user_aggregated_df = daily_activity.groupby('Id').agg({
    'LightlyActiveMinutes': 'sum',
    'FairlyActiveMinutes': 'sum',
    'VeryActiveMinutes': 'sum',
    'SedentaryMinutes': 'sum'
}).reset_index()
​
# Create a new column indicating whether the user meets the aerobic activity guidelines
user_aggregated_df['Meets_Aerobic_Guidelines'] = (
    (user_aggregated_df['LightlyActiveMinutes'] >= 150) |
    ((user_aggregated_df['FairlyActiveMinutes'] + user_aggregated_df['VeryActiveMinutes']) >= 75) |
    (((user_aggregated_df['LightlyActiveMinutes'] + user_aggregated_df['FairlyActiveMinutes'] + user_aggregated_df['VeryActiveMinutes']) >= 150) &
     ((user_aggregated_df['FairlyActiveMinutes'] + user_aggregated_df['VeryActiveMinutes']) <= 300))
)
​
# Create a new column indicating whether the user meets the muscle-strengthening guidelines
user_aggregated_df['Meets_Muscle_Strengthening_Guidelines'] = (
    user_aggregated_df['FairlyActiveMinutes'] >= 2
)
​
# Create a new column indicating whether the user meets the sedentary behavior guidelines
user_aggregated_df['Meets_Sedentary_Behavior_Guidelines'] = (
    user_aggregated_df['SedentaryMinutes'] <= 720  # WHO suggests limiting sedentary time, using 720 (12 hours)
)
​
# Print the count of users meeting each guideline
print(f"Number of users meeting aerobic activity guidelines: {user_aggregated_df['Meets_Aerobic_Guidelines'].sum()}")
print(f"Number of users meeting muscle-strengthening guidelines: {user_aggregated_df['Meets_Muscle_Strengthening_Guidelines'].sum()}")
print(f"Number of users meeting sedentary behavior guidelines: {user_aggregated_df['Meets_Sedentary_Behavior_Guidelines'].sum()}")

# Group by 'Id' and create a new column indicating sleep duration categories
sleepday['SleepDurationCategory'] = pd.cut(
    sleepday.groupby('Id')['TotalHoursAsleep'].transform('mean'),
    bins=[0, 7, 9, float('inf')],
    labels=['Less than 7 hours', '7-9 hours', 'More than 9 hours']
)

# Count the number of unique users in each sleep duration category
unique_sleep_duration_counts = sleepday.groupby('SleepDurationCategory')['Id'].nunique()

# Display the counts
print(unique_sleep_duration_counts)

id_column_name = 'Id'
bmi_column_name = 'BMI'
classification_column_name = 'BMI_Classification'

# Create a new column 'BMI_Classification' to store the classification for each user
weight_log['BMI_Classification'] = pd.cut(
    weight_log[bmi_column_name],
    bins=[0, 18.5, 24.9, 29.9, 34.9, 39.9, float('inf')],
    labels=['Underweight', 'Normal weight', 'Pre-obesity', 'Obesity class I', 'Obesity class II', 'Obesity class III']
)

# Drop duplicate rows based on 'Id' to keep only unique users
unique_users_df = weight_log.drop_duplicates(subset=['Id'])

# Group by 'BMI_Classification' and count the occurrences for each classification
bmi_counts = unique_users_df['BMI_Classification'].value_counts()

# Display the counts for each BMI classification
print(bmi_counts)

# Get the 14 unique users from the heart_rate dataset
unique_users = heart_rate['Id'].unique()[:14]

# Filter heart_rate data for these users
filtered_heart_rate = heart_rate[heart_rate['Id'].isin(unique_users)]

# Calculate the average heart rate for each user
average_heart_rate = filtered_heart_rate.groupby(['Id'])['MinuteAverage'].mean().reset_index()

print(average_heart_rate)

# Distribution of Heart Rate in Minutes for Each User 
plt.figure(figsize=(12, 8))
sns.boxplot(data=heart_rate, x='Id', y='MinuteAverage')
plt.title('Distribution of Heart Rate in Minutes for Each User')
plt.xticks(rotation=45, ha='right')  
plt.show()

# Correlation Matrix:

# Find the number of unique users in combined_df dataframe
unique_users_count = combined_df['Id'].nunique()
print(f"Number of unique users: {unique_users_count}")

combined_df.columns

# Rename the column 'SedentaryActiveDistance' to 'SedentaryDistance'
combined_df.rename(columns={'SedentaryActiveDistance': 'SedentaryDistance'}, inplace=True)

# Correlation analysis with the updated column name
correlation_matrix = combined_df[['TotalSteps', 'TotalDistance', 'TotalActiveMinutes', 'TotalMinutes',
                                   'LightlyActiveMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes',
                                   'SedentaryMinutes', 'LightActiveDistance', 'ModeratelyActiveDistance',
                                   'VeryActiveDistance', 'SedentaryDistance', 'Calories',
                                   'TotalHoursAsleep', 'WeightKg', 'BMI', 'MinuteAverage']].corr()

# Set up the matplotlib figure
plt.figure(figsize=(12, 10))

# Customize the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, annot_kws={"size": 8})

# Rotate the axis labels for better readability
plt.xticks(rotation=90)

# Add a title
plt.title('Correlation Matrix')

# Display the plot
plt.show()



