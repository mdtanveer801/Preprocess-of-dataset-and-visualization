import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'E:\Data Science Notes and projects\PDF and Datasets\titanic dataset.csv')
df

df.describe()

del df["Name"]
df.head()

del df["Ticket"]
df.head()

del df["Fare"]
df.head()

del df['Cabin']
df.head()

def getNumber(str):
    if str=="male":
        return 1
    else:
        return 2
df["Gender"]=df["Sex"].apply(getNumber)
df.head()

del df["Sex"]
df.head()

df.isnull().sum()
Means= df[df.Survived==1].Age.mean()
Means

df["age"]=np.where(pd.isnull(df.Age) & df["Survived"]==1  ,Means, df["Age"])
df.head()

df.isnull().sum()

meanN=df[df.Survived==0].Age.mean()
meanN


df.age.fillna(meanN,inplace=True)
df.head()


df.isnull().sum()


del df['Age']
df.head()

survivedQ = df[df.Embarked == 'Q'][df.Survived == 1].shape[0]
survivedC = df[df.Embarked == 'C'][df.Survived == 1].shape[0]
survivedS = df[df.Embarked == 'S'][df.Survived == 1].shape[0]


print(survivedQ)
print(survivedC)
print(survivedS)

survivedQ = df[df.Embarked == 'Q'][df.Survived == 0].shape[0]
survivedC = df[df.Embarked == 'C'][df.Survived == 0].shape[0]
survivedS = df[df.Embarked == 'S'][df.Survived == 0].shape[0]


print(survivedQ)
print(survivedC)
print(survivedS)

df.dropna(inplace=True)
df.head()

df.isnull().sum()

df.rename(columns={'age':'Age'}, inplace=True)
df.head()

df.rename(columns={'Gender':'Sex'}, inplace=True)
df.head()


def getEmb(str):
    if str=="S":
        return 1
    elif str=='Q':
        return 2
    else:
        return 3
    
    
df["Embark"]=df["Embarked"].apply(getEmb)
df.head()

del df['Embarked']
df.rename(columns={'Embark':'Embarked'}, inplace=True)
df.head()

#Drawing a pie chart for number of males and females aboard

from matplotlib import style

males = (df['Sex'] == 1).sum() 
#Summing up all the values of column gender with a 
#condition for male and similary for females
females = (df['Sex'] == 2).sum()
print(males)
print(females)
p = [males, females]
plt.pie(p,    #giving array
       labels = ['Male', 'Female'], #Correspndingly giving labels
       colors = ['green', 'yellow'],   # Corresponding colors
       explode = (0.15, 0),    #How much the gap should me there between the pies
       startangle = 0)  #what start angle should be given
plt.axis('equal') 
plt.show()


MaleS=df[df.Sex==1][df.Survived==1].shape[0]
print(MaleS)
MaleN=df[df.Sex==1][df.Survived==0].shape[0]
print(MaleN)
FemaleS=df[df.Sex==2][df.Survived==1].shape[0]
print(FemaleS)
FemaleN=df[df.Sex==2][df.Survived==0].shape[0]
print(FemaleN)

chart=[MaleS,MaleN,FemaleS,FemaleN]
colors=['lightskyblue','yellowgreen','Yellow','Orange']
labels=["Survived Male","Not Survived Male","Survived Female","Not Survived Female"]
explode=[0,0.05,0,0.1]
plt.pie(chart,labels=labels,colors=colors,explode=explode,startangle=100,counterclock=False,autopct="%.2f%%")
plt.axis("equal")
plt.show()























