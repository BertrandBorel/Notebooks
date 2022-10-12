# fonction pour générer une liste contenant des nombres aléatoires
# l'utilisateur peut choisir :
    # - le nombre d'éléments dans la liste
    # - la longeur de la liste

# Renvoie les éléments classés par ordre décroissant d'apparition

# Importations
from random import randint
from collections import Counter

# fonction 
def generate_random_list(number_of_elements, len_of_list):
    mylist = [randint(0, number_of_elements) for x in range(1, len_of_list)]
    print(mylist)
    most = Counter(mylist)
    print(most)

# appel de la fonction
generate_random_list(30, 20)
# produit ici une liste de 20 nombres allant chacun de 0 à 30




