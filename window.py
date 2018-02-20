from tkinter import *
from PIL import Image,ImageTk

class Window(Frame):

    
    def __init__(self, master = None):
        
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.place()

    def init_window(self):
        global mapSizeX
        global mapSizeY

        self.master.title("Map Generator")
        ##                 Menu bar stuff                   ##
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Save")
        file.add_command(label="New", command = self.startMap)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu = edit)
        ##                                                   ##

        ##                   Buttons and labels  yo                      ##
        
        self.labelX = Label(self, text="X size:")
        mapSizeX = IntVar()
        self.sizeEnterX = Entry(self.master, textvariable = mapSizeX, width =5)
        self.labelY = Label(self, text="Y size:")
        mapSizeY = IntVar()
        self.sizeEnterY = Entry(self.master, textvariable = mapSizeY, width = 5)
        self.submitButton = Button(self, text = "Submit", command = self.createImg)
        
        ##                   Buttons and labels  yo                      ##

    def startMap(self):
        self.labelX.grid(row=0)
        self.labelY.grid(row=1)
        self.sizeEnterX.grid(row=0,column=1,sticky=N)
        self.sizeEnterY.grid(row=1,column=1)
        

    def createImg(self):
        newSave=Image.new("RGB",(mapSizeX.get(),mapSizeY.get()), (255,255,255))
        self.render = ImageTk.PhotoImage(newSave)
        # labels can be text or images
        
        self.img = Label(self, image=self.render)
        self.img.image = self.render
        self.img.grid()
        self.clearButton = Button(self, text = "Clear", command = self.destroyImg)
        self.clearButton.grid(column= 2,row=1)
        self.submitButton.config(state=DISABLED)

    def destroyImg(self):
        self.clearButton.grid_forget()
        self.submitButton.config(state=ACTIVE)
        self.img.destroy()



root = Tk()

root.geometry("800x600")

app = Window(root)

root.mainloop()

