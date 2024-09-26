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

    # constructor to create the necessary data and upload the data
    # premade data to make sure that we have an option always
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

    # Method to display the data we have with a label
    def Display(self) -> None:
        print(self.car_data.head(5))

    # Here the user chooses which topology to work with
    def Topology(self) -> None:
        value = input("Please enter the topology you wish to(e.g 10-4-5).(min=2 layers) ")

        try: # Checks that the data is what we want
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

    # The method used to decide how we want to split the data for training
    def Test_split(self) -> None:
        option = input("Choose 1 if you want a 80-20 training or 2 if you want 50-50")
        if option == "1":
            self.random_split = True
        elif option == "2":
            self.random_split = False
        else:
            print("Exiting program, default value will be used")

    # The method we use to chose the training steps we want
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

    #Private method to start the training of the model
    # Made private so that the user doesn't mess and ruin the work flow
    def _training(self,graph=False) -> None:

        print("Gathering necessary data....")
        X = self.car_data.iloc[:, 0:4]
        y = self.car_data.select_dtypes(include=['int64'])

        le = preprocessing.LabelEncoder()
        y = y.apply(le.fit_transform)

        if self.random_split: # dependending on what split we chose the data will be randomized or not
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

        if self.train_step is None: # If we haven't provided a training step number it will
            # train adaptivly
            mlp = MLPClassifier(hidden_layer_sizes=self.topology
                                , max_iter=1000
                                , learning_rate='adaptive')

            mlp.fit(X_train, y_train.values.ravel())

        else: # since training step provided we work with that
            mlp = MLPClassifier(hidden_layer_sizes=self.topology
                                , max_iter=1000
                                , learning_rate='constant'
                                , learning_rate_init=self.train_step)
            mlp.fit(X_train, y_train.values.ravel())



        predictions = mlp.predict(X_test)


        print("Training complete")
        if not graph: # if statements used to return different values depending on the need
            return y_test,predictions
        else:
            return mlp,X_train,y_train

    # The private methods call function
    def Training(self) -> None:
        self._training()

    # The method we have for matrix and classification report
    def Classification(self):
        y_test, predictions = self._training()
        print('Now printing the confusion matrix (without normalization)...\n')
        matrix=confusion_matrix(y_test, predictions)
        print(confusion_matrix(y_test, predictions))

        with open("output_data.txt", "w") as file:
             file.writelines(str(y_test))
        print('\nNow printing the classification report...\n')
        print(classification_report(y_test, predictions))
        print("Accuracy of the model:")
        print(accuracy_score(y_test, predictions))

    # Method where we create the necessary files and the graphs
    # Warning if programm seems to be in infinite loop it is not
    # The file making and training take a lot of time
    def Graphs(self) -> None:
        mlp,X_train,y_train = self._training(True)
        loss=[]
        weights=[]
        values=y_train.values.tolist()

        for q in range(0, len(values)):
            with open("testing_data_unlabeled.txt", "a") as file:
                file.writelines(str(values[q]) + "\n")
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
        


        for i in range(0,8000):
             mlp.partial_fit(X_train, y_train.values.ravel())
             loss.append(mlp.loss_)
        weights=mlp.coefs_

        # Loss change graph
        plt.plot(range(8000),loss)
        plt.xlabel('Iteration')
        plt.ylabel('Loss')
        plt.title('Loss Progress')
        plt.show()


        #Weights change graph
        plt.plot(weights[0])
        plt.xlabel('Iteration')
        plt.ylabel('Weights')
        plt.title('Weight Progression')
        plt.show()

    # Method used to produce the 18 error graphs
    # the saving into files doesn't work but they are displayed
    def graph_18(self):
        # The simulated cases to record the graphs
        topologys=[(10,10),(10,3,2),(4,5,6,7)]
        train_split=[(0.5,False),(0.8,True)]
        learning_rate = [0.001, 0.5, 'adaptive']
        X = self.car_data.iloc[:, 0:4]
        y = self.car_data.select_dtypes(include=['int64'])
        count=0

        le = preprocessing.LabelEncoder()
        y = y.apply(le.fit_transform)

        for type in topologys:
            for rate in learning_rate:
                for split in train_split:
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 - split[0],
                                                                        random_state=42 if split[1] else None)
                    scaler = StandardScaler()
                    X_train = scaler.fit_transform(X_train)
                    X_test = scaler.transform(X_test)


                    if rate=='adaptive':
                         mlp = MLPClassifier(hidden_layer_sizes=type
                                            , max_iter=1000
                                            , learning_rate=rate)
                    else:
                        mlp = MLPClassifier(hidden_layer_sizes=type
                                            , max_iter=1000
                                            , learning_rate='constant'
                                            ,learning_rate_init=rate
                                            )
                    mlp.fit(X_train, y_train.values.ravel())
                    loss=[]
                    for i in range(0, 8000):
                        mlp.partial_fit(X_train, y_train.values.ravel())
                        loss.append(mlp.loss_)

                    plt.plot(range(8000),loss)
                    plt.xlabel('Iteration')
                    plt.ylabel('Loss')
                    plt.title('Loss Progress')
                    plt.show()
                    plt.tight_layout()
                    plt.savefig("Error_graph{c}".format(c=count), dpi=300)
                    count+=1



