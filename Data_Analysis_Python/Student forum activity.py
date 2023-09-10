import pandas as pd

engagement = pd.read_csv('Student Engagement Level-Binary.csv')

print(engagement[engagement['# Forum Posts'] > 0][['Student ID', '# Forum Reads', '# Forum Posts']])