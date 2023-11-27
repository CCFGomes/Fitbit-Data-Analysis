# Calculate summary statistics for numeric columns
summary_stats = combined_df.describe()

# Display the summary statistics
(summary_stats)

'''
Insights from the Summary Statistics:

TotalSteps and TotalDistance:

The average number of steps taken per day is approximately 9.076, with a minimum of 0 steps and a maximum of 36,019 steps.
The average total distance covered per day is around 6.75 km, with a minimum of 0 km and a maximum of 28.03 km.
The standard deviation for both "TotalSteps" and "TotalDistance" is relatively high, indicating significant variability in daily step counts and distances covered among the users.
TotalActiveMinutes and TotalMinutes:

The average total active minutes per day is approximately 253 minutes, ranging from 0 minutes to 552 minutes.
TotalMinutes refers to SedentaryMinutes + TotalActiveMinutes. So we can conclude that SedentaryMinutes is iqual to TotalMinutes(mean:1222) - TotalActiveMinutes(mean:253), which is iqual to 969 sedentary minutes.
The calculated average sedentary minutes per day (approximately 969 minutes) highlights that users spend a significant portion of their day in sedentary activities.
TotalActiveHours:

The average total active hours per day is approximately 3.62 hours, with a minimum of 2 hours and a maximum of 9 hours.
"TotalActiveHours" represents the total number of hours of active minutes in a day.
LightlyActiveMinutes, FairlyActiveMinutes, and VeryActiveMinutes:

The average number of minutes spent in lightly active activities is about 187 minutes, with a minimum of 0 minutes and a maximum of 518 minutes.
The average number of minutes spent in fairly active activities is around 12 minutes, ranging from 0 minutes to 143 minutes.
The average number of minutes spent in very active activities is approximately 17.67 minutes, with a minimum of 0 minutes and a maximum of 210 minutes.
LightActiveDistance, ModeratelyActiveDistance, and VeryActiveDistance:

The average distance covered during lightly active activities is approximately 3.38 km, ranging from 0 km to 10.71 km.
The average distance covered during moderately active activities is about 0.46 km, with a minimum of 0 km and a maximum of 6.48 km.
The average distance covered during very active activities is around 1.29 km, ranging from 0 km to 21.92 km.
Calories:

The average number of calories burned per day is approximately 2288 calories, with a minimum of 0 calories and a maximum of 4900 calories.
The standard deviation for "Calories" is relatively high, indicating significant variability in daily calorie burn among participants.
TotalHoursAsleep:

The average total hours of sleep per day is approximately 7.25 hours, with a minimum of 0.97 hours (around 58 minutes) and a maximum of 13.27 hours (around 13 hours and 16 minutes).
Some participants may have recorded very little sleep (or no sleep) for certain days, while others might have recorded an unusually long duration of sleep.
WeightKg and Fat:

The average weight of the participants is around 72.55 kg, with a minimum weight of 52.60 kg and a maximum weight of 133.50 kg.
The average body fat percentage is about 24.87%, ranging from 22% to 25%.
BMI:

The average BMI (Body Mass Index) is approximately 24.75, with a minimum of 21.45 and a maximum of 47.
A BMI of 47 classifies the user as having severe obesity and, because of this, they are exposed to a higher risk of developing high blood pressure, type 2 diabetes, sleep apnea, or other serious health conditions.
Heart Rate:

The average MinuteAverage heart rate is 71.58 beats per minute, indicating a moderate heart rate for users during recorded minutes, with a minimum of 36, which can be interpreted as a resting time, and a maximum of 191, which can be interpreted as a very active period.
Similarly, the average HourlyAverage heart rate is 71.41 beats per minute, suggesting a moderate heart rate on an hourly basis.
'''
