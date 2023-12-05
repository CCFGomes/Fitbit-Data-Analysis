# Fitbit Data Analysis

This repository contains the code and documentation for a data analysis conducted for Fitbit, a high-tech manufacturer of health-focused products for women.

## Objective

The objective of this analysis was to gain insights into consumer smart device usage patterns and provide data-driven recommendations to guide future marketing strategies for fitbit.

## Data Analysis Process

The data analysis process followed a structured approach, including the steps of asking relevant questions, preparing the data, processing and analyzing the data, sharing insights, and taking actionable steps.

## Technologies Used

- Python
- Jupyter Notebook
- Data visualization libraries (Matplotlib, Seaborn)
- Statistical analysis tools (Pandas, NumPy)

## Key Findings and Insights

The analysis revealed key trends, patterns, and correlations in consumer smart device usage data. These findings have direct implications for Fitbit's marketing strategies, allowing them to better understand their target audience and tailor their products and messaging accordingly.

## Repository Structure

- **data**: This directory contains the dataset used for the analysis.
- **notebooks**: Explore Jupyter Notebooks with detailed code and analysis steps.
- **src**: Contains any source code or scripts associated with the project.
- **other_files**: Additional files or resources that support the project.
- **reports**: Holds generated reports, visualizations, or any project-related documentation.

## Getting Started

To replicate or explore the analysis conducted, follow the instructions below:

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Open the Jupyter Notebooks in the `notebooks` directory to view the analysis code and documentation.

## Analysis steps

### 1. **Data Preparation:**
- Goal: **To gain insights from smart device data usage for informed marketing strategies.**
- Business Questions:
  1. What are some trends in smart device usage?
  2. How could these trends apply to Fitbit customers?
  3. How could these trends help influence Fitbit marketing strategy?

   - **Data Source:**
     - Provided details about the Fitbit Fitness Tracker dataset.
     - Mentioned limitations of the data source.
   - **Importing the Required Libraries:**
     - Imported necessary Python libraries.
   - **Data to be Analyzed:**
     - Chose specific datasets for analysis: `daily_activity`, `sleep_day`, `weight_log`, and `heart_rate`.
   - **Loading the Data into a Pandas DataFrame:**
     - Loaded data into DataFrames using `pd.read_csv`.
   - **Data Cleaning:**
     - Checked for unique users, columns, and missing values.
     - Dropped unnecessary columns and handled missing values.
   
### 2. **Data Processing:**
     - Transformed heart rate data by aggregating values into minute averages.
     - Created new columns MinuteAverage and HourlyAverage.
     - Created new columns TotalHoursAsleep and TotalTimeInBedHour, and renamed TotalTimeInBed' to 'TotalTimeInBedMin'
     - Created new columns in the `daily_activity` DataFrame.
### 3. **Data Transformation:**
     - Converted data types to DateTime.
     - Checked for duplicates and missing values.
     - Renamed columns for simplified Data merge.
     - Concatenate DataFrames for Correlation analysis
     - Handle Missing Values by replacing them with their mean
     - Created WeekDay column and reordering columns in merged data frame
   
### 4. **Data Analysis:**
#### **How active are the users along the week?**
<img width="915" alt="Screen Shot 2023-12-05 at 3 41 46 PM" src="https://github.com/CCFGomes/Fitbit-Data-Analysis/assets/103965914/40b13fea-51fc-4fcc-9615-2c56ff83a30d">
       
**Peak Exercise Day:** Tuesday has the highest exercise count among the days of the week, with 790 recorded exercise sessions. This indicates that Tuesday is the day when people are most actively engaging in exercise.
**Consistent Exercise on Weekdays:** Weekdays (Tuesday to Thursday) have higher exercise counts compared to weekends (Saturday and Sunday) with 790, 770 and 742 sessions on Tuesda, Wednesday, and Thursday, respectively.
**Lower Exercise Counts on Weekends:** Sunday and Monday have lower exercise counts compared to weekdays, with 578 and 576 sessions, respectively. These lower counts might suggest that people are less likely to engage in structured exercise activities during the weekend, and it seem hard to get back on track on Monday.
**Moderate Exercise on Friday and Saturday:** Friday and Saturday have a moderate exercise count, with 654 and 639 sessions, respectively. It's typical for exercise counts to be slightly lower at the end of the week.

