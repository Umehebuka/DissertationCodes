import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('students_adaptability_level_online_education.csv')

# Previous encodings
df['Gender'] = df['Gender'].map({'Boy': 0, 'Girl': 1})  

# Take average of min and max values
df['Class Duration'] = df['Class Duration'].str.split('-').mean(axis=1)

# Numeric columns
numeric_cols = ['Age', 'Adaptivity Level', 'Gender', 'Class Duration']  

# Correlation and heatmap as before 
corr = df[numeric_cols].corr()

sns.heatmap(corr, 
            xticklabels=corr.columns,
            yticklabels=corr.columns,
            cmap='RdBu_r', 
            annot=True)

plt.show()
