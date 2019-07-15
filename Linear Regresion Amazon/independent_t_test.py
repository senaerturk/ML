# Define IAM role
from sagemaker import get_execution_role
role = get_execution_role()


bucket='word.dataset.ttest'
data_key = 't_test_data_set.csv'
data_location = 's3://{}/{}'.format(bucket, data_key)

import pandas
from scipy import stats
from math import sqrt
from scipy.stats import t

data = pandas.read_csv(data_location)
  
# to run t test define groups as Noun and Verb   
ind_t_test = stats.ttest_ind(data.duration[data.category == 'Noun'],data.duration[data.category == 'Verb'])

print('The results of the independent t-test are: \n\tt-value = {:4.3f}\n\tp-value = {:4.3f}'.format(ind_t_test[0],ind_t_test[1]))

# Calculate the mean difference and 95% confidence interval
N1 = 30
N2 = 30
df = (N1 + N2 - 2)
std1 = data.duration[data.category == 'Noun'].std()
std2 = data.duration[data.category == 'Verb'].std()
std_N1N2 = sqrt( ((N1 - 1)*(std1)**2 + (N2 - 1)*(std2)**2) / df) 

diff_mean = data.duration[data.category == 'Noun'].mean() - data.duration[data.category == 'Verb'].mean()
MoE = t.ppf(0.975, df) * std_N1N2 * sqrt(1/N1 + 1/N2)
print ('\nThe difference between groups is {:3.1f} [{:3.1f} to {:3.1f}] (mean [95% CI])'.format(diff_mean, 
                                                                         diff_mean - MoE, diff_mean + MoE))