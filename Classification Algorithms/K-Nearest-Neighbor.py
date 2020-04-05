#K-Nearest Neighbor

#importing libraries
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

#importing the datasets
data=pd.read_csv("Social_Network_Ads.csv")
x=data.iloc[:,2:-1].values
y=data.iloc[:,-1].values

#splitting the data into Training and Testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)

#Fitting Classifier to Dataset
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier()
classifier.fit(x_train,y_train)

#Predicting the Test Data using Train data
y_pred=classifier.predict(x_test)

#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

#Visualizing the Training set results
from matplotlib.colors import ListedColormap
x_set,y_set=x_train,y_train
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min() - 1,stop=x_set[:,0].max() + 1,step=0.01),
                   np.arange(start=x_set[:,1].min() - 1,stop=x_set[:,1].max() + 1,step=0.01))
plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
              alpha=0.75,cmap=ListedColormap(("red","green")))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
     plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
                 c=ListedColormap(("red","green"))(i),label=j)
plt.title("K-NN(Training Set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()

#Visualizing the Test set results
from matplotlib.colors import ListedColormap
x_set,y_set=x_test,y_test
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min() - 1,stop=x_set[:,0].max() + 1,step=0.01),
                   np.arange(start=x_set[:,1].min() - 1,stop=x_set[:,1].max() + 1,step=0.01))
plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
              alpha=0.75,cmap=ListedColormap(("red","green")))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
     plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
                 c=ListedColormap(("red","green"))(i),label=j)
plt.title("K-NN(Test Set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()
