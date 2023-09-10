import pandas as pd  

engagement = pd.read_csv('365_student_engagement.csv')
info = pd.read_csv('365_student_info.csv')  

df = engagement.merge(info, on='student_id')

print(df.groupby('student_country')[['engagement_quizzes', 'engagement_exams', 'engagement_lessons']].mean())