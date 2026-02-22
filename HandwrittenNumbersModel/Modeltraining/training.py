#Author: Deniz Rahnefeld

#Model Training for handwritten Numbers
from sklearn.datasets import load_digits
from network import Network
from layer import Layer
from neuron import Neuron

digits = load_digits()


## Preprocessing
# Hier werde ich die Rohen Bilddaten, also eine 2D Matrix mit Werten       
# zwischen 0 (Weiß) und 16(Schwarz), zunächst in eine Liste umschreiben
# und dann auf 0 und 1 abbilden, also die Graustufen filtern.
# 

raw_images = digits.images
raw_targets = digits.target




#Flattening:
flattend_images = []
for img in raw_images:
    flattend_images.append([img[x][y] for x in range(8) for y in range(8)])


#Übersetzen von targets in binäre Listen
targets = [] #Eine Liste aus Listen mit binären Werten und der Länge 10
for i in raw_targets:
    targets.append([1 if j == i else 0 for j in range(10)])

#Aufsplitten der Trainingsdaten
x_img = flattend_images[:1400]
x_trgts  = targets[:1400]

y_img = flattend_images[1400:]
y_trgts = targets[1400:]


#Netzwerk Init
#Layer 1: Hidden Layer mit 32 Neuronen mit je 64 Inputs
layer1 = Layer(32, 64)

#Layer 2: Output Layer mit 10 Neuronen mit je 32 Inputs
layer2 = Layer(32, 32)

layer3 = Layer(10,32)

writtenNumbers_Model = Network('writtenNbrs.json', layer1, layer2, layer3)

writtenNumbers_Model.import_state()

treffer = 0
amnt_tests = len(y_img)
#verification loop
for img, trgt in zip(y_img, y_trgts):
    output = writtenNumbers_Model.forward(img)

    prediction = output.index(max(output))

    truth = trgt.index(max(trgt))

    if prediction == truth:
        treffer += 1

accuracy = (treffer / amnt_tests) * 100
print(f"Das Netzwerk hat {treffer} von {amnt_tests} Bildern richtig erkannt!")
print(f"Genauigkeit: {accuracy:.2f} %")

"""
#Trainingsloop
for epoch in range(100):
    loss = 0.0
    for img, trgt in zip(x_img, x_trgts):
        prediction = writtenNumbers_Model.forward(img)
        d_out = [(p-e) for p, e in zip(prediction, trgt)]
        writtenNumbers_Model.backward(d_out)
        writtenNumbers_Model.update(0.02)

        loss += sum(d**2 for d in d_out)

    print(f'Epoche {epoch + 1}/100: Aktueller Fehler: {loss:.4f}')


writtenNumbers_Model.export_state()
"""