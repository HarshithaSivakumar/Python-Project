### GRADE: X / 45

#Name:Harshitha Sivakumar
#ID:0267414
#Lab Day & Time: Monday 4.00pm

#Enter your acknowledgements below (eg., I received no help from other sources on this lab)
#see the Academic Integrity Module for more information.
#

### ANSWER QUESTIONS HERE

#Q4:There are 12 columns in this data.The columns that represent the categorical data are Username,DayofWeek,Reply,Alignment,Text,
#ProcessedTweet,Tweet Id,Year,Month,Day,Hour
#and the columns that represent numerical data is Sentiment.

#Q5e:Proportion of Left-leaning tweets:0.32,Proportion of Right-leaning tweets:0.67,Proportion of Right-leaning tweets:0.01

#Q6:I feel like there is a slight underestimate in the left-leaning tweets and overestimate in the right-leaning ones.

#Q7b:We are changing the denominator cause we are only filtering the data that has only year 2012.

#Q10b:It can be seen that the proportion of right-leaning tweets increases, the values of the average sentiment decreases.

'''
Year | Proportion R (Q8) | Average Sentiment (Q10a)
---------------------------------------------
2012 |  0.60             |       0.23    
2013 |  0.63             |       0.21    
2014 |  0.65             |       0.20
2015 |  0.62             |       0.23
2016 |  0.62             |       0.20 
2017 |  0.65             |       0.18
2018 |  0.62             |       0.21
2019 |  0.64             |       0.18 
2020 |  0.65             |       0.20
2021 |  0.63             |       0.18
2022 |  0.69             |       0.13
2023 |  0.77             |       0.12
'''

###########################################################

#CODE GOES BELOW
#pandas - used to read and analyse the data in the file
import pandas as pd
#used to do numerical operation in the dataset of a file
import numpy as np

elon_data = pd.read_csv('elonTweets.csv')
print(elon_data)

#blank
pd.set_option('display.max_columns', None)
print(elon_data)

left_tweets = elon_data.loc[elon_data['Alignment']=='L']
print('Proportion of Left-leaning tweets:')
length_L = len(left_tweets)/len(elon_data)
print(round(length_L,2))

#right-leaning tweets:
right_tweets = elon_data.loc[elon_data['Alignment']=='R']
print('Proportion of Right-leaning tweets:')
lenght_R = len(right_tweets)/len(elon_data)
print(round(lenght_R,2))

#Center tweets:
Center_tweets = elon_data.loc[elon_data['Alignment']=='C']
print('Proportion of center-leaning tweets:')
lenght_C = len(Center_tweets)/len(elon_data)
print(round(lenght_C,2))

#2012 alignment R proportion
y2012_data = elon_data.loc[elon_data['Year']==2012]
right_tweets = y2012_data.loc[y2012_data['Alignment']=='R']
print('Proportion of Right-leaning tweets in 2012:')
length_12 = len(right_tweets)/len(y2012_data)
print(round(length_12,2))

#2013 alignment R proportion
y2013_data = elon_data.loc[elon_data['Year']==2013]
right_tweets = y2013_data.loc[y2013_data['Alignment']=='R']
print('Proportion of Right-leaning tweets in 2013:')
length_13 = len(right_tweets)/len(y2013_data)
print(round(length_13,2))

#2014 alignment R proportion
y2014_data = elon_data.loc[elon_data['Year']==2014]
right_tweets = y2014_data.loc[y2014_data['Alignment']=='R']
print('Proportion of Right-leaning tweets in 2014:')
length_14 = len(right_tweets)/len(y2014_data)
print(round(length_14,2))

#2015 alignment R proportion
y2015_data = elon_data.loc[elon_data['Year']==2015]
right_tweets = y2015_data.loc[y2015_data['Alignment']=='R']
print('Proportion of Right-leaning tweets in 2015:')
length_15 = len(right_tweets)/len(y2015_data)
print(round(length_15,2))

#2016 alignment R proportion
y2016_data = elon_data.loc[elon_data['Year']==2016]
right_tweets = y2016_data.loc[y2016_data['Alignment']=='R']
print('Proportion of Right-leaning tweets in 2016:')
length_16 = len(right_tweets)/len(y2016_data)
print(round(length_16,2))

#2017 alignment R proportion
y2017_data = elon_data.loc[elon_data['Year']==2017]
right_tweets = y2017_data.loc[y2017_data['Alignment']=='R']
print('Proportion of Right-leaning tweets in 2017:')
length_17 = len(right_tweets)/len(y2017_data)
print(round(length_17,2))

