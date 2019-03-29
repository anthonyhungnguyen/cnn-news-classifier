import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def label(cate):
    return {
        0: 'business',
        1: 'entertainment',
        2: 'health',
        3: 'sports'
    }.get(cate, 4)

# Get dataset
dataset = pd.read_csv('tf_idf.csv')
X = dataset.iloc[:, 0:-1].values
y = dataset.iloc[:, -1].values

# New data
dataset_new = pd.read_csv('tf_idf_new.csv')
X_new = dataset_new.iloc[:, :].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=0)


# KNN-Classifer
clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train, y_train)

# Predicting the Test set results
y_pred = clf.predict(X_test)

# Predict newtext
y_new = clf.predict(X_new)

for y in y_new:
    print(label(y))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Accuracy
accuracy = accuracy_score(y_test, y_pred) * 100