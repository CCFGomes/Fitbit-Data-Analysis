# Filter out days with < 200 TotalSteps taken
filtered_daily_activity = daily_activity[daily_activity['TotalSteps'] > 200]

# Group by 'Id' and count the number of days used
daily_use2 = filtered_daily_activity.groupby('Id')['ActivityDate'].count().reset_index()
daily_use2.rename(columns={'ActivityDate': 'daysused'}, inplace=True)

# Assign usage categories based on the number of days used
daily_use2['Usage'] = pd.cut(daily_use2['daysused'], bins=[0, 14, 21, 31],
                             labels=['Low Use', 'Moderate Use', 'High Use'])

# Calculate percentage and total participants for each usage type
daily_use = daily_use2.groupby('Usage').agg(participants=('Id', 'nunique')).reset_index()
daily_use['perc'] = (daily_use['participants'] / daily_use['participants'].sum()) * 100
daily_use['perc'] = daily_use['perc'].map('{:.0f}%'.format)

# Plot the pie chart for distribution of different usage types
plt.figure(figsize=(4, 4))
plt.pie(daily_use['participants'], labels=daily_use['Usage'], autopct='%1.0f%%', startangle=90,
        colors=plt.cm.Pastel1.colors)
plt.title('Usage Group Distribution')
plt.axis('equal')
plt.show()

'''
The pie chart illustrates the distribution of participants in different usage categories based on the number of days they have actively used the Fitbit tracker, filtering out days with less than 200 TotalSteps taken. The usage categories are defined as follows:

Low Use: Participants who used the Fitbit tracker for less than or equal to 14 days.
Moderate Use: Participants who used the Fitbit tracker for more than 14 days but less than or equal to 21 days.
High Use: Participants who used the Fitbit tracker for more than 21 days.
Insights:

Majority of Participants: The largest segment of participants (73%) fall under the "High Use" category, indicating that a significant number of users actively engaged with their Fitbit trackers for more than 21 days.

Moderate Use: The "Moderate Use" category accounts for the second largest proportion of participants (21%). This suggests that a substantial number of users used their Fitbit trackers for more than two weeks but did not reach the threshold of using it for more than 21 days.

Low Use: The smallest segment is the "Low Use" category (6%), representing users who used the Fitbit tracker for less than or equal to 14 days. This indicates a relatively smaller group of participants who may have used the device for a brief period or infrequently.

About Missing Data: According to this chart, we can suppose that the missing data in the combined_df DataFrame can be justified by participants not wearing the Fitbit device during certain activities or periods, not recording specific metrics, and not providing continuous data throughout the day.
'''
