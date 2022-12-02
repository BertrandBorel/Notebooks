# Afficher une image avec Tkinter
# ____________________________________________________________

# Importations
from tkinter import *
from PIL import Image, ImageTk


# Création de la fenêtre
root = Tk()
# root.maxsize(600, 400) = taille max de la fenêtre 

# image 
my_img = ImageTk.PhotoImage(Image.open("./test_images/image_10.JPG"))

# création d'un label avec l'image
my_label = Label(image=my_img)
my_label.pack()

# lancement de l'application
root.mainloop()