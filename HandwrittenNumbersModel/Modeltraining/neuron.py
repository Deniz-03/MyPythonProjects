#Author: Deniz Rahnefeld

import random
import math

class Neuron:

    def __init__(self, input_length):   
        self.weights = [random.uniform(-0.1, 0.1) for i in range(input_length)]
        self.bias = 0
        self.cache_inputs: list = None
        self.cache_sum: float = None

    def forward(self, input): #forwardfunction sum(weights * inputs) + bias
        self.cache_inputs = input
        self.z = math.sumprod(input, self.weights) + self.bias
        self.cache_sum = self.z
        return self.reLU(self.z)

    def reLU(self, z): #Aktivierungsfunktion
        if z > 0:
            return z
        else:
            return 0
        
    def backward(self, d_out):
        if self.cache_sum > 0:
            dz = d_out * 1
        else:
            dz = 0

        self.dw = [dz * i for i in self.cache_inputs]
        self.db = dz
        dx = [dz * w for w in self.weights]
        return dx
    
    def update(self, learningrate):
        self.weights = [w - (learningrate * d_w) for w, d_w in zip(self.weights, self.dw)]
        self.bias = self.bias - (learningrate * self.db)

    def export_state(self):
        return (self.weights, self.bias)

    def import_state(self, state: tuple):
        self.weights = state[0]
        self.bias = state[1]