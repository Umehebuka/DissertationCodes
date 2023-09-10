import pandas as pd
import matplotlib.pyplot as plt

exams = pd.read_csv('365_student_exams.csv')

plt.hist(exams['exam_result'], bins=20)
plt.title('Distribution of Exam Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()