#2018 alignment R proportion
y2018_data = elon_data.loc[elon_data['Year']==2018]
right_tweets = y2018_data.loc[y2018_data['Alignment']=='R']
print('Proportion of Right-leaning tweets in 2018:')
length_18 = len(right_tweets)/len(y2018_data)
print(round(length_18,2))

#2019 alignment R proportion
y2019_data = elon_data.loc[elon_data['Year']==2019]
right_tweets = y2019_data.loc[y2019_data['Alignment']=='R']
print('Proportion of Right-leaning tweets in 2019:')
length_19 = len(right_tweets)/len(y2019_data)
print(round(length_19,2))

#2020 alignment R proportion
y2020_data = elon_data.loc[elon_data['Year']==2020]
right_tweets = y2020_data.loc[y2020_data['Alignment']=='R']
print('Proportion of Right-leaning tweets in 2020:')
length_20 = len(right_tweets)/len(y2020_data)
print(round(length_20,2))

#2021 alignment R proportion
y2021_data = elon_data.loc[elon_data['Year']==2021]
right_tweets = y2021_data.loc[y2021_data['Alignment']=='R']
print('Proportion of Right-leaning tweets in 2021:')
length_21=len(right_tweets)/len(y2021_data)
print(round(length_21,2))

#2022 alignment R proportion
y2022_data = elon_data.loc[elon_data['Year']==2022]
right_tweets = y2022_data.loc[y2022_data['Alignment']=='R']
print('Proportion of Right-leaning tweets in 2022:')
length_22 =len(right_tweets)/len(y2022_data)
print(round(length_22,2))

#2023 alignment R proportion
y2023_data = elon_data.loc[elon_data['Year']==2023]
right_tweets = y2023_data.loc[y2023_data['Alignment']=='R']
print('Proportion of Right-leaning tweets in 2023:')
length_23 = len(right_tweets)/len(y2023_data)
print(round(length_23,2))


#Average sentiment
avg_sentiment = np.mean(elon_data['Sentiment'])
print("Average Sentiment: ",avg_sentiment)

#Average Sentimnet of 2012
avg_sentiment12 = np.mean(y2012_data['Sentiment'])
print("Average Sentiment of 2012: ",round(avg_sentiment12,2))

#Average Sentimnet of 2013
avg_sentiment13 = np.mean(y2013_data['Sentiment'])
print("Average Sentiment of 2013: ",round(avg_sentiment13,2))

#Average Sentimnet of 2014
avg_sentiment14 = np.mean(y2014_data['Sentiment'])
print("Average Sentiment of 2014: ",round(avg_sentiment14,2))

#Average Sentimnet of 2015
avg_sentiment15 = np.mean(y2015_data['Sentiment'])
print("Average Sentiment of 2015: ",round(avg_sentiment15,2))

#Average Sentimnet of 2016
avg_sentiment16 = np.mean(y2016_data['Sentiment'])
print("Average Sentiment of 2016: ",round(avg_sentiment16,2))

#Average Sentimnet of 2017
avg_sentiment17 = np.mean(y2017_data['Sentiment'])
print("Average Sentiment of 2017: ",round(avg_sentiment17,2))

#Average Sentimnet of 2018
avg_sentiment18 = np.mean(y2018_data['Sentiment'])
print("Average Sentiment of 2018: ",round(avg_sentiment18,2))

#Average Sentimnet of 2019
avg_sentiment19 = np.mean(y2019_data['Sentiment'])
print("Average Sentiment of 2019: ",round(avg_sentiment19,2))

#Average Sentimnet of 2020
avg_sentiment20 = np.mean(y2020_data['Sentiment'])
print("Average Sentiment of 2020: ",round(avg_sentiment20,2))

#Average Sentimnet of 2021
avg_sentiment21 = np.mean(y2021_data['Sentiment'])
print("Average Sentiment of 2021: ",round(avg_sentiment21,2))

#Average Sentimnet of 2022
avg_sentiment22 = np.mean(y2022_data['Sentiment'])
print("Average Sentiment of 2022: ",round(avg_sentiment22,2))

#Average Sentimnet of 2023
avg_sentiment23 = np.mean(y2023_data['Sentiment'])
print("Average Sentiment of 2023: ",round(avg_sentiment23,2))


