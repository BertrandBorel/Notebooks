# Fonction : Redimensionner une image avec Tkinter
# ____________________________________________________________

# Importations
from tkinter import *
from PIL import Image, ImageTk
 

# Création de la fenêtre
root = Tk()

# fonction resize() les images :
def redimensionner(image):
    my_img = Image.open(image)
    resize_image = my_img.resize((500, 200))
    img = ImageTk.PhotoImage(resize_image)

    return img
 

# Image :
img = redimensionner("image.jpg") 

# Création du label
label1 = Label(image=img)

# Ajout de l'image
label1.image = img
label1.pack()
 
# Lancement de l'application
root.mainloop()