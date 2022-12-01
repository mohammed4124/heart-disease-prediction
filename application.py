import matplotlib.pyplot as plt
import pandas as pd
import warnings
import seaborn as sns
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.decomposition import PCA
import joblib
from sklearn import metrics

#-----------variables---------------
knn_scores = []
y_predicted=[]
#knn_classifier=[],[]
warnings.filterwarnings('ignore')

df = pd.read_csv('dataset.csv')


def inforamation():
    df.info()

# # Feature Selection

# obtain the correlation of each feature in dataset


# plot heat map

def plot_heat_map():
    corrmat = df.corr()
    top_corr_features = corrmat.index
    plt.figure(figsize=(15, 15))
    g = sns.heatmap(df[top_corr_features].corr(), annot=True, cmap='RdYlGn')
    g.set_yticklabels(g.get_yticklabels(), rotation=0, horizontalalignment='right')
    plt.show()


def plot_histogram():
    df.hist()
    plt.show()


def plot_patient_num():
    sns.set_style('whitegrid')
    sns.countplot(x='age', data=df, palette='RdBu_r')
    plt.show()


# # Data Processing
#In data processing, the categorical values are converted to dummy variables and scale all the values before training the machine leraning models.

def dataProcessingAndAlgorithm():

    # data Processing
    dataset = pd.get_dummies(df, columns=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])
    standardScaler = StandardScaler()
    # Standarisation___________
    columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    dataset[columns_to_scale] = standardScaler.fit_transform(dataset[columns_to_scale])


    # Feature extraction with PCA

    pca = PCA(n_components=7)
    pca.fit(dataset)
    dataset_pca = pca.transform(dataset)



    global y, x, X_test, X_train, y_test
    y = dataset['target']
    # x = dataset.drop(['target'], axis=1)
    x = dataset_pca
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=1)

    # Algorithm

    for k in range(1, 21):
        knn_classifier = KNeighborsClassifier(n_neighbors=k)
        knn_classifier.fit(X_train, y_train)
        global knn_scores
        knn_scores.append(round(knn_classifier.score(X_test, y_test), 4))

    knn_classifier = KNeighborsClassifier(n_neighbors=13).fit(X_train, y_train)
    for x in X_test:
        y_predicted.append(knn_classifier.predict([x]))
    joblib.dump(knn_classifier, 'knn_model.pkl')
    '''score = cross_val_score(knn_classifier, x, y, cv=10)
    print("the accuracy of the algorithm is ----> ", score)'''


def processing_test_value(h):
    datas = pd.DataFrame(columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'])
    ar = pd.DataFrame(data=np.array([h]), columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'])
    data_to_test = pd.concat([datas, ar], ignore_index=True)
    data_to_test = pd.concat([df, ar], ignore_index=True)

    data_to_test = pd.get_dummies(data_to_test, columns=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])
    standardScaler = StandardScaler()
    # Standarisation___________

    columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    data_to_test[columns_to_scale] = standardScaler.fit_transform(data_to_test[columns_to_scale])
    pca = PCA(n_components=7)
    pca.fit(data_to_test)
    dataset_pca = pca.transform(data_to_test)
    x_test = data_to_test.drop(['target'], axis=1)
    #r = dataset_pca.iloc[-1]
    #r = r.reshape(1, -1)
    return [dataset_pca[-1]] #[r]


def test(test_values):

    # Load the pickled model
    laoded_model = joblib.load('knn_model.pkl')
    # Use the loaded pickled model to make predictions
    prediction = laoded_model.predict(test_values)
    return prediction


def plot_knn_scores():
    if knn_scores==[]:
        dataProcessingAndAlgorithm()
    plt.plot([k for k in range(1, 21)], knn_scores, color='blue')
    for i in range(1, 21):
        plt.text(i, knn_scores[i-1], (i, knn_scores[i-1]))
    plt.xticks([i for i in range(1, 21)])
    plt.xlabel('Nombre de voisins (K)', color='Red', weight='bold', fontsize='12')
    plt.ylabel('Accuracy', color='Red', weight='bold', fontsize='12')
    plt.title('Accuracy du classificateur KNN pour différentes valeurs K', color='Red', weight='bold', fontsize='12')
    plt.show()
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"


def main():
        dataProcessingAndAlgorithm()
    # print(test(processing_test_value([45,1,3,110,264,0,1,132,0,1.2,1,0,3,0])))
        print("the accuracy is ", metrics.accuracy_score(y_test, y_predicted))
        print("the precision is ", metrics.precision_score(y_test, y_predicted))
        print("the F1-score is ", metrics.f1_score(y_test, y_predicted))
        print("the recall is ", metrics.recall_score(y_test, y_predicted))


if __name__ == '__main__':
    main()
