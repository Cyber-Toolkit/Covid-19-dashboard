import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("covid_19_data.csv",index_col = 1)
ax = df.loc['01/22':'02/22', 'Confirmed'].plot(marker='o', linestyle='-')
ax.set_ylabel('Confirmed Cases')
plt.show()