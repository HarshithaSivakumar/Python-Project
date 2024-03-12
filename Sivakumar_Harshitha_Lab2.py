### GRADE: X / 15

#Name:Harshitha Sivakumar
#ID:0267414
#Lab Day & Time:Monday 4.00pm

#Enter your acknowledgements below (eg., I received no help from other sources on this lab)

### ANSWER QUESTIONS HERE

#Q3d:There are 12 colums in the datafile.The columns are work_year,job_title,job_category,salary_currency,salary,salary_in_usd,employee_residencec
#experience_level,employment_type,work_setting,company_location,company_size

#Q4:
#The data is from some countries, not all 193 countries in world
#The info is only from 2020 to 2023 not for all the years
#The printed data is the subset of the entire population(all countries in the world and all years in the history)

#Q6:I would go for the salary_in_usd since it is already converted to a common currency making it easier to compare salaries between countries directly

#Q8:It means the number of times that particular country has occured in the dataset.This count provides information
#on how frequently each country appears in the dataset.

#Q9:I would choose the Arithmetic average (c_mean) for comparing salaries in different countries because
#it gives a balance by adding up all salaries and dividing by the number of data points as the values are independent to each other

#Q10:As the sample size of the dataset is small for nations such as China, Saudi Arabia, Algeria, New Zealand, or others, examining means and standard deviations might not be accurate.

#Q11:When the arithmetic mean is greater than the median, it indicates that the distribution of salaries in that country is right-skewed

#Q13:The most occured year is 2023 ,it occurs 7453 and it's appropriate mean is 155132.59170803704  and median is 147100.0

###########################################################

#CODE GOES BELOW
import pandas as pd
import numpy as np
import scipy .stats as stats

ds_data = pd.read_csv('jobs_in_data.csv')
pd.set_option('display.max_columns', None)
print(ds_data)

years_covered = set(ds_data['work_year'])
countries_covered = set(ds_data['company_location'])
print(years_covered)
print(countries_covered)

for country in countries_covered:
    country_data = ds_data.loc[ds_data['company_location'] == country]  
    country_mean = np.mean(country_data['salary_in_usd'])
    country_gmean = stats.gmean(country_data['salary_in_usd'])
    country_hmean = stats.hmean(country_data['salary_in_usd'])
    country_median = np.median(country_data['salary_in_usd'])
    country_std = np.std(country_data['salary_in_usd'])
    print("Country:",country," Count:",len(country_data)," Arthimetic Mean:",country_mean," Geomentric Mean:",country_gmean," Harmonic Mean:",country_hmean," Median:",country_median," Standarard Deviation:",country_std)


for year in years_covered:
    year_data = ds_data.loc[ds_data['work_year'] == year]
    entries = len(year_data)
    mean_salary = np.mean(year_data['salary_in_usd'])
    median_salary = np.median(year_data['salary_in_usd'])
    print("YEAR:",year," COUNT:",entries," MEAN:",mean_salary," MEDIAN:",median_salary)



    

