import pandas as pd
from scipy.stats import mannwhitneyu

df = pd.read_csv('Student Engagement Level-Binary.csv')
df = df.drop(['Student ID'], axis=1)

# Recreate numeric engagement column
# This tests if there is a significant difference in assignment 1 lateness between the high and low engagement groups.
df['Engagement Numeric'] = df['Engagement Level'].map({'H': 1, 'L': 0})


high_eng = df[df['Engagement Numeric'] == 1]
low_eng = df[df['Engagement Numeric'] == 0]

p = mannwhitneyu(high_eng['Assignment 1 lateness indicator'], low_eng['Assignment 1 lateness indicator']).pvalue

print("P-value:", p)

#Predict Engagement Level from Metrics
# This trains a random forest model to predict engagement level from the metrics.
from sklearn.ensemble import RandomForestClassifier

X = df[['# Logins', '# Content Reads', '# Forum Reads']]
y = df['Engagement Numeric']

model = RandomForestClassifier()
model.fit(X, y) 

print("Accuracy:", model.score(X, y))

# Cluster Students by Engagement Patterns
# This performs k-means clustering to group students into 2 clusters based on their engagement patterns.
from sklearn.cluster import KMeans

X = df[['# Logins', '# Content Reads', '# Forum Reads']]

kmeans = KMeans(n_clusters=2).fit(X)
print(kmeans.labels_)