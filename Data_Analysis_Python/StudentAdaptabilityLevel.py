import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('students_adaptability_level_online_education.csv')

df.describe(include=['object'])


