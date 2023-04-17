#pip3 install seaborn
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Gold_Futures_Plot_Data')

plt.figure(figsize=(40,40)) 
# play with the figsize until the plot is big enough to plot all the columns
# of your dataset, or the way you desire it to look like otherwise

sns.heatmap(data.corr())
plt.show()
#Following is the interpretation of the heatmap.
'''
price to price is highly correlated(white color at the peak value of '1'.
price to open is the lowest correlation('Black color at the bottom')
.....
'''.0