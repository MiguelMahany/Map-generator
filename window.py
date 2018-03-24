from tkinter import *
import NoiseMap
import colormap
from PIL import ImageTk,Image

class Window(Frame):

    def __init__(self,master):
        self.WIDTH = IntVar()
        self.HEIGHT = IntVar()
        self.SCALE = IntVar()
        self.OCTAVES = IntVar()
        self.PERSISTANCE = IntVar()
        self.LACUNARITY = IntVar()
        self.SEED = IntVar()
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
        self.grid()

    def init_window(self):
        self.master.title("Map Generator")

    #                  Menu Widgets                            #
        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="New",command = self.SetNoiseMap)
        self.filemenu.add_command(label="Open")
        self.filemenu.add_separator()
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.master.config(menu=self.menubar)
    #                  Menu Widgets                            #




    #                  SetNoiseMap widgets                                #
        self.wentry=Entry(self.master,textvariable = self.WIDTH)
        self.hentry=Entry(self.master,textvariable = self.HEIGHT)
        self.scaleentry=Entry(self.master,textvariable = self.SCALE)
        self.octavesentry=Entry(self.master,textvariable = self.OCTAVES)
        self.persistanceentry=Entry(self.master,textvariable = self.PERSISTANCE)
        self.lacunarityentry=Entry(self.master,textvariable = self.LACUNARITY)
        self.seedentry=Entry(self.master,textvariable = self.SEED)
        
        self.WidthEnter = Label(self.master, text="Width: ")
        self.HeightEnter = Label(self.master, text="Height: ")
        self.ScaleEnter = Label(self.master, text="Scale: ")
        self.OctavesEnter = Label(self.master, text="Octaves: ")
        self.PersistanceEnter = Label(self.master, text="Persistance: ")
        self.LacunarityEnter = Label(self.master, text="Lacunarity: ")
        self.LacunarityEnter = Label(self.master, text="Lacunarity: ")
        self.SeedEnter = Label(self.master,text = "Seed: " )

        
        self.nmapsubmitbutton=Button(self.master,text="Submit",command=self.StartNoiseMap)

    #                  SetNoiseMap widgets                                #
        

    def SetNoiseMap(self):
    #    All the widgets for inputting values for NoiseMap.py's NoiseMapGenerator  
        
        self.wentry.grid(row=0,column=1)
        self.hentry.grid(row=1,column=1)
        self.scaleentry.grid(row=2,column=1)
        self.octavesentry.grid(row=3,column=1)
        self.persistanceentry.grid(row=4,column=1)
        self.lacunarityentry.grid(row=5,column=1)
        self.seedentry.grid(row=6,column=1)
        self.WidthEnter.grid(row=0,column=0)
        self.HeightEnter.grid(row=1,column=0)
        self.ScaleEnter.grid(row=2,column=0)
        self.OctavesEnter.grid(row=3,column=0)
        self.PersistanceEnter.grid(row=4,column=0)
        self.LacunarityEnter.grid(row=5,column=0)
        self.SeedEnter.grid(row=6,column=0)
        self.nmapsubmitbutton.grid(row = 7, column = 0)


    def StartNoiseMap(self):
    #Creates noise map from NoiseMap.py, which outputs an image file for ShowNoiseMap to use
        self.width  = self.wentry.get()
        self.height = self.hentry.get()
        self.scale  = self.scaleentry.get()
        self.octaves = self.octavesentry.get()
        self.persistance = self.persistanceentry.get()
        self.lacunarity = self.lacunarityentry.get()
        self.seed = self.seedentry.get()
        self.noisemap = NoiseMap.NoiseMapGenerator(self.width,self.height,self.scale,self.octaves,self.persistance,self.lacunarity,self.seed)
        self.noisemap.StartMap()
        self.ShowNoiseMap()
    
    def ShowNoiseMap(self):
    # Makes a tkimage for showing the noisemap on the tkinter window 
        self.ClearWidgets()
        self.img = Image.open("NoiseMap.png")
        self.tkimg = ImageTk.PhotoImage(self.img)
        self.noisemapimage = Label(self.master, image = self.tkimg)
        self.noisemapimage.grid(row=0,column=0)

    # def ColorNoiseMap(self):
    #     return True
    
    def ClearWidgets(self):
    # Clears all the widgets that have been created in the init_window method
        self.WidthEnter.grid_forget()
        self.HeightEnter.grid_forget()
        self.ScaleEnter.grid_forget()
        self.OctavesEnter.grid_forget()
        self.PersistanceEnter.grid_forget()
        self.LacunarityEnter.grid_forget()
        self.wentry.grid_forget()
        self.hentry.grid_forget()
        self.scaleentry.grid_forget()
        self.octavesentry.grid_forget()
        self.persistanceentry.grid_forget()
        self.lacunarityentry.grid_forget()
        self.seedentry.grid_forget()
        self.SeedEnter.grid_forget()
        self.nmapsubmitbutton.grid_forget()



root= Tk()

root.geometry("800x600")
app = Window(root)

app.mainloop()