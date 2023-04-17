#This program prints the covariance between open and high prices of gold futures.
#The covariance is calculated using  np.cov
import pandas as pd
import numpy as np
df= pd.read_csv("Gold_Futures_Data.csv")
b1 = [df['open']]
b2 = [df['high']]
cov_mat = np.cov(b1, b2)
print(cov_mat)
