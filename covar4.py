import pandas as pd
import numpy as np
df= pd.read_csv("Gold_Futures_Data.csv")
b1 = [df['open']]
df1= pd.read_csv("Silver_Futures_Data.csv")
b2 = [df1['open']]
cov_mat = np.cov(b1, b2)
print(cov_mat)