#import libary
from numpy import *
import seaborn as sns
import matplotlib.pyplot as plt
#load dataset
plt.figure(figsize=(8,4))
pool= sns.load_dataset("iris")
print(pool)
# change figure
#draw a line plot
sns.lineplot(x="sepal_length",y="sepal_width",data=pool)
plt.show()

#draw a bar plot
sns.barplot(x="species",y="sepal_width",data=pool)
plt.show()

sns.barplot(x="species",y="petal_width",data=pool)
plt.show()

#draw a titanoc bar plot
tit = sns.load_dataset("titanic")
print(tit)

sns.barplot(x="sex",y="alone",hue="who",data=tit,order=["female","male"],color='brown',
         ci=None,palette="pastel")#ci means confident
plt.show()

sns.barplot(x="class",y="fare",hue="sex",data=tit,estimator=median,saturation=0.2)
plt.show()