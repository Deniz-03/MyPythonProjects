#Author: Deniz Rahnefeld
from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self, commit_drawing):
        self.root = Tk()
        self.root.title('Handwritten Numbers')

        self.content_frame = ttk.Frame(self.root, padding = (3, 3, 3, 3))
        self.content_frame.pack()


        self.canvas = Canvas(self.content_frame, width=80, height=80, 
                             background='black')
        self.canvas.pack(side = 'left')

        self.prediction_label = Label(self.content_frame, 
                                      text = 'Prediction: None')
        self.prediction_label.pack(side = 'right')

        self.button_frame = ttk.Frame(self.root, padding = (3, 3, 3, 3))
        self.button_frame.pack()


        self.commit_button = ttk.Button(self.button_frame, text = 'commit', 
                                                command = commit_drawing)
        self.commit_button.pack(side = 'left')


        self.clear_button = ttk.Button(self.button_frame, text = 'clear', 
                                       command = self.clear_canvas)
        self.clear_button.pack(side = 'left')

    def savePosn(self, event):
        self.lastx, self.lasty = event.x, event.y

    def addLine(self, event):
        self.canvas.create_line(self.lastx, self.lasty, event.x, event.y, fill="white", width=5)
        self.savePosn(event)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.prediction_label.config(text = f'Prediction: {None}')
    

    def update_prediction(self, prediction):
        self.prediction_label.config(text = f'Prediction: {prediction}')


    def getState(self):
        input = []
        cell_width= 10
        step_width = 2.5 # 20 / 4 Abtastrate 4x4 = 16

        for r in range(8): #rows
            row_data = []
            for c in range(8): # columns
                x_start = c * cell_width
                y_start = r * cell_width

                counter = 0

                for sub_r in range(4):
                    for sub_c in range(4):
                        px = x_start + (sub_c * step_width) + 1
                        py = y_start + (sub_r * step_width) + 1

                        if self.canvas.find_overlapping(px, py, px+1, py+1):
                            counter += 1

                row_data.append(counter)

            input.append(row_data)

        return [input[x][y] for x in range(8) for y in range(8)]
            

    

    def start(self):
        #Eventhandling Init:
        self.canvas.bind('<Button-1>', self.savePosn)
        self.canvas.bind('<B1-Motion>', self.addLine)

        self.root.mainloop()
