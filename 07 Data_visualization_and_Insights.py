
# Plot the correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Activity and Health Metrics")
plt.show()

'''
Comparing correlations:
Calories
Let's compare the correlations of the "Calories" variable with other features in the dataset and provide insights into the relationships:

Calories and TotalActiveMinutes:

Calories have a moderate positive correlation (approximately 0.55) with TotalActiveMinutes.
This indicates that participants who engage in more active minutes tend to burn more calories. It makes intuitive sense, as physical activity leads to higher energy expenditure.
Calories and TotalSteps, TotalDistance:

Calories have a positive correlation with both TotalSteps (approximately 0.73) and TotalDistance (approximately 0.76).
This suggests that participants who take more steps and cover greater distances tend to burn more calories.
It reaffirms the relationship between physical activity (measured by steps and distance) and calorie expenditure.
Calories and VeryActiveMinutes, VeryActiveDistance:

Calories have a relatively strong positive correlation with VeryActiveMinutes (approximately 0.76) and VeryActiveDistance (approximately 0.63).
Participants who spend more time in very active activities and cover longer distances during such activities tend to burn more calories.
Very active activities are likely to be more intense and result in higher calorie burn.
Calories and FairlyActiveMinutes, ModeratelyActiveDistance:

Calories have a moderate positive correlation with FairlyActiveMinutes (approximately 0.42) and ModeratelyActiveDistance (approximately 0.32).
Fairly active and moderately active activities are less intense than very active activities but still contribute to calorie burn.
Calories and LightlyActiveMinutes, LightActiveDistance:

Calories have a moderate positive correlation with LightlyActiveMinutes (approximately 0.22) and LightActiveDistance (approximately 0.46).
Light physical activities contribute to calorie burn, but their impact is relatively lower compared to more intense activities.
It suggests that even light activities, when accumulated over time, can contribute to calorie expenditure.
Calories and TotalHoursAsleep:

Calories and TotalHoursAsleep have a moderate negative correlation (approximately -0.26). This negative correlation indicates that there is an inverse relationship between the number of calories burned and the total minutes of sleep. It suggests that higher calorie burn is associated with fewer total minutes of sleep.
The relationship is not very strong, but indicating that sleep duration may have a some direct impact on daily calorie burn. However, it's important to note that correlation does not necessarily imply causation. The negative correlation between calories and total minutes asleep may be influenced by other factors that affect both variables.
Calories and BMI, WeightKg, Fat:

Calories have a weak negative correlation with BMI (approximately -0.10), and with WeightKg (approximately -0.02) and a very weak positive correlation with Fat (approximately 0.10).
Calories have a weak negative correlation with BMI: Approximately -0.10. This suggests that as BMI (body mass index) increases, calorie burn tends to decrease slightly. In other words, individuals with higher BMI may burn slightly fewer calories compared to those with lower BMI.
Calories have a very weak positive correlation with Fat: Approximately 0.10. This indicates that as the percentage of body fat increases, calorie burn also tends to increase slightly. However, the correlation is quite weak, and other factors are likely to have a more significant impact on calorie burn.
Calories have a very weak negative correlation with WeightKg: Approximately -0.02. This means that as calorie burn decreases, the body weight increases, slightly, but the correlation is so weak that it is not practically significant.
Comparing the impact of activity levels and distances on Calories burned

Both activity levels and distance levels have positive impacts on calorie burn (Calories). However, the correlation values suggest that activity levels (TotalSteps, TotalActiveMinutes, VeryActiveMinutes, LightlyActiveMinutes, FairlyActiveMinutes) have a slightly stronger correlation with Calories compared to distance levels (TotalDistance, LightActiveDistance, ModeratelyActiveDistance, VeryActiveDistance).
This implies that while both increasing overall activity and covering longer distances are beneficial for burning calories, the intensity and engagement in various activity levels play a significant role in calorie expenditure.
Heart rate
Overall, the correlations between heart rate (MinuteAverage and HourlyAverage) and other variables are generally weak, suggesting that heart rate does not have a strong linear relationship with most of the recorded metrics.
However, the positive correlations with physical activity-related variables (TotalSteps, TotalDistance, TotalActiveMinutes, VeryActiveMinutes, LightActiveDistance, and Calories) indicate that higher heart rates may be associated with increased activity levels and energy expenditure during exercise.
The weak negative correlations with TotalHoursAsleep, WeightKg, and Fat suggest a possible association between lower heart rate and better sleep quality, lower body weight, and lower body fat percentage, respectively.
TotalMinutesAsleep
Let's compare the correlations of "TotalHoursAsleep" with other features in the dataset and provide insights into the relationships:

TotalHoursAsleep:

TotalHoursAsleep represents the total number of hours slept by the individual.
TotalHoursAsleep has a weak negative correlation with the following variables:

TotalSteps: Approximately -0.36, indicating a weak negative relationship between the total hours of sleep and the number of steps taken. This suggests that individuals who sleep more may tend to take fewer steps during the day.
TotalDistance: Approximately -0.37, suggesting a weak negative correlation between the total hours of sleep and the total distance covered. This means that individuals who sleep more may cover a shorter distance throughout the day.
TotalActiveMinutes: Approximately -0.12, indicating a weak negative correlation between total hours of sleep and total active minutes. This suggests that individuals who sleep more may engage in fewer active minutes.
VeryActiveMinutes: Approximately -0.33, suggesting a weak negative correlation between total hours of sleep and very active minutes. This means that individuals who sleep more may spend less time in very active activities.
Calories: Approximately -0.26. This means that as the total hours of sleep increase, there is a slight tendency for calorie burn to decrease. In other words, individuals who sleep more may burn slightly fewer calories compared to those who sleep less.
TotalHoursAsleep has a weak positive correlation with the following variable:

WeightKg: Approximately 0.10, indicating a weak positive correlation between total hours of sleep and body weight. This suggests that individuals who sleep more may tend to have a slightly higher body weight.
Other Variables:

TotalSteps, TotalDistance, TotalActiveMinutes, and VeryActiveMinutes have negative correlations with TotalHoursAsleep, suggesting that higher activity levels are associated with shorter sleep durations.
Calories also has a negative correlation with TotalHoursAsleep, indicating that higher calorie burn is associated with shorter sleep durations.
WeightKg has a positive correlation with TotalHoursAsleep, suggesting that higher body weight is associated with longer sleep durations.
Overall, the correlations between TotalHoursAsleep and other variables show that individuals who sleep more tend to be less physically active, cover shorter distances, and burn fewer calories. Additionally, there is a weak positive correlation between total hours of sleep and body weight, indicating that individuals with longer sleep durations may have slightly higher body weights. However, it's important to note that correlation does not imply causation, and other factors may influence these relationships. It's essential to consider individual variations and lifestyle factors when interpreting these correlations.

Weight, BMI and Fat percentage
Weight (WeightKg):

TotalSteps: Very weak positive correlation (0.09) - Suggests a slight tendency for individuals with higher body weight to take slightly more steps, but the impact is not significant.

TotalDistance: Very weak positive correlation (0.11) - Implies that individuals with higher body weight may cover slightly more distance, but the correlation is not strong.

TotalActiveMinutes: Very weak positive correlation (0.01) - Body weight has little to no impact on the total minutes of active physical activity.

TotalHoursAsleep: Very weak negative correlation (-0.05) - Individuals with higher body weight may sleep slightly fewer hours, but the correlation is not significant.

BMI:

TotalSteps: Very weak positive correlation (0.05) - Suggests a slight tendency for individuals with higher BMI values to take slightly more steps, but the impact is not strong.

TotalDistance: Very weak positive correlation (0.05) - Implies that individuals with higher BMI values may cover slightly more distance, but the correlation is not substantial.

TotalActiveMinutes: Very weak positive correlation (0.04) - BMI has little to no impact on the total minutes of active physical activity.

TotalHoursAsleep: Weak negative correlation (-0.11) - Individuals with higher BMI values may sleep slightly fewer hours, but the correlation is not strong.

Fat:

TotalSteps: Very weak positive correlation (0.08) - Suggests a slight tendency for individuals with higher body fat percentages to take slightly more steps, but the impact is not strong.

TotalDistance: Very weak positive correlation (0.10) - Implies that individuals with higher body fat percentages may cover slightly more distance, but the correlation is not significant.

TotalActiveMinutes: Very weak positive correlation (0.04) - Body fat percentage has little to no impact on the total minutes of active physical activity.

TotalHoursAsleep: Very weak negative correlation (-0.04) - Body fat percentage has little to no impact on sleep duration.

The correlations between weight, BMI, and fat with other variables are generally weak, suggesting that these body composition measures alone do not strongly influence physical activity, sleep patterns, or calorie burn.
'''
