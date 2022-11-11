import tkinter
import sys
import math
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


root = Tk()
root.title("Logistic Functions")
root.geometry("1600x1600")
sys.setrecursionlimit(100) # sets the number of iterations before an error is called
data1 = []
data2 = []
data3 = []
xvalue = []
yvalue1 = []
yvalue2 = []
yvalue3= []

class ModelSetUp:
    def __init__(self, master1):
        self.myFrame = Frame(master1)
        self.myFrame.pack()
        ModelSetUp.datasetup(self)

    def datasetup(self):

        # data set up

        self.Data_set_up = tkinter.LabelFrame(self.myFrame, text="Data Set Up")
        self.Data_set_up.grid(row=0, column=0)

        self.Constant_label= tkinter.Label(self.Data_set_up, text="Constant")
        self.Constant_label.grid(row=1, column=0)

        self.StartValue_label = tkinter.Label(self.Data_set_up,text="Start Value")
        self.StartValue_label.grid(row=2, column=0)

        self.PowersValue_label = tkinter.Label(self.Data_set_up,text="Powers for 1st function")
        self.PowersValue_label.grid(row=3, column=0)

        self.Constant = tkinter.Entry(self.Data_set_up)
        self.Constant.insert(0, 2)
        self.Constant.grid(row=1, column=1)

        self.StartValue = tkinter.Entry(self.Data_set_up)
        self.StartValue.insert(0, 0.5)
        self.StartValue.grid(row=2, column=1)

        self.PowersValue = tkinter.Entry(self.Data_set_up)
        self.PowersValue.insert(0, 1)
        self.PowersValue.grid(row=3, column=1)


        # add buttons

        self.Data_entry_button = tkinter.Button(self.Data_set_up, text="plot logistic function", command=self.logistic1)
        self.Data_entry_button.grid(row=1, column=3)

        self.Data_entry_button = tkinter.Button(self.Data_set_up, text="plot bifurcation diagram", command=self.logistic2)
        self.Data_entry_button.grid(row=2, column=3)

    def logistic1(self):
        data1.append(float(self.StartValue.get()))
        data2.append(float(self.StartValue.get()))
        logistic1(float(self.StartValue.get()),float(self.Constant.get()), float(self.PowersValue.get()))
        logistic2(float(self.StartValue.get()),float(self.Constant.get()))
        logistic3(float(self.StartValue.get()), float(self.Constant.get()))
        print ("data1 = ",data1)
        self.printgraph(data1, data2, data3)

    def logistic2(self):
        resetbifurcationdata()
        PlotBifurcationDiagram(float(self.PowersValue.get()))
        print("xvalue = ", xvalue)
        print("yvalue1 = ", yvalue1)
        print("yvalue2 = ", yvalue2)
        self.PlotBifurcationPlot(xvalue, yvalue1, yvalue2, yvalue3)

    def printgraph(self,DataToPlot1, DataToPlot2, DataToPlot3):

        self.Output = tkinter.LabelFrame(self.myFrame, text="Outputs")
        self.Output.grid(row=2, column=0)

        fig = Figure(figsize=(5, 3), dpi=100)
        fig.add_subplot(111).plot(DataToPlot1)
        fig.suptitle("Logistic Function µx^p(1-x^p)")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)

        fig = Figure(figsize=(5, 3), dpi=100)
        fig.add_subplot(111).plot(DataToPlot2)
        fig.suptitle("Logistic Function µsin(x)(1-sin(x))")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1)

        fig = Figure(figsize=(5, 3), dpi=100)
        fig.add_subplot(111).plot(DataToPlot3)
        fig.suptitle("Logistic Function µtan(x)(1-tan(x))")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=2)

        resetdata()

    def PlotBifurcationPlot(self,xvalue,DataToPlot1, DataToPlot2, DataToPlot3):

        self.Output = tkinter.LabelFrame(self.myFrame, text="Outputs")
        self.Output.grid(row=3, column=0)

        fig = Figure(figsize=(5, 3), dpi=100)
        fig.add_subplot(111).scatter(xvalue,DataToPlot1,s=0.5)
        fig.suptitle("Logistic Function µx(1-x)")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)

        fig = Figure(figsize=(5, 3), dpi=100)
        fig.add_subplot(111).scatter(xvalue,DataToPlot2,s=0.5)
        fig.suptitle("Logistic Function µsin(x)(1-sin(x))")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1)

        fig = Figure(figsize=(5, 3), dpi=100)
        fig.add_subplot(111).scatter(xvalue, DataToPlot3, s=0.5)
        fig.suptitle("Logistic Function µtan(x)(1-tan(x))")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=2)

        resetdata()


def logistic1(x,constant,power):

    print ("power = ", power)
    x1 = constant * x**power * (1 - x**power)
    if x1 >= 1:
        print ("all dead")
        data1.append(x1)
        return data1
    if x1<= 0:
        print ("all dead")
        data1.append(x1)
        return data1
    else:
        print (x1)
        data1.append(x1)

    try:
        logistic1(x1, constant,power)

    except:
        print ("run out of puff") # we run to for the total amount of iterations set

    return data1[-1]

def logistic2(x,constant):

    x2 = constant * math.sin(x) * (1 - math.sin(x))
    if x2 >= 1:
        print ("all dead")
        data2.append(x2)
        return data1
    if x2<= 0:
        print ("all dead")
        data2.append(x2)
        return data1
    else:
        print (x2)
        data2.append(x2)

    try:
        logistic2(x2, constant)

    except:
        print ("run out of puff") # we run to for the total amount of iterations set

    return data2[-1]

def logistic3(x,constant):

    x3 = constant * math.tan(x) * (1 - math.tan(x))
    if x3 >= 1:
        print ("all dead")
        data3.append(x3)
        return data1
    if x3<= 0:
        print ("all dead")
        data3.append(x3)
        return data3
    else:
        print (x3)
        data3.append(x3)

    try:
        logistic3(x3, constant)

    except:
        print ("run out of puff") # we run to for the total amount of iterations set

    return data3[-1]

def PlotBifurcationDiagram(power1):

    for j in range (1,399,1):
        j2 = float(j/100)  # we plot across the range in intervals of 1/1000
        print ("j2 = ",j2)
        logistic1(0.5, j2,power1) # 0.5 is the start value, but it is does not matter what value is chosen
        logistic2(0.5, j2)  # 0.5 is the start value, but it is does not matter what value is chosen
        logistic3(0.5, j2)

        for i in range (1,10):
            yvalue1.append(data1[-i])
            yvalue2.append(data2[-i])
            yvalue3.append(data3[-i])
            xvalue.append(j2)
    return xvalue,yvalue1,yvalue2,yvalue3

def resetbifurcationdata():
    yvalue1.clear()
    yvalue2.clear()
    yvalue3.clear()
    xvalue.clear()

def resetdata():
    data1.clear()
    data2.clear()
    data3.clear()

Model = ModelSetUp(root)  # passes the root window to the class

root.mainloop()


