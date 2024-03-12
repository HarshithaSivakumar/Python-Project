# Name:

# GRADE: X / 25

#Name:Harshitha Sivakumar
#ID:0267414
#Lab Day & Time:Monday 4.00pm

#I received help from Dr.Betti and Dr.Allen in rectifying errors that occurred

### ANSWER QUESTIONS HERE

#Q3:The names of the columns are shape,price,carat,cut,color,clarity,currency,Lab
#And their associated datatypes are:
#shape        string
#price        string
#carat       float64
#cut          string
#color        string
#clarity      string
#currency     string
#Lab           boolen
#I think "price" column which is classified as string, can be classified as numbers which can help us to do alot of mathematical operations in it

#Q4e:'CA','$',',' are the non-numeric symbols that appear in the price column along with the numerical values

#Q7:After examining the scatter plot, we can see that the points tend to move upward from left to right,
#it indicates a positive correlation between carats and price.

#Q8e:The scatterplot shows a positive correlation, it means that as diamonds get bigger,
#the price for each carat also goes up. In simple words it can be said that the larger diamonds tend to be more expensive per carat.

#Q8g:For natural diamonds, the price-per-carat tends to increase as the size of the diamond gets larger.
#This is indicated by a positive correlation in the scatterplot, suggesting that larger natural diamonds are generally more expensive per carat.
#In contrast, for lab-grown diamonds, there is no clear correlation between the size of the diamond and the price-per-carat.
#The scatterplot does not show a consistent pattern,
#indicating that the price-per-carat for lab-grown diamonds does not necessarily increase as the diamond size grows.

#Q9:Cushion shaped diamond is the most expensive.And from the information that i gave seen
#The shape alone is not a good indicator of expense for a diamond. Other factors like carat weight,
#cut, color, and clarity collectively determine a diamond's value.

#Q10a:The mode of.,
#-->carat is 1.0
#-->clarity is VS1
#-->color is D
#-->Lab is False

#Q10c:The bar graph depicts the average price of diamond shapes within the filtered dataset.
#Initially, "cushion" was the most expensive shape, but after filtering, "round" emerges as the priciest.
#However, this conclusion may not generalize to all diamonds, as it's specific to the filters.

#Q11:#Based on this data,does the price of the diamonds changes according to the colours of the diamonds or not?

########################

#CODE GOES BELOW
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

ds_data = pd.read_csv('newDiamonds.csv')

print(ds_data.dtypes)
print(ds_data)

ds_data['shape'] = ds_data['shape'].str.lower()
ds_data['price'] = ds_data['price'].str.replace('CA','')
ds_data['price'] = ds_data['price'].str.replace('$','')
ds_data['price'] = ds_data['price'].str.replace(',', '')

ds_data['price'] = pd.to_numeric(ds_data['price'], errors='coerce')

sns.scatterplot(x=ds_data['carat'],y=ds_data['price']).set(title="Carat v Price")
plt.show()

print("After converting the price datatype")
print(ds_data.dtypes)
print(ds_data)

plt.figure()

ds_data['ppc'] = ds_data['price']/ds_data['carat']
sns.scatterplot(x=ds_data['carat'],y=ds_data['ppc']).set(title="Carat vs Price Per Carat")
plt.show()

nat_data = ds_data[ds_data['Lab']==False]
lab_data = ds_data[ds_data['Lab']==True]

plt.figure()
sns.scatterplot(x=nat_data['carat'],y=nat_data['ppc']).set(title="Carat vs Price Per Carat For Natural Diamonds")
plt.show()

plt.figure()
sns.scatterplot(x=lab_data['carat'],y=lab_data['ppc']).set(title="Carat vs Price Per Carat For Lab Diamonds")
plt.show()

plt.figure()
sns.barplot(x=ds_data['shape'],y=ds_data['price']).set(title="Shape vs Price")
plt.show()


list_of_columns = ds_data.columns
for column in list_of_columns:
    the_mode = ds_data[column].mode()
    print("Column: ",column,"Mode: ",the_mode)


modal_data = ds_data.loc[
    (ds_data['Lab'] == False) &
    (ds_data['carat'] == 1.0) &
    (ds_data['clarity'] == 'VS1') &
    (ds_data['color'] == 'D')]

plt.figure()
sns.barplot(x=modal_data['shape'],y=modal_data['price']).set(title="Shape vs Price")
plt.show()

