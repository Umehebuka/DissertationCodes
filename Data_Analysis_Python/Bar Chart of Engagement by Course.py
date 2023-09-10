import pandas as pd
import matplotlib.pyplot as plt

engagement = pd.read_csv('365_student_engagement.csv')
courses = pd.read_csv('365_course_info.csv')
student_courses = pd.read_csv('365_student_learning.csv')


df = engagement.merge(student_courses, on='student_id').merge(courses, on='course_id')

df.groupby('course_title')[['engagement_quizzes', 'engagement_exams']].sum().plot(kind='bar')
plt.title('Engagement by Course')
plt.ylabel('Engagement Count')
plt.show()