#### Average Activity Level for Each Day of the Week
<img width="1285" alt="Screen Shot 2023-12-05 at 3 42 16 PM" src="https://github.com/CCFGomes/Fitbit-Data-Analysis/assets/103965914/2e19d4a9-9ed5-4e02-a87d-d1ee3983c08b">

**Total Active Minutes:**
   - Friday and Saturday stand out with higher total active minutes compared to other weekdays.
   - Sunday has the lowest count of active minutes among the weekdays.
**Very Active Minutes:**
   - Friday and Saturday have the highest count of very active minutes, indicating higher-intensity physical activities on these days.
**Lightly Active Minutes:**
   - Lightly active minutes are predominant across all weekdays, suggesting consistent engagement in light physical activities throughout the week.
**Comparison Across Weekdays:**
   - There is variability in active minutes across weekdays, with Friday and Saturday showing a peak in both total and very active minutes.


#### Average Active Distance for Each Day of the Week
<img width="1282" alt="Screen Shot 2023-12-05 at 3 42 58 PM" src="https://github.com/CCFGomes/Fitbit-Data-Analysis/assets/103965914/ac60bb20-4128-4519-9833-349836f92eb0">

**Longer Distances on Wednesday:**
   - Wednesday is notable for having the longest total activity distance compared to other weekdays.
**Saturday as the Second-Longest Distance Day:**
   - Saturday follows Wednesday as the second day with longer activity distances.
**Thursday and Friday:**
   - Thursday and Friday also exhibit good distances, suggesting a consistent level of physical activity.
**Lower Distances from Sunday to Tuesday:**
   - Sunday to Tuesday shows relatively lower activity distances, indicating potentially less engagement in activities that cover longer distances.

#### Observations:

**Different Patterns for Minutes and Distances:**
   - While Friday and Saturday show higher total active minutes and very active minutes, the pattern is different when considering activity distances.
   - Wednesday emerges as the day with both higher total distance and very active minutes.
**Consistency in Light Activity:**
   - Lightly active minutes and distances are consistent across weekdays, indicating regular engagement in lighter physical activities.

#### Data Summary Statistics:
     - Calculated and analyzed summary statistics for numeric columns.  
### Daily Activity Dataset:

- **Steps and Distance:**
  - On average, users take around 7,638 steps, covering approximately 5.49 km per day.
  - Notably, there are instances where users have recorded 0 steps or 0 distance.

- **Active Minutes:**
  - Users spend an average of 227.54 minutes in active pursuits daily.
  - The breakdown shows around 21.16 minutes in very active, 13.56 minutes in fairly active, and 192.81 minutes in lightly active activities.

- **Sedentary Behavior:**
  - Users spend approximately 991 minutes (around 16.5 hours) in sedentary activities daily.

- **Calories Burned:**
  - The average calorie burn is 2,303.61 calories per day.

### SleepDay Dataset:

- **Sleep Duration:**
  - On average, users sleep for around 6.99 hours per night.
  - The standard deviation indicates variability in sleep duration among users.

- **Time in Bed:**
  - Users spend approximately 7.64 hours in bed.
  - The difference between the average sleep duration (6.99 hours) and the average time in bed (7.64 hours) suggests that, on average, users spend about 0.65 hours (39 minutes) in bed but not sleeping. This could be due to factors such as time taken to fall asleep, waking up during the night, or spending extra time in bed without actual sleep.
  
### Weight Log Dataset:

- **Weight and BMI:**
  - The average weight is around 72.04 kg, with an average BMI of 25.19.
  - BMI classifications indicate users, on average, fall into the 'Pre-obesity' category.

### Heart Rate Dataset:

- **Heart Rate Averages:**
  - Users have an average minute heart rate of 74.08 and an average hourly heart rate of 73.42.
  - The standard deviations suggest variability in heart rate values, which is likely to be related to the time during activities.

### Other analysis
- Checking if users meet WHO guidelines for weight and sleep recomendations
- Checking the distribution of heart rate among unique users
<img width="887" alt="Screen Shot 2023-12-05 at 3 43 50 PM" src="https://github.com/CCFGomes/Fitbit-Data-Analysis/assets/103965914/671b9b30-adc5-4843-a54d-bd83d48d6580">

