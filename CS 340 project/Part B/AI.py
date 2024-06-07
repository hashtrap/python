import pandas as pd
import numpy as np
import time

class Ai:

    def __init__(self):
        self.data=[]
        self.topology=(10,10,10)
        self.train_step=None
        self.random_split=True
        columns = ['variance', 'skewness', 'curtosis', 'entropy', 'class']
        self.car_data = pd.read_csv('data_banknote_authentication.txt', names=columns)
    def Display(self)->None:
       print(self.car_data.head(5))

    def Topology(self)->None:
        value=input("Please enter the topology you wish to(e.g 10-4-5).(min=2 layers) ")

        try:
            if value!="":
                self.topology=()
                topology=value.split("-")
                if len(topology)>=2:
                    for i in topology:
                        self.topology=(*self.topology,(int(i)))


                else:
                    print("Exiting program, the limit is two hidden layers, using default")
            else:
                print("Exiting program, using default")
        except ValueError:
               print("Error what you entered wasn't a number but a character, using default")
    def Test_split(self)->None:
        option=input("Choose 1 if you want a 80-20 training or 2 if you want 50-50")
        if option=="1":
            self.random_split=True
        elif option=="2":
            self.random_split=False
        else:
            print("Exiting program, default value will be used")
    def Training_steps(self,)->None:
        steps=input("Please enter the number for training steps(0.001 - 0.5)")
        try:
            if steps=="":
                print("Because steps weren't chosen it will be left to the system.")
            elif float(steps)<0.001 or float(steps)>0.5:
                  print("The input entered isn't in the designated limit")
            else:
                self.train_step=float(steps)
                print(self.train_step)
        except ValueError:
            print("Error: Characters or spaces aren't numbers")

    def _training(self)->None:
       X =self.car_data.iloc[:, 0:4]
       y = self.car_data.select_dtypes(include=['int64'])




       from sklearn import preprocessing
       le = preprocessing.LabelEncoder()
       y = y.apply(le.fit_transform)

       from sklearn.model_selection import train_test_split
       if self.random_split:
             X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20
                                                                 ,random_state=np.random.seed(int(time.time())))
       else:
           X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

       from sklearn.preprocessing import StandardScaler
       scaler = StandardScaler()
       scaler.fit(X_train)

       X_train = scaler.transform(X_train)
       X_test = scaler.transform(X_test)

       from sklearn.neural_network import MLPClassifier
       mlp = MLPClassifier(hidden_layer_sizes=self.topology, max_iter=1000,learning_rate='adaptive')
       mlp.fit(X_train, y_train.values.ravel())

       predictions = mlp.predict(X_test)

       from sklearn.metrics import classification_report, confusion_matrix
       print('Now printing the confusion matrix (without normalization)...\n')
       print(confusion_matrix(y_test, predictions))
       print('\nNow printing the classification report...\n')
       print(classification_report(y_test, predictions))

    def Training(self)->None:
        self._training()


a=Ai()
a.Topology()