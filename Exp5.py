# Write a python program to import and export data using Pandas and 
# show the details of the dataset like number of rows, columns, first five 
# rows, size, number of missing values, sum, average, min and max 
# values from the numerical columns.

import pandas as pd

# Import data from a CSV file
df = pd.read_csv('student-scores.csv')

# Display dataset details
print("Number of rows:", df.shape[0])
# output :- Number of rows: 2000

print("Number of columns:", df.shape[1])
# output :- Number of columns: 17

# printing 5 rows 
print("\nFirst five rows:\n", df.head())
#Output :- First five rows:
#    id first_name last_name                                  email  gender  part_time_job  ...  history_score  physics_score  chemistry_score biology_score  english_score  geography_score
#0   1       Paul     Casey         paul.casey.1@gslingacademy.com    male          False  ...             81             93               97            63             80               87
#1   2   Danielle  Sandoval  danielle.sandoval.2@gslingacademy.com  female          False  ...             86             96              100            90             88               90
#2   3       Tina   Andrews       tina.andrews.3@gslingacademy.com  female          False  ...             97             95               96            65             77               94
#3   4       Tara     Clark         tara.clark.4@gslingacademy.com  female          False  ...             74             88               80            89             63               86
#4   5    Anthony    Campos     anthony.campos.5@gslingacademy.com    male          False  ...             77             65               65            80             74               76

#[5 rows x 17 columns]


print("\nSize of the dataset:", df.size)
# Output :- Size of the dataset: 34000
print("\nNumber of missing values:\n", df.isnull().sum())
# Output :- Number of missing values:
#  id                            0
# first_name                    0
# last_name                     0
# email                         0
# gender                        0
# part_time_job                 0
# absence_days                  0
# extracurricular_activities    0
# weekly_self_study_hours       0
# career_aspiration             0
# math_score                    0
# history_score                 0
# physics_score                 0
# chemistry_score               0
# biology_score                 0
# english_score                 0
# geography_score               0
# dtype: int64


# Display summary statistics for numerical columns
print("\nSum of numerical columns:\n", df.sum(numeric_only=True))
# Output :-Sum of numerical columns:
#  id                            2001000
# part_time_job                     316
# absence_days                     7331
# extracurricular_activities        408
# weekly_self_study_hours         35511
# math_score                     166904
# history_score                  160664
# physics_score                  162673
# chemistry_score                159990
# biology_score                  159163
# english_score                  162555
# geography_score                161776
# dtype: int64

print("\nAverage of numerical columns:\n", df.mean(numeric_only=True))
# Output :- Average of numerical columns:
#  id                            1000.5000
# part_time_job                    0.1580
# absence_days                     3.6655
# extracurricular_activities       0.2040
# weekly_self_study_hours         17.7555
# math_score                      83.4520
# history_score                   80.3320
# physics_score                   81.3365
# chemistry_score                 79.9950
# biology_score                   79.5815
# english_score                   81.2775
# geography_score                 80.8880
# dtype: float64

print("\nMinimum values of numerical columns:\n", df.min(numeric_only=True))
# Output :- Minimum values of numerical columns:
#  id                                1
# part_time_job                 False
# absence_days                      0
# extracurricular_activities    False
# weekly_self_study_hours           0
# math_score                       40
# history_score                    50
# physics_score                    50
# chemistry_score                  50
# biology_score                    30
# english_score                    50
# geography_score                  60
# dtype: object

print("\nMaximum values of numerical columns:\n", df.max(numeric_only=True))
# Output :- Maximum values of numerical columns:
#  id                            2000
# part_time_job                 True
# absence_days                    10
# extracurricular_activities    True
# weekly_self_study_hours         50
# math_score                     100
# history_score                  100
# physics_score                  100
# chemistry_score                100
# biology_score                  100
# english_score                   99
# geography_score                100
# dtype: object


print(df.info())
# Output :- <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2000 entries, 0 to 1999
# Data columns (total 17 columns):
#  #   Column                      Non-Null Count  Dtype
# ---  ------                      --------------  -----
#  0   id                          2000 non-null   int64
#  1   first_name                  2000 non-null   object
#  2   last_name                   2000 non-null   object
#  3   email                       2000 non-null   object
#  4   gender                      2000 non-null   object
#  5   part_time_job               2000 non-null   bool
#  6   absence_days                2000 non-null   int64
#  7   extracurricular_activities  2000 non-null   bool
#  8   weekly_self_study_hours     2000 non-null   int64
#  9   career_aspiration           2000 non-null   object
#  10  math_score                  2000 non-null   int64
#  11  history_score               2000 non-null   int64
#  12  physics_score               2000 non-null   int64
#  13  chemistry_score             2000 non-null   int64
#  14  biology_score               2000 non-null   int64
#  15  english_score               2000 non-null   int64
#  16  geography_score             2000 non-null   int64
# dtypes: bool(2), int64(10), object(5)
# memory usage: 238.4+ KB
# None

# Export data to a new CSV file
df.to_csv('output.csv', index=False)
