#steps involved in Data visualitaiion
#step-1 import libaries
import seaborn as sns 
import matplotlib.pyplot as plt
#step-2 set a theme
sns.set_theme(style="ticks",color_codes=True)
titanic= sns.load_dataset("titanic")
#print(titanic) # this is print in data vivo 
p1= sns.countplot(x = 'who',data=titanic,hue='alone')  
p1.set_title("ploat for couting")
plt.show()
#step-3 import data set you can also import your own data
info = sns.load_dataset('titanic')
#step-4 plot basic graph with 1 variable (count)
p = sns.countplot(x='sex',data=titanic)
plt.show() 

#step-5 plot basic graph with 2 variable (count plot)
s = sns.countplot(x='sex',data=titanic,hue='class')
s.set_title("uze tech information")
plt.show()