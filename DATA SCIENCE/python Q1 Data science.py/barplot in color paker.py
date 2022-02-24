#import libary 
import seaborn as sns
import matplotlib.pyplot as plt

#load a file name is : 
sns.set(style="whitegrid3")
bar = sns.load_dataset("tips")
print(bar)

# show barpolt
sns.boxplot(x="tip",y="day",data=bar)
plt.show()

#color was copy in gool  (hex color picker)

sns.boxplot(x="tip",y="day",data=bar,color="#18266e")
plt.show()
print("**************************************************")
print("**************************************************")
print("**************************************************")

#import library 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pt
import numpy as np

a = np.array([1,2,3,4])
b = np.array(["basit","aziz","mosawer","waqar"])
sns.boxplot(x=b,y=a)
plt.show()

sns.set(style = "whitegrid")
box =sns.load_dataset("titanic")
print(box)

sns.boxplot(x="sex",y="age",hue="survived",showmeans=True,meanprops={"marker":"+",
                                                       "markersize":"12",
                                                       "markeredgecolor":"red"},data=box)
plt.xlabel("how many survived",size=15),
plt.ylabel("Age(year)",size=15),
plt.title("Box plot ia titinic",size=15)
plt.show() 