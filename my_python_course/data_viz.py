# step 1import libaries
import seaborn as sns 
import matplotlib.pyplot as plt
# step 2 set a theme
sns.set_theme(style="ticks", color_codes=True)
#step 3 import data set
kashti = sns.load_dataset("titanic")
#print(kashti)

# step 4 count plot basic graph with 1 variable #count plot has no y axis
# p = sns.countplot(x= "sex", data= kashti)
# plt.show()

# # step 5 count plot basic graph with 2 variable 
# p = sns.countplot(x= "sex", data= kashti, hue="class")
# plt.show()

# step 6 count plot basic graph with 2 variable with title
p = sns.countplot(x= "sex", data= kashti, hue="class")
p.set_title("Count Plot for Titanic")
plt.show()