#### Correlation Analysis:
<img width="879" alt="Screen Shot 2023-12-05 at 3 45 18 PM" src="https://github.com/CCFGomes/Fitbit-Data-Analysis/assets/103965914/56d601d4-3314-4712-96de-49412775c7a0">

- ### Correlation of Calories with Other Variables:

#### Strong Positive Correlations:
   - **Calories vs. TotalSteps (0.73):** Strong positive correlation.
   - **Calories vs. TotalDistance (0.76):** Strong positive correlation.
   - **Calories vs. VeryActiveMinutes (0.76):** Strong positive correlation.

#### Moderate Positive Correlations:
   - **Calories vs. VeryActiveDistance (0.63):** Moderate positive correlation.
   - **Calories vs. FairlyActiveMinutes (0.42):** Moderate positive correlation.
   - **Calories vs. LightActiveDistance (0.46):** Moderate positive correlation.

#### Weak Positive Correlations:
   - **Calories vs. ModeratelyActiveDistance (0.32):** Weak positive correlation.
   - **Calories vs. LightlyActiveMinutes (0.22):** Weak positive correlation.
   
#### Weak Negative Correlations:
   - **Calories vs. TotalHoursAsleep (-0.26):** Weak negative correlation.

### Insights:
   - The correlation matrix values align with the provided insights.
   - Higher steps, longer distances, and more very active minutes are strongly correlated with more burned calories.
   - Moderate activities and longer light active distances also show positive correlations with calories but to a lesser extent.
   - The weak negative correlation between total hours of sleep and calories suggests a slight tendency for fewer calories burned with longer sleep. Alternatively, it could imply that as more calories are burned, there is a slight tendency for less sleep. The direction of causation is not clear from the correlation alone, and further investigation or complementary data may be needed to establish a causal relationship.

### Correlation of WeightKg with Other Variables:

#### Moderate Positive Correlations:
   - **WeightKg vs. BMI (0.63):** Moderate positive correlation.
   - **WeightKg vs. MinuteAverage (0.23):** Very weak positive correlation.

#### Insights:
   - The correlation matrix values align with the provided insights.
   - Weight has a moderate positive correlation with BMI, as expected.
   - Weight has a very weak positive correlation with MinuteAverage, suggesting minimal impact on heart rate variance.

### Correlation of TotalHoursAsleep with Other Variables:

#### Negative Correlations:
   - **TotalHoursAsleep vs. VeryActiveDistance (-0.41):** Moderate negative correlation.
   - **TotalHoursAsleep vs. TotalSteps (-0.36):** Weak negative correlation.
   - **TotalHoursAsleep vs. TotalDistance (-0.37):** Weak negative correlation.
   - **TotalHoursAsleep vs. VeryActiveMinutes (-0.33):** Weak negative correlation.

#### Insights:
   - Longer total hours of sleep show moderate negative correlations with very active distance, total steps, total distance, and very active minutes.
   - This suggests that more active individuals may have slightly less sleep time
### 5 Actionable insights and recommendations

   ### Trends in Smart Device Usage:

1. **Exercise Patterns:**
   - Users are most active on weekdays, with Tuesday being the peak exercise day.
   - Weekends (Saturday and Sunday) show lower exercise counts, suggesting potential variations in structured exercise routines during the weekend.

2. **Active Minutes and Distances:**
   - Friday and Saturday consistently have higher total active minutes and very active minutes.
   - Wednesday stands out for longer total activity distances.
   - Lightly active minutes and distances remain consistent across weekdays.

3. **Sleep Duration:**
   - The average sleep duration is around 6.99 hours per night, with variability among users.
   - Users spend approximately 7.64 hours in bed, suggesting some time spent in bed without actual sleep.

4. **Weight and BMI:**
   - The average weight is around 72.04 kg, with an average BMI of 25.19, falling into the 'Pre-obesity' category on average.

5. **Heart Rate Averages:**
   - Users have an average minute heart rate of 74.08 and an average hourly heart rate of 73.42.
   - Variability in heart rate values indicates potential fluctuations during different activities.

### Application to Fitbit Customers:

