import csv
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("Data/train.csv")


survived = train[train["Survived"] == 1]
died = train[train["Survived"] == 0]
survived["Age"].plot.hist(alpha=0.5,color='red',bins=50)
died["Age"].plot.hist(alpha=0.5,color='green',bins=50)
plt.legend(['Survived','Died'])
plt.show()

