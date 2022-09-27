# Ecrire une fonction mon_maximum qui prend en entrée une liste de valeurs et qui renvoie le maximum 
# ainsi que son indice dans la liste.


def maximum(a, b):
    if a > b :
        return a
    else:
        return b

valeur_1 = int(input("Entrez une valeur : "))
valeur_2 = int(input("Entrez une deuxième valeur : "))

print("La valeur maximale est", maximum(valeur_1, valeur_2))