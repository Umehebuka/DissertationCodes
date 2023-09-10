import pandas as pd
import matplotlib.pyplot as plt

exams = pd.read_csv('365_student_exams.csv')

plt.scatter(exams['exam_completion_time'], exams['exam_result'])
plt.title('Exam Result vs Duration Scatterplot')
plt.xlabel('Duration')
plt.ylabel('Result')
plt.show()