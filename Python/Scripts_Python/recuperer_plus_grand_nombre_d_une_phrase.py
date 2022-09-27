'''Le but de cet exercice est de prendre une phrase et de dire lequel de ses mots est 
le plus grand.
Pour cela on utilise la fonction split() pour transformer la variable txt en liste.
Puis on demande le max de txt :
key = len'''

# on entre la phrase qui devient une liste avec split ()
txt = input("Entrez une phrase : ").split()


# on récupère le plus grand nombre
print("Le mot le plus long est : ", max(txt, key = len))