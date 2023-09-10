import pandas as pd

learning = pd.read_csv('365_student_learning.csv') 
courses = pd.read_csv('365_course_info.csv')

df = learning.merge(courses, on='course_id')

print(df.groupby('student_id')['course_title'].value_counts())