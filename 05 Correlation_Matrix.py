Calculate the correlation matrix
df = combined_df

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Print the correlation matrix
print(correlation_matrix)

'''
                                Id   WeekDay  TotalSteps  TotalDistance  \
Id                        1.000000  0.002936    0.053521       0.063773   
WeekDay                   0.002936  1.000000    0.074058       0.082191   
TotalSteps                0.053521  0.074058    1.000000       0.987553   
TotalDistance             0.063773  0.082191    0.987553       1.000000   
TotalActiveMinutes        0.023239  0.063240    0.719934       0.651848   
TotalMinutes             -0.007118  0.114056    0.097026       0.122763   
TotalActiveHours          0.020538  0.056065    0.736309       0.671653   
LightlyActiveMinutes      0.000735 -0.003556    0.423133       0.351402   
FairlyActiveMinutes       0.006981  0.203004    0.359625       0.333465   
VeryActiveMinutes         0.057085  0.074975    0.762590       0.760408   
LightActiveDistance       0.027151  0.056245    0.589287       0.558477   
ModeratelyActiveDistance  0.003050  0.199246    0.331307       0.304462   
VeryActiveDistance        0.062557  0.025875    0.842484       0.880121   
Calories                  0.093323  0.241706    0.734070       0.758926   
TotalHoursAsleep          0.026280 -0.048477   -0.358232      -0.365259   
WeightKg                  0.057679 -0.205572    0.087087       0.109416   
Fat                       0.007569 -0.085369    0.016591       0.039814   
BMI                       0.018736 -0.263494   -0.033522      -0.030163   
MinuteAverage             0.075169  0.062410    0.048939       0.046679   
HourlyAverage             0.078994  0.104490    0.065706       0.063358   

                          TotalActiveMinutes  TotalMinutes  TotalActiveHours  \
Id                                  0.023239     -0.007118          0.020538   
WeekDay                             0.063240      0.114056          0.056065   
TotalSteps                          0.719934      0.097026          0.736309   
TotalDistance                       0.651848      0.122763          0.671653   
TotalActiveMinutes                  1.000000     -0.025473          0.990537   
TotalMinutes                       -0.025473      1.000000         -0.029576   
TotalActiveHours                    0.990537     -0.029576          1.000000   
LightlyActiveMinutes                0.887411     -0.040825          0.869070   
FairlyActiveMinutes                 0.406925      0.015767          0.377723   
VeryActiveMinutes                   0.407734      0.018826          0.439909   
LightActiveDistance                 0.773787      0.093465          0.758605   
ModeratelyActiveDistance            0.371414      0.036728          0.340769   
VeryActiveDistance                  0.329341      0.093809          0.368914   
Calories                            0.552052      0.154519          0.561747   
TotalHoursAsleep                   -0.118322     -0.038048         -0.143315   
WeightKg                            0.010108     -0.020313          0.014034   
Fat                                -0.066781     -0.085203         -0.049701   
BMI                                -0.035674     -0.113700         -0.030905   
MinuteAverage                       0.035729      0.018493          0.029705   
HourlyAverage                       0.045701      0.013176          0.039445   

                          LightlyActiveMinutes  FairlyActiveMinutes  \
Id                                    0.000735             0.006981   
WeekDay                              -0.003556             0.203004   
TotalSteps                            0.423133             0.359625   
TotalDistance                         0.351402             0.333465   
TotalActiveMinutes                    0.887411             0.406925   
TotalMinutes                         -0.040825             0.015767   
TotalActiveHours                      0.869070             0.377723   
LightlyActiveMinutes                  1.000000             0.134682   
FairlyActiveMinutes                   0.134682             1.000000   
VeryActiveMinutes                    -0.018641             0.270509   
LightActiveDistance                   0.808730             0.133956   
ModeratelyActiveDistance              0.151841             0.963764   
VeryActiveDistance                   -0.006905             0.106835   
Calories                              0.217038             0.424528   
TotalHoursAsleep                      0.003401             0.002237   
WeightKg                              0.058420            -0.138155   
Fat                                  -0.085336            -0.046143   
BMI                                   0.011935            -0.109810   
MinuteAverage                         0.017145             0.017794   
HourlyAverage                         0.020327             0.024924   

                          VeryActiveMinutes  LightActiveDistance  \
Id                                 0.057085             0.027151   
WeekDay                            0.074975             0.056245   
TotalSteps                         0.762590             0.589287   
TotalDistance                      0.760408             0.558477   
TotalActiveMinutes                 0.407734             0.773787   
TotalMinutes                       0.018826             0.093465   
TotalActiveHours                   0.439909             0.758605   
LightlyActiveMinutes              -0.018641             0.808730   
FairlyActiveMinutes                0.270509             0.133956   
VeryActiveMinutes                  1.000000             0.122746   
LightActiveDistance                0.122746             1.000000   
ModeratelyActiveDistance           0.153634             0.135080   
VeryActiveDistance                 0.845366             0.156089   
Calories                           0.759701             0.456871   
TotalHoursAsleep                  -0.326460            -0.073927   
WeightKg                          -0.038988             0.109763   
Fat                                0.043161             0.048691   
BMI                               -0.067822            -0.007126   
MinuteAverage                      0.046858             0.032036   
HourlyAverage                      0.062576             0.045257   

                          ModeratelyActiveDistance  VeryActiveDistance  \
Id                                        0.003050            0.062557   
WeekDay                                   0.199246            0.025875   
TotalSteps                                0.331307            0.842484   
TotalDistance                             0.304462            0.880121   
TotalActiveMinutes                        0.371414            0.329341   
TotalMinutes                              0.036728            0.093809   
TotalActiveHours                          0.340769            0.368914   
LightlyActiveMinutes                      0.151841           -0.006905   
FairlyActiveMinutes                       0.963764            0.106835   
VeryActiveMinutes                         0.153634            0.845366   
LightActiveDistance                       0.135080            0.156089   
ModeratelyActiveDistance                  1.000000            0.061507   
VeryActiveDistance                        0.061507            1.000000   
Calories                                  0.319383            0.626089   
TotalHoursAsleep                         -0.009130           -0.412389   
WeightKg                                 -0.111639            0.110376   
Fat                                      -0.096760            0.048256   
BMI                                      -0.111952           -0.005833   
MinuteAverage                             0.018225            0.040330   
HourlyAverage                             0.025118            0.052914   

                          Calories  TotalHoursAsleep  WeightKg       Fat  \
Id                        0.093323          0.026280  0.057679  0.007569   
WeekDay                   0.241706         -0.048477 -0.205572 -0.085369   
TotalSteps                0.734070         -0.358232  0.087087  0.016591   
TotalDistance             0.758926         -0.365259  0.109416  0.039814   
TotalActiveMinutes        0.552052         -0.118322  0.010108 -0.066781   
TotalMinutes              0.154519         -0.038048 -0.020313 -0.085203   
TotalActiveHours          0.561747         -0.143315  0.014034 -0.049701   
LightlyActiveMinutes      0.217038          0.003401  0.058420 -0.085336   
FairlyActiveMinutes       0.424528          0.002237 -0.138155 -0.046143   
VeryActiveMinutes         0.759701         -0.326460 -0.038988  0.043161   
LightActiveDistance       0.456871         -0.073927  0.109763  0.048691   
ModeratelyActiveDistance  0.319383         -0.009130 -0.111639 -0.096760   
VeryActiveDistance        0.626089         -0.412389  0.110376  0.048256   
Calories                  1.000000         -0.257674 -0.021311  0.097659   
TotalHoursAsleep         -0.257674          1.000000  0.104904  0.044360   
WeightKg                 -0.021311          0.104904  1.000000  0.145143   
Fat                       0.097659          0.044360  0.145143  1.000000   
BMI                      -0.098498          0.139833  0.625712  0.079198   
MinuteAverage             0.043540          0.015333  0.229023 -0.000047   
HourlyAverage             0.059058          0.008973  0.217775  0.002514   

                               BMI  MinuteAverage  HourlyAverage  
Id                        0.018736       0.075169       0.078994  
WeekDay                  -0.263494       0.062410       0.104490  
TotalSteps               -0.033522       0.048939       0.065706  
TotalDistance            -0.030163       0.046679       0.063358  
TotalActiveMinutes       -0.035674       0.035729       0.045701  
TotalMinutes             -0.113700       0.018493       0.013176  
TotalActiveHours         -0.030905       0.029705       0.039445  
LightlyActiveMinutes      0.011935       0.017145       0.020327  
FairlyActiveMinutes      -0.109810       0.017794       0.024924  
VeryActiveMinutes        -0.067822       0.046858       0.062576  
LightActiveDistance      -0.007126       0.032036       0.045257  
ModeratelyActiveDistance -0.111952       0.018225       0.025118  
VeryActiveDistance       -0.005833       0.040330       0.052914  
Calories                 -0.098498       0.043540       0.059058  
TotalHoursAsleep          0.139833       0.015333       0.008973  
WeightKg                  0.625712       0.229023       0.217775  
Fat                       0.079198      -0.000047       0.002514  
BMI                       1.000000       0.010998      -0.009687  
MinuteAverage             0.010998       1.000000       0.811340  
HourlyAverage            -0.009687       0.811340       1.000000  
/tmp/ipykernel_20/3457317263.py:4: FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
  correlation_matrix = df.corr()
'''
