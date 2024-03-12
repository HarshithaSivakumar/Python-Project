# Name:

# GRADE: X / 15

#Name:Harshitha Sivakumar
#ID:0267414
#Lab Day & Time: Monday 4.00pm

#Enter your acknowledgements below (eg., I received help from the help centre
#see the Academic Integrity Module for more information.
#

### ANSWER QUESTIONS HERE

#2:The Simpson Diversity Index is better suited for our data since it only considers names given to at least 5 babies in a year.
#This means rare names won't impact the index. In contrast, the Shannon Diversity Index assumes all names are sampled, which isn't the case in our data.
#The Simpson index indicates the probability that randomly chosen babies share the same name.

#9:new_data.to_csv('babynamefilewithproportioncolumn.csv')

#10:Commented below

#11:The Simpson Diversity Index is different because it measures the probability (λ) of randomly choosing two babies with the same name.
#A higher λ means a greater chance of two individuals sharing a name, indicating lower diversity. If λ is 1,
#everyone has the same name; if it's 0, no one shares a name. In this context, lower values signify higher diversity,
#contrary to the Shannon Diversity Index.

#12:Yes, based on the graphs, Shannon Diversity Index shows an increasing trend over time,
#indicating growing name variety. Simultaneously, the Simpson Diversity Index decreases,
#suggesting a higher concentration of specific names in the dataset.

#13: Leslie used to be mostly a name given to boys from 1880 to 1940. However, around 1940,
#there was a significant increase in the number of girls named Leslie, and by then, the proportion of girls with that name became almost twice that of boys.
#On the other hand, the number of boys named Leslie started decreasing steadily from around 1940 and by 2020,
#it was close to zero. In summary, Leslie shifted from being a predominantly male name before 1940 to becoming mostly a female name afterward. 

#14:To identify names with gender-switching trends similar to Leslie, analyze the dataset by calculating gender variation metrics,
#set thresholds for significant shifts, and filter names accordingly. Visual
#inspection of a subset and summary statistics can then reveal names exhibiting comparable gender association changes
#without individually plotting every name.

#15:Analyzing the USDemoData.csv dataset shows a rising trend in the proportion of live births included in the baby_names dataset over time.
#This doesn't necessarily contradict diversity findings;
#it suggests an expanding dataset coverage without directly indicating a decrease in name diversity.

#########################

#CODE GOES BELOW
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt

newData = pd.read_csv('baby_names.csv')
pd.set_option('display.max_columns', None)
print(newData)

years = set(newData['Year'])
genders = set(newData['Gender'])
new_column = pd.Series(name='Proportion')

for year in years:
    for gender in genders:
        filtered_data = newData[(newData['Year'] == year) & (newData['Gender'] == gender)]
        total = np.sum(filtered_data['Count'])
        new_column = pd.concat([new_column, filtered_data['Count'] / total])                                                                               
               
newData['Proportion'] = new_column
filtered_data_meghan_1980 = newData[(newData['Name'] == 'Meghan') & (newData['Year'] == 1980)]
print(filtered_data_meghan_1980)


diversity = []

for year in years:
    for gender in genders:
        filtered_data = newData[(newData['Year'] == year) & (newData['Gender'] == gender)]
        proportion = filtered_data['Proportion']
        shannon = -np.sum(proportion*np.log(proportion))
        simpson = np.sum(proportion**2)
        diversity.append([year,gender,shannon,simpson])
diversity.append([year,gender,shannon,simpson])
print(diversity)

diversity_data = pd.DataFrame(diversity, columns=['Year', 'Gender', 'Shannon', 'Simpson'])
diversity_data.to_csv('diversity_of_baby_names.csv')
newData.to_csv('data_of_baby_names.csv')

#Question 10:
#sns.lineplot(x=diversity_data['Year'], y=diversity_data['Shannon'], hue=diversity_data['Gender']).set(title = 'Year vs Shannon')
#plt.savefig('Sivakumar_Harshitha_Shannon_Index.png', dpi=300, bbox_inches='tight')
#plt.show()
#plt.figure()
#sns.lineplot(x=diversity_data['Year'], y=diversity_data['Simpson'], hue=diversity_data['Gender']).set(title = 'Year vs Simpson')
#plt.savefig('Sivakumar_Harshitha_Simpson_Index.png', dpi=300, bbox_inches='tight')
#plt.show()

#leslie_data = newData.loc[(newData["Name"] == "Leslie")]
#plt.figure()
#sns.lineplot(x=leslie_data['Year'], y=leslie_data['Shannon'], hue=leslie_data['Gender']).set(title='Year vs Proportion for Leslie')
#plt.show()


us_data = pd.read_csv('USDemoData.csv')
sns.lineplot(x=us_data['Year'], y=us_data['Proportion']).set(title = 'Year vs Proportion of US baby data')
plt.show()

