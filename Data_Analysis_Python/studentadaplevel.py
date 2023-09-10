import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('students_adaptability_level_online_education.csv')

# Previous columns
df = df.fillna(-1)
df['Adaptivity Level'] = df['Adaptivity Level'].map({'Moderate': 1, 'Low': 2, 'High': 3})
df['Gender'] = df['Gender'].map({'Boy': 0, 'Girl': 1})
df['Internet Type'] = df ['Internet Type'].map({'Mobile Data': 1, 'Wifi': 2})
df['Network Type']= df ['Network Type'].map ({'4G':1, '3G': 2, 'others': 3}) 

# Extract numeric part from Age 
df['Age'] = df['Age'].str.extract('(\d+)').astype(int)

# Numeric columns
numeric_cols = ['Age', 'Adaptivity Level', 'Gender']

# Correlation matrix 
corr = df[numeric_cols].corr()
plt.matshow(corr)
plt.show()

# ANOVA
f, p = stats.f_oneway(df['Adaptivity Level'], df['Class Duration'])
print("Class Duration p-value:", p)

f, p = stats.f_oneway(df['Adaptivity Level'], df['Gender'])
print("Gender p-value:", p)


