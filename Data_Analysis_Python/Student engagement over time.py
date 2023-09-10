import pandas as pd
import matplotlib.pyplot as plt

engagement = pd.read_csv('365_student_engagement.csv') 
info = pd.read_csv('365_student_info.csv')

df = engagement.merge(info, on='student_id')

df['date_engaged'] = pd.to_datetime(df['date_engaged'])

plt.plot(df.groupby('date_engaged').count()['engagement_id'])
plt.xticks(rotation=45)
plt.xlabel('Date')  
plt.ylabel('Engagement Count')
plt.title('Student Engagement Over Time')
plt.show()