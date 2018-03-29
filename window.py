from tkinter import Tk, Frame,IntVar,Menu,Entry,Label,Button
import NewNoiseMap
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
        # self.SEED = IntVar()
        self.White = IntVar()
        self.Grey = IntVar()
        self.Green = IntVar()
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
        self.grid()

    def init_window(self):
    #               Window Name                         #
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

    #                  Entries                                             #


        self.wentry=Entry(self.master,textvariable = self.WIDTH)
        self.hentry=Entry(self.master,textvariable = self.HEIGHT)
        self.scaleentry=Entry(self.master,textvariable = self.SCALE)
        self.octavesentry=Entry(self.master,textvariable = self.OCTAVES)
        self.persistanceentry=Entry(self.master,textvariable = self.PERSISTANCE)
        self.lacunarityentry=Entry(self.master,textvariable = self.LACUNARITY)

    #                       Labels                                      #


        self.WidthEnter = Label(self.master, text="Width: ")
        self.HeightEnter = Label(self.master, text="Height: ")
        self.ScaleEnter = Label(self.master, text="Scale: ")
        self.OctavesEnter = Label(self.master, text="Octaves: ")
        self.PersistanceEnter = Label(self.master, text="Persistance: ")
        self.LacunarityEnter = Label(self.master, text="Lacunarity: ")
        self.LacunarityEnter = Label(self.master, text="Lacunarity: ")

        #                    Buttons                                    #


        self.nmapsubmitbutton=Button(self.master,text="Submit",command=self.StartNoiseMap)

    #                  SetNoiseMap widgets                                #

    #                  ShowNoiseMap widgets                                #
        self.ColorMapButton=Button(self.master,text="Color Map",command=self.ColorNoiseMapSet)

    #                  ShowNoiseMap widgets                                #


    #                  ColorNoiseMap widgets                                #

        self.White=Entry(self.master,textvariable = self.White)
        self.Grey=Entry(self.master,textvariable = self.Grey)
        self.Green=Entry(self.master,textvariable = self.Green)

        self.WhiteEnter = Label(self.master, text="White color end: ")
        self.GreyEnter = Label(self.master, text="Grey color end: ")
        self.GreenEnter = Label(self.master, text="Green color end: ")


    #                  ColorNoiseMap widgets                                #

        self.ColorMapButtonStart=Button(self.master,text="Color Map",command=self.StartColorMap)

    def SetNoiseMap(self):
    #    All the widgets gridded for inputting values for NoiseMap.py's NoiseMapGenerator

        self.wentry.grid(row=0,column=1)
        self.hentry.grid(row=1,column=1)
        self.scaleentry.grid(row=2,column=1)
        self.octavesentry.grid(row=3,column=1)
        self.persistanceentry.grid(row=4,column=1)
        self.lacunarityentry.grid(row=5,column=1)
        self.WidthEnter.grid(row=0,column=0)
        self.HeightEnter.grid(row=1,column=0)
        self.ScaleEnter.grid(row=2,column=0)
        self.OctavesEnter.grid(row=3,column=0)
        self.PersistanceEnter.grid(row=4,column=0)
        self.LacunarityEnter.grid(row=5,column=0)
        self.nmapsubmitbutton.grid(row = 7, column = 0)


    def StartNoiseMap(self):
    #Creates noise map from NoiseMap.py, which outputs an image file for ShowNoiseMap to use
        self.width  = self.wentry.get()
        self.height = self.hentry.get()
        self.scale  = self.scaleentry.get()
        self.octaves = self.octavesentry.get()
        self.persistance = self.persistanceentry.get()
        self.lacunarity = self.lacunarityentry.get()
        self.noisemap = NewNoiseMap.NoiseMapGenerator(self.width,self.height,self.scale,self.octaves,self.persistance,self.lacunarity)
        self.noisemap.StartMap()
        self.ShowNoiseMap()

    def ShowNoiseMap(self):
    # Makes a tkimage for showing the noisemap on the tkinter window
        self.ClearWidgets()
        self.img = Image.open("NoiseMap.png")
        self.tkimg = ImageTk.PhotoImage(self.img)
        self.noisemapimage = Label(self.master, image = self.tkimg)
        self.noisemapimage.grid(row=0,column=0)
        self.ColorMapButton.grid(row= 1,column =0 )

    def ColorNoiseMapSet(self):
        self.ClearWidgets()
        self.WhiteEnter.grid(row=0,column=1,sticky="N")
        self.GreyEnter.grid(row=0,column=1)
        self.GreenEnter.grid(row=0,column=1,sticky = "S")
        self.White.grid(row=0,column=2,sticky="N")
        self.Grey.grid(row=0,column=2)
        self.Green.grid(row= 0,column=2,sticky="S")
        self.ColorMapButtonStart.grid(row=0,column=3)


    def StartColorMap(self):
        self.WhiteNum = self.White.get()
        self.GreyNum = self.Grey.get()
        self.GreenNum = self.Green.get()
        self.Coloredmap = colormap.ColorMap(self.WhiteNum,self.GreyNum,self.GreenNum)
        self.noisemapimage.grid_forget()
        self.Coloredmap.Start()
        self.ShowColorMap()

    def ShowColorMap(self):
        self.ClearWidgets()
        self.img = Image.open("ColorMap.png")
        self.tkimgcolor = ImageTk.PhotoImage(self.img)
        self.colornoisemapimage = Label(self.master, image = self.tkimgcolor)
        self.colornoisemapimage.grid(row=0,column=0)



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
        self.nmapsubmitbutton.grid_forget()
        self.White.grid_forget()
        self.Grey.grid_forget()
        self.Green.grid_forget()
        self.WhiteEnter.grid_forget()
        self.GreyEnter.grid_forget()
        self.GreenEnter.grid_forget()
        self.ColorMapButton.grid_forget()
        self.ColorMapButtonStart.grid_forget()



root= Tk()

root.geometry("800x600")
app = Window(root)

app.mainloop()
