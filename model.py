import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/yearly-water-usage.csv"
train = pd.read_csv(url)

train.dropna(inplace=True)

target = 'Water'
features = ['Year']

X = train[features]
y = train[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=40)
print(X_train.shape)
print(X_test.shape)

mlp = MLPClassifier(hidden_layer_sizes=(1,2,1), activation='tanh', solver='adam', max_iter=500)
mlp.fit(X_train,y_train)

import pickle
pickle.dump(mlp, open('model.pkl', 'wb'))
