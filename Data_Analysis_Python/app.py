import pandas as pd

# Load the CSV into a Pandas DataFrame
df = pd.read_csv('Student Engagement Level-Binary.csv')

# Create a new column for engagement level as a numeric value 
df['Engagement Numeric'] = df['Engagement Level'].map({'H': 1, 'L': 0})

# Calculate summary statistics 
print(df['Engagement Numeric'].describe())

# Group by engagement level and calculate average assignment duration
print(df.groupby('Engagement Level')['Average time to submit assignment (in hours)'].mean())

# Plot a histogram of assignment duration by engagement level
df.hist('Average time to submit assignment (in hours)', by='Engagement Level', bins=20)