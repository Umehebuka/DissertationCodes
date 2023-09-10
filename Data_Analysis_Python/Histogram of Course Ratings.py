import pandas as pd 
import matplotlib.pyplot as plt

ratings = pd.read_csv('365_course_ratings.csv')

plt.hist(ratings['course_rating'], bins=5)
plt.title('Distribution of Course Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()