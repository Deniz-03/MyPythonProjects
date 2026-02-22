#Author: Deniz Rahnefeld
from userInterface import GUI
from network import Network
from layer import Layer


def commit_drawing():
    pass
    
    input = number_Gui.getState()

    for i in range(8):
        zeile =input[i*8 : (i+1)*8]
        # Druckt ein '#' für Tinte (1.0) und einen Punkt für Hintergrund (0.0)
        print("".join(['#' if pixel == 1.0 else '.' for pixel in zeile]))
        print("-------------------------------------------\n")

    output = writtenNumbers_Model.forward(input)
    prediction = output.index(max(output))
    number_Gui.update_prediction(prediction)
    

number_Gui = GUI(commit_drawing)


#Netzwerk Init
#Layer 1: Hidden Layer mit 32 Neuronen mit je 64 Inputs
layer1 = Layer(32, 64)

#Layer 2: Output Layer mit 10 Neuronen mit je 32 Inputs
layer2 = Layer(32, 32)

layer3 = Layer(10,32)

writtenNumbers_Model = Network('writtenNbrs.json', layer1, layer2, layer3)

writtenNumbers_Model.import_state()

number_Gui.start()
