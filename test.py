import pickle
import sklearn
print(sklearn.__version__)
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import _dist_metrics
dt = pickle.load(open('models/dt.pkl','rb'))
knn = pickle.load(open('models/knn.pkl','rb'))
lr = pickle.load(open('models/lr.pkl','rb'))
nb = pickle.load(open('models/nb.pkl','rb'))
rf = pickle.load(open('models/randomf.pkl','rb'))
pred = dt.predict([[88,6,807,0,2]])
print(pred[0])
