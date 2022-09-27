liste = [404, 8, 22, 310, 5] 
somme = 0
i = 0

# tri de la liste :
tri = liste.sort()
print("Voici la liste triée :", liste)

# addition de la liste :
while i < len(liste):
    somme = somme + liste[i]
    i = i + 1
print("La somme est de :", somme)

# avec la fonction sum():
# print(sum(liste))
