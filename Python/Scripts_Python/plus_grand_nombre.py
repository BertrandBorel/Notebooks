# l'utilisateur rentre 3 nombres... :
nombre_1 = int(input("Entrez un premier nombre : "))
nombre_2 = int(input("Entrez un deuxième nombre : "))
nombre_3 = int(input("Entrez un troisième nombre : "))

# ... et l'on renvoit le plus grand d'entre eux :
if nombre_1 > nombre_2 :
    if nombre_1 > nombre_3 :
        print(nombre_1, "est le plus grand des nombres.")
    else :
        print(nombre_3, "est le plus grand des nombres.")
else : 
    if nombre_2 > nombre_3 :
        print(nombre_2, "est le plus grand des nombres.")
    else :
        print(nombre_3, "est le plus grand des nombres.")