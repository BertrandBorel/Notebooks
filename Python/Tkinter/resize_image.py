# Redimensionner une image avec Tkinter
# ____________________________________________________________

# Importations
from tkinter import *
from PIL import Image, ImageTk
 

# Création de la fenêtre
root = Tk()
 
# Ouverture de l'image
image = Image.open("image.jpg")
 
# Redimension : 
resize_image = image.resize((500, 200))
img = ImageTk.PhotoImage(resize_image)
 
# Création du label
label1 = Label(image=img)

# Ajout de l'image
label1.image = img
label1.pack()
 
# Lancement de l'application
root.mainloop()