#This program prints the covariance between open and high prices of gold futures.
#The covariance is calculated using the formulae
import pandas as pd
import numpy as np
df= pd.read_csv("Gold_Futures_Data.csv")
b1 = df['open']
b1 = list(b1)
b2 = df['high']
N = df.shape[0]
b2 = list(b2)
#print(b1)
#print(b2)
X = np.column_stack([b1, b2])
#print(X.mean(axis=0))
X -= X.mean(axis=0)
#print(X)
fact = N - 1 
by_hand_cov = np.dot(X.T, X.conj()) / fact
print(by_hand_cov)
