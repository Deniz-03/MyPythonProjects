#Author: Deniz Rahnefeld
from layer import Layer
import json

class Network:
    def __init__(self, model_name, *layers): #beliebig viele Layer
        self.layers = layers #hier werden diese zu einem Tupel zusammengeführt
        self.file_name = model_name

    def forward(self, input):
        curr_output = input
        for layer in self.layers:
            curr_output = layer.forward(curr_output)
        return curr_output
    
    def backward(self, loss_gradient):
        curr_d_out = [loss_gradient]
        for layer in reversed(self.layers):
            curr_d_out = layer.backward(curr_d_out)
        
    def update(self, learningrate):
        for layer in self.layers:
            layer.update(learningrate)

    def export_state(self):
        layer_states = [layer.export_state() for layer in self.layers]
        with open(self.file_name, 'w', encoding='utf-8') as file: #w : writing
            json.dump(layer_states, file, indent=4)

    def import_state(self):
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:#r : reading
                layer_states = json.load(file)
            for layer, state in zip(self.layers, layer_states):
                layer.import_state(state)
        except FileNotFoundError:
            pass
        