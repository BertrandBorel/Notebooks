# Afficher du texte avec Tkinter

import tkinter as tk

# création de la fenêtre
root = tk.Tk()

my_text = tk.Text(root, height=2, width=30)
my_text.pack()

# insertion du texte
my_text.insert(tk.END, "Ceci est une phrase de test")


# lancement de l'application
tk.mainloop()