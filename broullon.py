import matplotlib.pyplot as plt
import pandas as pd
import warnings
import seaborn as sns
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
import joblib
import featurewiz as FW
from featurewiz import featurewiz

warnings.filterwarnings('ignore')
df = pd.read_csv('dataset.csv')
'''
dataset = pd.get_dummies(df, columns=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])
standardScaler = StandardScaler()

# Standarisation___________

columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
dataset[columns_to_scale] = standardScaler.fit_transform(dataset[columns_to_scale])
#data_selected = FW.featurewiz(dataset, 'target', corr_limit=0.70, verbose=2, sep=',', header=0, test_data='',feature_engg='', category_encoders='', ask_xgboost_flag=False, nrows=None)
features, train = featurewiz(df, 'target', corr_limit=0.7, verbose=2, sep=",", header=0,test_data="", feature_engg="", category_encoders="")
data_colums = dataset.columns
intersection = [value for value in data_colums if value in features]
print(dataset[intersection])
#print(data_selected)
print("this is the features ________________________________________________________________", features)
print("this is the intersetion _____________________________________________________________")
'''
cp = ["Angine typique", "Angine atypique", "Douleur non angineuse", "Asymptomatique"]
print(cp.index("Angine atypique"))
