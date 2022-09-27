def get_vowels_numbers(word):
	    # créer un compteur de voyelles
	    nb_vowels = 0
	
	    # pour chaque lettre du mot vous verifiez s'il s'agit d'un voyelle
	    for letter in word:
	        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
	            # on ajoute un au compteur
	            nb_vowels += 1
	
	    # à la fin de la fonction, vous allez renvoyer le compteur
	    return nb_vowels
	
	
word = input("Entrez un mot : ")
vowels_count = get_vowels_numbers(word)
print("Il y a", vowels_count, "voyelles dans le mot", word)