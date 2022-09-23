# fonction map

nombres = [1, 2, 3, 4]

def fonction_test(nombre):
    calc = nombre * nombre
    return calc

# Voir les éléments avec une boucle
resultat_1 = map(fonction_test, nombres)
for x in resultat_1 :
    print(x)

# conversion en liste
resultat_2 = list(map(fonction_test, nombres))
print(nombres)