1. **Tailored Exercise Plans:**
   - Fitbit can tailor exercise plans to align with observed trends, emphasizing peak exercise days and adjusting recommendations for weekends.

2. **Sleep and Recovery Recommendations:**
   - Fitbit could provide insights and recommendations to improve sleep quality, considering the average sleep duration and time spent in bed without sleep.

3. **Weight Management Support:**
   - Fitbit can offer personalized weight management support based on observed weight and BMI trends, providing targeted advice and goals.

4. **Heart Rate Monitoring Optimization:**
   - Fitbit could optimize heart rate monitoring features by considering variability during different activities, providing more accurate insights into users' cardiovascular health.

### Influence on Fitbit Marketing Strategy:

1. **Promotion of Weekday Engagement:**
   - Fitbit could strategically promote features, challenges, or rewards that encourage weekday engagement, leveraging the observed peak exercise days.

2. **Sleep Improvement Features:**
   - Marketing efforts could highlight features aimed at improving sleep quality, addressing the observed average sleep duration and time spent in bed without sleep.

3. **Weight Management Campaigns:**
   - Fitbit could run targeted campaigns focusing on weight management, leveraging insights into average weight and BMI categories.

4. **Heart Health Awareness:**
   - Marketing messages could emphasize the importance of heart health, showcasing how Fitbit's heart rate monitoring features adapt to various activities.

5. **Customized Recommendations:**
   - Fitbit's marketing strategy can highlight the platform's ability to provide personalized recommendations based on observed trends, enhancing the user experience.
  
### 6. **Conclusion:**

   ### Conclusion:

In conclusion, the in-depth analysis of Fitbit user data has unearthed valuable insights into exercise patterns, sleep duration, weight metrics, heart rate averages, and device usage trends. These findings present a comprehensive picture of user behaviors and provide actionable recommendations for both Fitbit users and the company.

#### Key Takeaways:

1. **Exercise Patterns:**
   - Users showcase a strong inclination towards exercise on weekdays, peaking on Tuesdays. Weekends exhibit a decline in structured exercise, indicating potential variations in users' routines.

2. **Sleep Metrics:**
   - The average sleep duration hovers around 6.99 hours, accompanied by an average of 7.64 hours spent in bed. Variability in sleep patterns emphasizes the need for personalized sleep insights.

3. **Weight and BMI:**
   - The average weight of approximately 72.04 kg places users in the 'Pre-obesity' category, emphasizing the importance of weight management support.

4. **Heart Rate Averages:**
   - Users demonstrate diverse heart rate averages during different activities, showcasing the potential for enhanced heart health monitoring and insights.

#### Recommendations for Fitbit:

1. **Tailored Exercise Plans:**
   - Fitbit can capitalize on observed exercise trends to provide tailored plans, optimizing engagement on peak exercise days and adapting recommendations for weekends.

2. **Sleep Improvement Features:**
   - Enhancements to sleep tracking features can address average sleep duration, offering personalized insights for improved sleep quality and overall well-being.

3. **Weight Management Support:**
   - Fitbit can offer targeted weight management support, aligning with average weight and BMI trends to guide users towards healthier lifestyles.

4. **Heart Health Optimization:**
   - Further optimization of heart rate monitoring features will enhance Fitbit's ability to deliver accurate insights into users' cardiovascular health during various activities.

#### Marketing Strategy Implications:

1. **Strategic Promotions:**
   - Fitbit's marketing can strategically promote features, challenges, or rewards to maximize user engagement on weekdays, leveraging observed peak exercise days.

2. **Sleep Optimization Campaigns:**
   - Marketing efforts can focus on sleep improvement features, emphasizing Fitbit's role in enhancing sleep quality and overall well-being.

3. **Weight Management Initiatives:**
   - Targeted campaigns can highlight Fitbit's role in weight management, offering users personalized strategies to achieve their health goals.

4. **Heart Health Awareness:**
   - Fitbit can run awareness campaigns emphasizing the importance of heart health and how the platform adapts to users' cardiovascular activities.

In essence, this analysis equips Fitbit with the knowledge needed to refine its offerings, providing users with more personalized and effective tools for their health and wellness journeys. The insights gained are instrumental in shaping Fitbit's future strategies, ensuring continued empowerment of users in their pursuit of healthier lifestyles.

