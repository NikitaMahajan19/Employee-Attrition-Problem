import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('HR_comma_sep')
print df.head()
print df.tail()
print df.info()
left = df.groupby('left')
print left.mean()
print df.describe()
left_count=df.groupby('left').count()
plt.bar(left_count.index.values, left_count['satisfaction_level'])
plt.xlabel('Employees Left Company')
plt.ylabel('Number of Employees')
plt.savefig('employees left')
plt.show()
print df.left.value_counts()

num_projects=df.groupby('number_project').count()
plt.bar(num_projects.index.values, num_projects['satisfaction_level'])
plt.xlabel('Number of Projects')
plt.ylabel('Number of Employees')
plt.savefig('number of projects')
plt.show()

time_spent=df.groupby('time_spend_company').count()
plt.bar(time_spent.index.values, time_spent['satisfaction_level'])
plt.xlabel('Number of Years Spend in Company')
plt.ylabel('Number of Employees')
plt.savefig('number of years')
plt.show()

num_bins = 10
df.hist(bins=num_bins, figsize=(20,15))
plt.savefig('hr')
plt.show()

