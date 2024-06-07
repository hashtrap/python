import pandas as pd
import numpy as np
import time

class Ai:

    def __init__(self):
        self.data=[]
        self.topology=()
        self.train_step=None
        columns = ['variance', 'skewness', 'curtosis', 'entropy', 'class']
        self.car_data = pd.read_csv('data_banknote_authentication.txt', names=columns)
    def Display(self):
       print(self.car_data.head(5))

    def Topology(self):
        topology=input("Please enter the topology you wish to(e.g 10-4-5).(min=2 layers) ")

        try:

            a=topology.split("-")
            if len(a)>=2:
                for i in a:
                   self.topology=(*self.topology,(int(i)))

            else:
                print("Exiting program, the limit is two hidden layers")
        except ValueError:
               print("Error what you entered wasn't a number but a character")
    def Training_steps(self):
        steps=input("Please enter the number for training steps")
        try:
            if steps==None:
                print("Because steps weren't chosen it will be left to the system.")
            elif steps<0.001 or steps>0.5:

        except ValueError:
            print("Error: Characters aren't numbers")

    def opology(self,topology=(10,10,10)):
       X =self.car_data.iloc[:, 0:4]
       y = self.car_data.select_dtypes(include=['int64'])




       from sklearn import preprocessing
       le = preprocessing.LabelEncoder()
       y = y.apply(le.fit_transform)

       from sklearn.model_selection import train_test_split
       X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

       from sklearn.preprocessing import StandardScaler
       scaler = StandardScaler()
       scaler.fit(X_train)

       X_train = scaler.transform(X_train)
       X_test = scaler.transform(X_test)

       from sklearn.neural_network import MLPClassifier
       mlp = MLPClassifier(hidden_layer_sizes=topology, max_iter=1000,learning_rate='adaptive')
       mlp.fit(X_train, y_train.values.ravel())

       predictions = mlp.predict(X_test)

       from sklearn.metrics import classification_report, confusion_matrix
       print('Now printing the confusion matrix (without normalization)...\n')
       print(confusion_matrix(y_test, predictions))
       print('\nNow printing the classification report...\n')
       print(classification_report(y_test, predictions))


a=Ai()
a.Topology()