#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pandas as pd
# %%
#%%
# # splitter
from sklearn.model_selection import train_test_split
# algorithm
from sklearn import tree
# for computing the confusion matrix
from sklearn.metrics import confusion_matrix



# %%
import csv

vib = pd.read_csv('04_41_DT_Accelerometer.csv')



# %%
vib.shape


#%%
vib.columns=["Hora","No","Vibracion","Lugar" ]

# plot
labels, index = np.unique(vib["Lugar"], return_inverse=True)
fig1 = plt.figure(1)
fig1.set_size_inches(14, 6)
ax1 = fig1.add_subplot(111)
sc=ax1.scatter(vib["No"], vib["Vibracion"], marker='o', c=index, alpha=1.0, s=50, edgecolor='black')
ax1.legend(sc.legend_elements()[0], labels)
plt.title("Accelerometer")
plt.xlabel("")
plt.ylabel("Vibracion")
plt.show()


#%%
vib.head()


#%%
X=vib[vib.columns[2:3]]
y=vib[vib.columns[3:4]]


#%%
X.head(4)


#%%
y.head(4)


#%%
# Making Class a list
y=y[y.columns[0:1]].values.tolist()


#%%
# show type of y
type(y)


#%%
#   65% train 35% test split
#   random_state for replicate the experiment
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.35, random_state=42)


#%%
# Show dimensions data
print(X_train.shape)
print(X_test.shape)


#%%
print(len(y_train))
print(len(y_test))


#%%
# Decision Tree:
decisionTree = tree.DecisionTreeClassifier(criterion='entropy')


#%%
# fit the model to X and y (in training the model)
decisionTree.fit(X_train, y_train)


#%%
# using the X for testing to predict
y_pred = decisionTree.predict(X_test)


#%%
# If we know the y test, how is the accuracy of model 
decisionTree.score(X_test, y_test)


#%%
# create matrix to compare real vs predicted values
confusion_matrix(y_test, y_pred)


#%%
import seaborn as sns

cf_matrix = confusion_matrix(y_test, y_pred)
ax = sns.heatmap(cf_matrix, annot=True, cmap='Blues')

ax.set_title('Seaborn Confusion Matrix with labels\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['domo','pavimento','Stadis'])
ax.yaxis.set_ticklabels(['domo','pavimento','Stadis'])

## Display the visualization of the Confusion Matrix.
plt.show()

