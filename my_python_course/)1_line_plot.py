# import libraries
import seaborn as sns 
import matplotlib.pyplot as plt
# load dataset 
phool = sns.load_dataset("iris")
print(phool)
# draw a line plot 
sns.lineplot(x="sepal_length", y= "sepal_width", data=phool)
plt.show()