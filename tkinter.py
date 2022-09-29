from tkinter import *

#Tk
root = Tk()
root.title("Hola mundo")
#root.iconbitmap("hola.ico") para cambiar el icono pero se debe tener la imagen
#root.resizable(False, True) #(Width,Height) Cambiar el tamaño de la ventana
root.config(cursor = "arrow")
root.config(bg = "blue")
root.config(bd = 15)
root.config(relief = "ridge")

#Frames
frame = Frame(root, width = 480, height = 300)
#frame.pack(side = "top", anchor="w") #bottom #left #top
frame.pack(fill = "x")
#fram.pack(fill = "y", expand = 1) #Para expandir en alto
frame.pack(fill = "both", expand = 1)
frame.config(cursor = "pirate")
frame.config(bg = "lightblue")
frame.config(bd = 30)
frame.config(relief = "sunken")


#frame.config(width = 480, height = 300) Se pueden declaras los valores a la hora de crear el frame como arriba

#Label

label = Label(frame, text = "Hola Mundo")
label.pack()

root.mainloop()




