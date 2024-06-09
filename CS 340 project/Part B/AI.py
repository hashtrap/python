import pandas as pd
import numpy as np
import time
from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# A list with the labels of the data put outside so that it is a global variable
columns = ['Variance', 'Skewness', 'Curtosis', 'Entropy', 'Class']


class Ai:

    def __init__(self):
        self.data = []
        self.topology = (10,10,10)
        self.train_step = None
        self.random_split = True
        self.car_data = pd.read_csv('data_banknote_authentication.txt'
                                    , names=columns)
        self.car_data.to_csv("original_labeled_data.txt"
                             , header=columns
                             , index=None
                             , sep=','
                             , mode='w')

    def Display(self) -> None:
        print(self.car_data.head(5))

    def Topology(self) -> None:
        value = input("Please enter the topology you wish to(e.g 10-4-5).(min=2 layers) ")

        try:
            if value != "":
                self.topology = ()
                topology = value.split("-")
                if len(topology) >= 2:
                    for i in topology:
                        self.topology = (*self.topology, (int(i)))


                else:
                    print("Exiting program, the limit is two hidden layers, using default")
            else:
                print("Exiting program, using default")
        except ValueError:
            print("Error what you entered wasn't a number but a character, using default")

    def Test_split(self) -> None:
        option = input("Choose 1 if you want a 80-20 training or 2 if you want 50-50")
        if option == "1":
            self.random_split = True
        elif option == "2":
            self.random_split = False
        else:
            print("Exiting program, default value will be used")

    def Training_steps(self, ) -> None:
        steps = input("Please enter the number for training steps(0.001 - 0.5)")
        try:
            if steps == "":
                print("Because steps weren't chosen it will be left to the system.")
            elif float(steps) < 0.001 or float(steps) > 0.5:
                print("The input entered isn't in the designated limit")
            else:
                self.train_step = float(steps)

        except ValueError:
            print("Error: Characters or spaces aren't numbers")

    def _training(self,graph=False) -> None:

        print("Gathering necessary data....")
        X = self.car_data.iloc[:, 0:4]
        y = self.car_data.select_dtypes(include=['int64'])

        le = preprocessing.LabelEncoder()
        y = y.apply(le.fit_transform)

        if self.random_split:
            print("Initiate training....")
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20
                                                                , random_state=np.random.seed(int(time.time())))
        else:
            print("Initiate training....")
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

        scaler = StandardScaler()
        scaler.fit(X_train)

        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)

        if self.train_step is None:
            mlp = MLPClassifier(hidden_layer_sizes=self.topology
                                , max_iter=1000
                                , learning_rate='adaptive')

            mlp.fit(X_train, y_train.values.ravel())

        else:
            mlp = MLPClassifier(hidden_layer_sizes=self.topology
                                , max_iter=1000
                                , learning_rate='constant'
                                , learning_rate_init=self.train_step)
            mlp.fit(X_train, y_train.values.ravel())
            mlp.loss_


        predictions = mlp.predict(X_test)


        print("Training complete")
        if not graph:
            return y_test,predictions
        else:
            return mlp,X_train,y_train


    def Training(self) -> None:
        self._training()

    def Classification(self):
        y_test, predictions = self._training()
        print('Now printing the confusion matrix (without normalization)...\n')
        matrix=confusion_matrix(y_test, predictions)
        print(confusion_matrix(y_test, predictions))

        with open("output_data.txt", "w") as file:
             file.write("  0   1 \n")
             file.writelines("0 "+str(matrix[0][0])+" "+str(matrix[0][1])+"\n1 "+str(matrix[1][0])+" "+str(matrix[1][1])+"\n")
        print('\nNow printing the classification report...\n')
        print(classification_report(y_test, predictions))
        print("Accuracy of the model:")
        print(accuracy_score(y_test, predictions))

    def Graphs(self) -> None:
        mlp,X_train,y_train = self._training(True)
        loss=[]
        weights=[]
        values=y_train.values.tolist()
        for j in range(0, len(values)):
            with open("testing_data_unlabeled.txt", "a") as file:
                file.writelines(str(values[j]) + "\n")
        for j in range(0, len(values)):
            with open("testing_data_labeled.txt", "a") as file:
                if j>0:
                     file.writelines(str(values[j]) + "\n")
                else:
                   file.write("Class \n")


        for j in range(0,len(X_train)):
            with open("training_data.txt","a") as file:
                if j >0:
                    file.writelines(str(X_train[j])+"\n")
                else:
                    file.write("Variance,Skewness,Curtosis,Entropy \n")
        
        

        for i in range(0,1000):
             mlp.partial_fit(X_train, y_train.values.ravel())
             loss.append(mlp.loss_)
        weights=mlp.coefs_
        print(len(weights))
        plt.plot(loss)
        plt.xlabel('Iteration')
        plt.ylabel('Loss')
        plt.title('Weight Loss Progress')
        plt.show()



        plt.plot(weights[0])
        plt.xlabel('Iteration')
        plt.ylabel('weights')
        plt.title('Progress')
        plt.show()


a = Ai()
a.Graphs()
