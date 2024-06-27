import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Wine Quality Dataset.csv")
print(data.head())
print(data.shape)
print(data.index)
print(data.columns)
print(data.info())

#View the distributions of the various features in the dataset and calcuate their tendencies

#We will look now into the various features of the dataset
#we will also calculate appropriate measures for the central tendencies

#Creating a histogram of fixed acidity feature
plt.figure(figsize=(11,6))
# sns.histplot(data=data,x="fixed acidity",color='orange',edgecolor='linen',alpha=.5,bins=5)
plt.title("Histogram of Fixed Acidity")
plt.xlabel("Fixed Acidity")
plt.ylabel("Count")
# # plt.show()
# #OBSERVATIONS-1)We can see from the graph that the histogram is normally distributed,2)The count is maximum between 6 to 8.
#
# #Mean of fixed acidity
print(round(data['fixed acidity'].mean(),2))
# # #Median of fixed acidity
print(round(data['fixed acidity'].median(),2))
#
# #Creating a histogram of fixed acidity feature with mean & median
plt.figure(figsize=(11,6))
sns.histplot(data=data,x="fixed acidity",color='orange',edgecolor='linen',alpha=.5,bins=5)
plt.title("Histogram of Fixed Acidity")
plt.xlabel("Fixed Acidity")
plt.ylabel("Count")
# plt.show()
plt.vlines(data['fixed acidity'].mean(),ymin=0,ymax=4000,colors='blue',label='mean')
plt.vlines(data['fixed acidity'].median(),ymin=0,ymax=4000,colors='red',label='median')
plt.legend()
# plt.show()
# #OBSERVATIONS-1)mean & median are very close to each other,2)We can chose either of them as the measurement of central tendency
#
# #Creating a histogram of volatile acidity feature
plt.figure(figsize=(11,6))
sns.histplot(data=data,x="volatile acidity",color='green',edgecolor='linen',alpha=.5,bins=5)
plt.title("Histogram of Volatile Acidity")
plt.xlabel("Volatile Acidity")
plt.ylabel("Density")
# plt.show()
# #OBSERVATIONS-We observe that the histogram is not well distributed,it is right or positively skewed,
# # As we have seen the skewness now we have to distplot function to see the distribution.
#
# #Creating a distplot of volatile acidity feature
plt.figure(figsize=(11,6))
sns.distplot(data['volatile acidity'],color='blue')
plt.title("Distplot of Volatile Acidity")
plt.xlabel("Volatile Acidity")
plt.ylabel("Density")
# plt.show()
# #OBSERVATION-This plot shows the normal distribution,The normal distribution is showed by the mean & sd,
# #The normal distribution is often called as 'Bell Curve' because of its shape
# #mean & median are equal,It has only one mode ,It is symmetric,means it decreases the same amount on the left and the right of the center
#
# #Calculatong Skewness
print(data['volatile acidity'].skew())
# #OBSERVATION-As we can see the value is greater than 1,hence it is positively skewed
# #Mean of volatile acidity
print(round(data['volatile acidity'].mean(),2))
# #Median of volatile acidity
print(round(data['volatile acidity'].median(),2))
#Creating a histogram of volatile acidity feature with mean & median
plt.figure(figsize=(11,6))
sns.histplot(data=data,x="volatile acidity",color='green',edgecolor='linen',alpha=.5,bins=5)
plt.title("Histogram of Volatile Acidity")
plt.xlabel("Volatile Acidity")
plt.ylabel("Count")
# plt.show()
plt.vlines(data['volatile acidity'].mean(),ymin=0,ymax=4000,colors='blue',label='mean')
plt.vlines(data['volatile acidity'].median(),ymin=0,ymax=4000,colors='red',label='median')
plt.legend()
# plt.show()
# #OBSERVATIONS-1)mean & median are very close to each other,2)We can chose either of them as the measurement of central tendency
#
# #Creating a histogram of citric acid feature
plt.figure(figsize=(11,6))
# sns.histplot(data=data,x="citric acid",color='red',edgecolor='linen',alpha=.5,bins=5)
plt.title("Histogram of Citric Acid")
plt.xlabel("Citric Acid")
plt.ylabel("Count")
# # plt.show()
# #OBSERVATIONS-We observe that the histogram is not well distributed,it is right or positively skewed
#
# #Mean of citric acid
# print(round(data['citric acid'].mean(),2))
# # #Median of citric acid
print(round(data['citric acid'].median(),2))
#
# #Creating a histogram of citric acid feature with mean & median
plt.figure(figsize=(11,6))
# sns.histplot(data=data,x="citric acid",color='red',edgecolor='linen',alpha=.5,bins=5)
plt.title("Histogram of Citric Acid")
plt.xlabel("Citric Acid")
plt.ylabel("Count")
# plt.show()
plt.vlines(data['citric acid'].mean(),ymin=0,ymax=4000,colors='blue',label='mean')
plt.vlines(data['citric acid'].median(),ymin=0,ymax=4000,colors='red',label='median')
plt.legend()
# # plt.show()
# #OBSERVATIONS-1)mean & median are very close to each other,2)We can chose either of them as the measurement of central tendency
#
# #Creating a distplot of citric acid feature
plt.figure(figsize=(11,6))
# sns.distplot(data['citric acid'],color='blue')
# plt.title("Distplot of Citric Acid")
plt.xlabel("Citric Acid")
plt.ylabel("Count")
# plt.show()

#Creating a countplot of quality feature
plt.figure(figsize=(11, 6))
sns.countplot(x='quality', data=data)
plt.title("Countplot of Quality")
plt.xlabel("Quality")
plt.ylabel("Count")
plt.show()
# print(data['quality'].value_counts())
# print(data['quality'].value_counts().index[0])

rep_acid=pd.Series(index=['fixed acidity','volatile acidity','citric acid','quality'],
            data=[data['fixed acidity'].mean(),data['volatile acidity'].mean(),data['citric acid'].mean(),data['quality'].value_counts().index[0]])
# print (rep_acid)