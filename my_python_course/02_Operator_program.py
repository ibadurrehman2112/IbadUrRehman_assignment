# defining a function of future

#def future_age(age):
#    new_age=age+20
#    return new_age
#    print(new_age)
#future_predicted_age= future_age(38)
#print(future_predicted_age) 

#x=0
#while (x<=5):
#  print(x)
#  x=x+1

#array 
# days=["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]  
# for d in days:
#    if (d=="Fri"): break
#    print(d)
#Bar plots-------------------
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
titanic = sns.load_dataset("titanic")
print(titanic)
p1=sns.countplot(x='sex', data=titanic, hue='class')
p1.set_title("Plot for counting")
plt.show()
#-------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
titanic = sns.load_dataset("titanic")
print(titanic)
p1=sns.countplot(x='who', data=titanic, hue='alone')
p1.set_title("Plot for counting")
plt.show()
