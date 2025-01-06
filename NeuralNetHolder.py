import math
import numpy as np

class NeuralNetHolder:
    def __init__(self):
        super().__init__()
        # Initialize the neural network with pre-trained weights

        # # Learning Rate 0.1 Momentum 0.1, lambda 0.9 hidden layer 4  
        self.weights_input_hidden = [
            [-0.49750877912392033, 1.2016780567776761], 
            [3.9012450597203903, 0.6675107395150973], 
            [0.6128513501539526, 3.0650919529059593], 
            [-3.501673328451882, 2.191063728579324]
        ]
        
        self.weights_hidden_output = [
            [1.873447273808668, 3.3091160965287, -4.627440859589127, 0.907365032837498], 
            [11.292756770956506, -2.96557321629238, -2.058701884008144, -4.757812016009416]
        ]

        self.min_vals = [-611.633297, 65.904359]
        self.max_vals = [610.366748, 749.980887]
        self.min_vector = [-4.999903, -4.999939]
        self.max_vector = [8.000000, 4.999938]

    def normalize(self, value, min_val, max_val):
        return (value - min_val) / (max_val - min_val)

    def denormalize(self, normalized_value, min_val, max_val):
        return normalized_value * (max_val - min_val) + min_val

    def sigmoidCalc(self, v):
        lambdaVal = 0.9
        if v > 100:  # Prevent overflow
            return 1.0
        elif v < -100:  # Prevent underflow
            return 0.0
        return 1 / (1 + math.exp(-lambdaVal * v))

    def layerValCalc(self, input_layer, weights):
        layer = []

        for i in range(len(weights)):
            layer_val = 0

            for j in range(len(weights[i])):
                layer_val += input_layer[j] * weights[i][j]

            layer.append(layer_val)
        return layer

    def feed_forward(self, input_layer_val):
        outputs = []
        v = 0

        for i in range(2):
            if i == 0:
                v = self.layerValCalc(input_layer_val, self.weights_input_hidden) 
            else:
                v = self.layerValCalc(input_layer_val, self.weights_hidden_output)

            if i != 1:
                hidden_outputs = [self.sigmoidCalc(val) for val in v] 
            else:
                hidden_outputs = v
            input_layer_val = hidden_outputs
            outputs.append(hidden_outputs)

        return outputs

    def predict(self, input_row):
        # Extract the input values
        x_distance_to_target, y_distance_to_target = input_row.split(',')

        # Convert them to float (if needed)
        x_distance_to_target = float(x_distance_to_target)
        y_distance_to_target = float(y_distance_to_target)

        # Normalize the input values
        normalized_x = self.normalize(x_distance_to_target, self.min_vals[0], self.max_vals[0])
        normalized_y = self.normalize(y_distance_to_target, self.min_vals[1], self.max_vals[1])

        # Create the input layer
        input_layer = [normalized_x, normalized_y]

        # Perform feed forward
        outputs = self.feed_forward(input_layer)

        # Extract predictions (assumes outputs[-1] contains the final layer outputs)
        vel_x_normalized, vel_y_normalized = outputs[-1]

        # De-normalize the predictions
        vel_x = self.denormalize(vel_x_normalized, self.min_vector[0], self.max_vector[0])
        vel_y = self.denormalize(vel_y_normalized, self.min_vector[1], self.max_vector[1])

        # Return the predictions
        return vel_y, vel_x
