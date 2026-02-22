#Author: Deniz Rahnefeld
from neuron import Neuron

class Layer:
    def __init__(self, neuron_amount, input_length):

        self.neuron_amount = neuron_amount
        self.input_length = input_length
        self.neurons = [Neuron(input_length) for _ in range(neuron_amount)]

    
    def forward(self, input):
        layer_output = [neuron.forward(input) for neuron in self.neurons]
        return layer_output
    
    def backward(self, d_out):
        dx_lists = [neuron.backward(dOut) for neuron, dOut in zip(self.neurons, d_out)] #list of lists
        new_dx = [sum(i) for i in zip(*dx_lists)] #entpackt die äußere Liste und summiert alle Elemente mit index i auf.
        return new_dx
    
    def update(self, learningrate):
        for neuron in self.neurons:
            neuron.update(learningrate) #neuron merkt sich selber was geändert werden muss

    def export_state(self):
        neuron_states = [neuron.export_state() for neuron in self.neurons]
        return neuron_states #Liste aus Tupeln der Form (weights, bias)
    
    def import_state(self, neuron_states):
        for neuron, state in zip(self.neurons, neuron_states):
            neuron.import_state(state)