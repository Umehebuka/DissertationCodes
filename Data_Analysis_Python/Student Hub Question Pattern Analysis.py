import pandas as pd  
import matplotlib.pyplot as plt

questions = pd.read_csv('365_student_hub_questions.csv')

questions['date_question_asked'] = pd.to_datetime(questions['date_question_asked'])
questions.set_index('date_question_asked').resample('W').count()['student_id'].plot()

plt.title('Weekly Student Questions')
plt.ylabel('Number of Questions')
plt.show()