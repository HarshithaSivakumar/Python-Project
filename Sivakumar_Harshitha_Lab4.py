# Name:

# GRADE: X / 20

#Name:Harshitha Sivakumar
#ID:0267414
#Lab Day & Time:Monday 4.00pm

#Enter your acknowledgements below(I received no help from other sources on this lab)
#

### ANSWER QUESTIONS HERE

#Q4a:Figure 7 does not fully represent the education levels in the dataset ('IndigenousSalaryReduced.csv').
#It includes specific categories, but the dataset contains additional education levels not covered by Figure 7.
#Therefore, Figure 7 may not be fully truthful with the data.

#Q5f:In general, both indigenous and non-indigenous mean values surpass their respective median values. Specifically, the mean value for non-indigenous
#individuals exhibits a more increase compared to that for indigenous individuals. The higher mean than median typically indicates
#a presence of significant outliers elevating the mean. Given the larger population of non-indigenous people compared to indigenous people, it can be
#inferred that the non-indigenous dataset contains more outliers.
#Lau may have opted for the median to avoid the confusion arising from the substantial gap between the increments in mean values for the two groups.

#Q6a:Without filtering education levels, Indigenous individuals appear to fare well compared to non-Indigenous counterparts in both median and mean earnings.
#The broader education categories suggest competitive earnings, challenging Lau's specific Figure 7 categories.

#Q6b:
#plt.figure()
#sns.barplot(x=salary_data['Highest education level'], y=salary_data['Mean'], hue=salary_data['Identity'])
#plt.title('Mean Salary by Education Level and Identity (Unfiltered)')
#plt.xticks(rotation=45)
#plt.subplots_adjust(bottom=0.3)
#plt.show()

#Q7e:the median after-tax income for Indigenous Canadians aged 25 to 64 is $39,200.


#Q7g:The true percent difference between salaries for Indigenous and Non-Indigenous people aged 25 to 64 is 10.9%.

#Q7i:Lau states the percentages of income gaps for First Nations people (11.2%) and the Métis population (2.7%)
#without providing evidence or justification for these figures.

#Q7k:Percent difference for Métis: 2.7 (Same as Lau's claim)
#Percent difference for First Nations: 16.4 (Different from Lau's claim)
#The percent difference for Métis matches Lau's claim, but the percent difference for First Nations is different from Lau's stated value.

#Q7l:The bar plot summarizes median after-tax income by age and identity.
#It provides a visual representation of income disparities across different age groups and between various identity categories.
#This allows for a quick comparison of median after-tax income levels, revealing potential patterns or variations in earnings based on age and identity.

#Q8:According to the STATCAN Figure,only the South Asian individuals have
#slightly higher earnings than the white population compared to other categories.
#Consequently, Lau's argument does not hold up when considering socioeconomic and employment characteristics.

#Q10:How does the median after-tax income for Indigenous Canadians compare to non-Indigenous Canadians,
#and is there a notable difference between various age groups?

#########################

#CODE GOES BELOW

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 3: Read in the CSV file
salary_data = pd.read_csv('IndigenousSalaryReduced.csv')
pd.set_option('display.max_columns',None)
print(salary_data)
print(set(salary_data['Highest education level']))
print('-----------------')

# Step 5: Filter data and reproduce Lau's plot with Median
lau_categories = ['Below High School', 'High School Diploma', 'Postsecondary Below Bachelor',
                  "Bachelor's degree", 'Univ. Cert/Diploma Above Bach.', 'Medical Degree',
                  "Master's degree", 'Earned Doctorate']

filtered_data = salary_data.loc[salary_data['Highest education level'].isin(lau_categories)]

#Create barplot for Median
plt.figure()
sns.barplot(x=filtered_data['Highest education level'], y=filtered_data['Median'], hue=filtered_data['Identity'])
plt.title('Median Salary by Education Level and Identity')
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.3)
plt.show()

#Reproduce Lau's plot with Mean
plt.figure()
sns.barplot(x=filtered_data['Highest education level'], y=filtered_data['Mean'], hue=filtered_data['Identity'])
plt.title('Mean Salary by Education Level and Identity')
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.3)
plt.show()

#Reproduce plots for Median and Mean without filtering education levels
plt.figure()
sns.barplot(x=salary_data['Highest education level'], y=salary_data['Median'], hue=salary_data['Identity'])
plt.title('Median Salary by Education Level and Identity (Unfiltered)')
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.3)
plt.show()

plt.figure()
sns.barplot(x=salary_data['Highest education level'], y=salary_data['Mean'], hue=salary_data['Identity'])
plt.title('Mean Salary by Education Level and Identity (Unfiltered)')
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.3)
plt.show()


data = pd.read_csv('IndigenousSalaryAge.csv')
print(data)
data2020 = data.loc[data['Year'] == 2020]
print(data2020)

# median after-tax income for Indigenous Canadians aged 25 to 64
avg_salary_ind = data2020.loc[(data2020['Age']=='25 to 64 years') &
                               (data2020['Identity'] == 'Indigenous')&
                            (data2020['Highest education level']=='Total - Highest certificate, diploma or degree')]['MedianAfterTax'].values
print('Average after-tax income for Indigenous Canadians aged 25 to 64',avg_salary_ind)

#Find the median after-tax income for Non-Indigenous Canadians aged 25 to 64
avg_salary_non_ind = data2020.loc[(data2020['Age']=='25 to 64 years') &
                                     (data2020['Identity'] == 'Non-Indigenous')&
                                     (data2020['Highest education level']=='Total - Highest certificate, diploma or degree')]['MedianAfterTax'].values
print('Average after-tax income for Non-Indigenous Canadians aged 25 to 64',avg_salary_non_ind)

#Calculate the true percent difference between salaries for Indigenous and Non-Indigenous people
p_diff_ind = ((avg_salary_non_ind - avg_salary_ind) / avg_salary_non_ind) * 100
print('True percent difference between salaries',round(p_diff_ind[0],1))


#Compute the percent difference between the average salary for Métis individuals
avg_salary_metis = data2020.loc[(data2020['Age']=='25 to 64 years') &
                                        (data2020['Identity'] == 'Metis')&
                                        (data2020['Highest education level']=='Total - Highest certificate, diploma or degree')]['MedianAfterTax'].values
p_diff_metis = ((avg_salary_non_ind - avg_salary_metis) / avg_salary_non_ind) * 100

avg_salary_first_nations = data2020.loc[(data2020['Age']=='25 to 64 years') &
                                        (data2020['Identity'] == 'First Nations')&
                                        (data2020['Highest education level']=='Total - Highest certificate, diploma or degree')]['MedianAfterTax'].values

p_diff_first_nations = ((avg_salary_non_ind - avg_salary_first_nations) / avg_salary_non_ind) * 100

print("Percent difference for Metis ",round(p_diff_metis[0],1))
print("Percent difference for First Nations ",round(p_diff_first_nations[0],1))

#We can summarize all this information...
plt.figure()
sns.barplot(x=data2020['Age'], y=data2020['MedianAfterTax'], hue=data2020['Identity'])
plt.title('Median After-Tax Income by Age and Identity')
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.3)
plt.show()






