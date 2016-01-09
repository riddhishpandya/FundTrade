#do this
# sudo apt-get install tk8.6-dev
# sudo apt-get remove python-matplotlib
# sudo apt-get install python-matplotlib

import Tkinter as tk
import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.widgets import Button
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
#setting fontsizes
LARGE_FONT= ("Verdana", 12)

class fundTrade(tk.Tk):
    #args are any number of arguments passed in as input
    #kwargs are dictionary pointers passed in as input
    def __init__(self, *args, **kwargs):

        #initializing tk
        tk.Tk.__init__(self, *args, **kwargs)

        #title
        tk.Tk.wm_title(self, "Fund Trade Client")

        #size
        tk.Tk.wm_geometry(self, "900x600")
        ws = tk.Tk.winfo_screenwidth(self) # width of the screen
        hs = tk.Tk.winfo_screenheight(self) # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (900/2)
        y = (hs/2) - (600/2)

        # set the dimensions of the screen
        # and where it is placed
        tk.Tk.wm_geometry(self, '%dx%d+%d+%d' % (900, 600, x, y))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #creates a dictionary
        self.frames = {}

        for allFrames in (StartPage, SecondPage, Graph):

            frame = allFrames(container, self)

            self.frames[allFrames] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    #pass through self and controller
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def qf(stringToPrint):
    print(stringToPrint)

class Graph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        theFigure = Figure(figsize=(2,2), dpi=100)
        thePlot = theFigure.add_subplot(121)
        thePlot.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(theFigure, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)


        button1 = ttk.Button(self, text = "V1",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text = "V3",
                            command=lambda: controller.show_frame(SecondPage))
        button2.pack()



        theFigure = Figure(figsize=(2,2), dpi=100)
        thePlot = theFigure.add_subplot(121)
        thePlot.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(theFigure, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        #CREATING GRAPH
        # toolbar = NavigationToolbar2TkAgg(canvas, self)
        # toolbar.update()
        # canvas._tkcanvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

#secondPage
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        button1 = ttk.Button(self, text = "V1",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text = "V3",
                            command=lambda: controller.show_frame(SecondPage))
        button2.pack()

        theFigure = Figure(figsize=(2,2), dpi=100)
        thePlot = theFigure.add_subplot(121)
        thePlot.plot(sin(2*pi*x))

        canvas = FigureCanvasTkAgg(theFigure, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.X, expand=True)




app = fundTrade()
app.mainloop()
