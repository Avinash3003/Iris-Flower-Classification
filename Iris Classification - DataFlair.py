

# DataFlair Iris Classification
# Import Packages
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


columns = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Class_labels'] # As per the iris dataset information

# Load the data
df = pd.read_csv('iris.data.csv')

df.head()

# Some basic statistical analysis about the data
# df.describe()

# Seperate features and target  
data = df.values
X = data[:,0:4]
Y = data[:,4]

# Split the data to train and test dataset.
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# Support vector machine algorithm
from sklearn.svm import SVC
svn = SVC()
svn.fit(X_train, y_train)

# Predict from the test dataset
predictions = svn.predict(X_test)

# Calculate the accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)

# A detailed classification report
from sklearn.metrics import classification_report
print(classification_report(y_test, predictions))

X_new = np.array([[3, 2, 1, 0.2]])
#Prediction of the species from the input vector
prediction = svn.predict(X_new)
print("Prediction of Species: {}".format(prediction))

# Save the model
import pickle
f=open('SVM.pickle', 'wb')
pickle.dump(svn, f)







