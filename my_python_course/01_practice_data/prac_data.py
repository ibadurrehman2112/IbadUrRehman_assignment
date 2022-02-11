# import library 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data01 = pd.read_csv("data_set_01.csv")
print(data01)
sns.set_theme(style="ticks", color_codes=True)
p1= sns.countplot(x="Gender", hue="Age", data=data01)
plt.show()