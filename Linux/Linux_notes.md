## paramètre court

un tiret + une seule lettre 

#### Exemple :
`commande -d`

#### Plusieurs paramètres : 
`commande -d -a -U -h`

ou :

`commande -daUh`


## paramètre long 

deux tirets + plusieurs lettres

#### Exemple :
`commande --parametre`

#### Plusieurs paramètres :
`commande --parametre1 --parametre2`


Il est également possible de combiner les paramètres courts/longs : `commande -daUh --autreparametre` .


## Chercher dans un fichier avec `grep`

`grep texte nomfichier`

Paramètres :
   - `-i` : ne pas tenir compte de la casse
   - `-n` : connaître les n° des lignes
   - `-v` : ignorer un mot
   - `-r` : rechercher dans tous les fichiers/sous-dossiers

Il est également possible de chercher avec une regex : `grep -E my_regex my_file`

## Expression régulière

|Caractère spécial|Signification
|---|---
`.`|Caractère quelconque
`^`|Début de ligne
`$`|Fin de ligne
`[]`|Un des caractères entre les crochets
`?`|L'élément précédent est optionnel (peut être présent 0 ou 1 fois)
`*`|L'élément précédent peut être présent 0, 1 ou plusieurs fois
`+`|L'élément précédent doit être présent 1 ou plusieurs fois
`()`|Groupement d'expressions


## Autres commandes :
   - `sort`: tirer les lignes
   - `wc` : compter le nombre de lignes
   - `uniq` : supprimer les doublons
   - `cut` : couper une partie du fichier
