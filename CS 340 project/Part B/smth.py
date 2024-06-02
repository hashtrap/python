# Implementation of a 3-layer Multilayer Perceptron ANN
# using a sigmoid activation function.
#
# Licensed under the GNU Open Source License agreement.
# Modified code based on an older Python 2 implementation.
# https://iamtrask.github.io/2015/07/12/basic-python-network/
# Alexander Astaras 30/05/2019 alexander.astaras@gmail.com

import numpy as np  # needed for the 2D matrix calculus
import time  # needed to see the pseudorandom number generator


def sigmoid(x, derivative=False):
    if (derivative == True):
        return x * (1 - x)

    return 1 / (1 + np.exp(-x))


# input dataset (4 sets of input values for
# each of the 3 neurons comprising the input layer)
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# saving the input dataset matrix
np.savetxt("input_data_matrix.txt", X, fmt="%s")

# output dataset (4 target values for the output neuron,
# corresponding to each of the 4 sets of input value in matrix X
y = np.array([[0],
              [1],
              [1],
              [0]])

# saving the output dataset matrix
np.savetxt("output_training_targets_matrix.txt", y, fmt="%s")

# seed the random number generator so that we don't end up
# with exactly the same values each time we run this code
np.random.seed(int(time.time()))

# Create two matrices to hold the synaptic weights for layers 0 and 1,
# then initialize these weights randomly (with a mean=0).

# randomly initialize our weights with mean 0
synMatrix0 = 2 * np.random.random((3, 4)) - 1
synMatrix1 = 2 * np.random.random((4, 1)) - 1

for j in range(60000):

    # Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = sigmoid(np.dot(l0, synMatrix0))
    l2 = sigmoid(np.dot(l1, synMatrix1))

    # how much did we miss the target value?
    l2_error = y - l2

    if (j % 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error * sigmoid(l2, derivative=True)

    # This is the most important line in this program, as it describes error backpropagation.
    # The rest of the code is the same as for the simple 2-layer MLP.
    # How much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(synMatrix1.T)

    # this is the weight change training rule for this MLP.
    # Calculate how much we missed (target - output, for each neuron)
    # and multiply it by the slope of the sigmoid at the values in l1.
    # This varies the weight modification: large corrective steps when
    # we are far away from target, smaller corrections when we approach it.
    l1_delta = l1_error * sigmoid(l1, derivative=True)

    # update weights
    synMatrix1 += l1.T.dot(l2_delta)
    synMatrix0 += l0.T.dot(l1_delta)

# Done with our 60000 training epcohs, time to save and display results

# The synapse matrices is our AI program, in a way. Saving it.
np.savetxt("synapse_matrix0.txt", synMatrix0, fmt="%s")
np.savetxt("synapse_matrix1.txt", synMatrix1, fmt="%s")

# The output matrix should be close to the training target, hopefully.
np.savetxt("output_matrix_after_training.txt", l2, fmt="%s")

print("\nAfter training, the synapse matrix for layer 0 looks like this:")
print(synMatrix0)
print("\nAfter training, the synapse matrix for layer 1 looks like this:")
print(synMatrix1)
print("\nAfter Training, the neuron excitation")
print("values of the output layer are:")
print(l2)
