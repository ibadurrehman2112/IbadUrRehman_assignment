import streamlit as st 
from sklearn import datasets
import numpy as np 
import pandas as pd
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
st.title("Streamlit Simple App by Ibad Ur Rehman")

st.write("""
## Explore different classifier
Which one is the best?
""")

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris","Breast Cancer","Wine Dataset")) 
#Assign the dataset selected in the box to the variable
# st.write(dataset_name)

classifier_name = st.sidebar.selectbox("Select Classifier",("KNN","SVM","Random Forest"))

def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "Breast Cancer":
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()
    
    X = data.data
    y = data.target
    df = pd.DataFrame(X)
    df['Target'] = y
    if st.checkbox('Show Raw Data'):
        "Dataset",df
    return X,y

X,y = get_dataset(dataset_name)
st.write("shape of the dataset",X.shape)
st.write("Number of classes", len(np.unique(y)))

def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == "KNN":
        K = st.sidebar.slider("K", 1, 15)
        params["k"]=K
    elif clf_name == "SVM":
        C = st.sidebar.slider("C", 0.01, 10.0)
        params['c']=C
    else:
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        n_estimators = st.sidebar.slider("n_estimators", 1, 100)
        params['max_depth'] = max_depth
        params['n_estimators'] = n_estimators
    return params

params = add_parameter_ui(classifier_name)

def get_classifer(clf_name, params):
    if clf_name == "KNN":
        clf = KNeighborsClassifier(n_neighbors=params["k"])
    elif clf_name == "SVM":
        clf = SVC(C=params["c"])
    else:
        clf = RandomForestClassifier(n_estimators=params["n_estimators"], max_depth=params["max_depth"],random_state=1234)
    return clf

clf = get_classifer(classifier_name, params)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=1234)

clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

acc= accuracy_score(y_test, y_pred)
st.write(f"classifier = {classifier_name}")
st.write(f"accuracy = {acc}")

# Plot
pca = PCA(n_components=2)
X_projected = pca.fit_transform(X)

x1 = X_projected[:,0]
x2 = X_projected[:,1]

fig = plt.figure()
plt.scatter(x1, x2, c=y, alpha=0.8, cmap="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()

#plt.show()
st.pyplot(fig)



