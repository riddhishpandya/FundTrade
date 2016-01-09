from Tkinter import *

#download and install pillow:
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
from PIL import Image, ImageTk


class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("GUI")

        self.pack(fill = BOTH, expand = 1)

        #quitButton = Button(self, text = "QUIT", command=self.client_exit)
        #quitButton.place(x =0, y = 0)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        #fileButton
        file = Menu(menu)
        file.add_command(label = "Save", command = self.client_exit)
        file.add_command(label = "Exit", command = self.client_exit)
        menu.add_cascade(label = "File", menu=file)

        #editButton that shows Image
        edit = Menu(menu)
        edit.add_command(label = "Show Image",command = self.showImg)
        edit.add_command(label = "Show Text",command = self.showTxt)
        menu.add_cascade(label = "Edit", menu=edit)

 ##displays image and outputs and saves 4 copies of different downsized formats
    def showImg(self):
        load = Image.open('pic.jpg')
        # adjust width and height to your needs
        width = 225
        height = 225
        # use one of these filter options to resize the image
        im2 = load.resize((width, height), Image.NEAREST)      # use nearest neighbour
        im3 = load.resize((width, height), Image.BILINEAR)     # linear interpolation in a 2x2 environment
        im4 = load.resize((width, height), Image.BICUBIC)      # cubic spline interpolation in a 4x4 environment
        load = load.resize((100, 100), Image.ANTIALIAS)    # best down-sizing filter
        ext = ".jpg"
        #im2.save("NEAREST" + ext)
        #im3.save("BILINEAR" + ext)
        #im4.save("BICUBIC" + ext)
        #load.save("ANTIALIAS" + ext)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image = render)
        img.image = render
        img.place(x = 10, y = 10)

    def showTxt(self):
        text = Label(self, text = "What's good nigga")
        text.pack()

    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")

app = Window(root)



root.mainloop()
