# Commandes Linux 
<br>

## APT (Advanced Package Tool)
### MAJ :
- `sudo apt update`
- `sudo apt upgrade`

- Full command :  `sudo apt update && sudo apt full-upgrade -y`

- `apt-get update` : mise à jour du cache des paquets puis `apt-get upgrade`
- `apt-get install` : installer un paquet
- `apt-get remove nom_paquet` : supprimer un paquet
- `apt-get autoremove  nom_paquet` : idem mais supprime aussi les dépendances inutiles

#### Lister les packages qui peuvent être mis à jour
`apt list --upgradable`

#### Mettre à jour un package particulier :
`sudo apt-get install --only-upgrade <packagename>`

### Vérifier la version d'Ubuntu
`lsb_release -a`

<br>

## Visualisation des fichiers

- `ls` : Afficher les fichiers du dossier courant

- `ls nom_dossier` : Afficher les fichiers d'un dossier

- `ls -a` : Afficher tous les fichiers (mêmes cachés)


### Afficher le contenu d'un fichier
`cat nom_fichier`

- `cat -n nom_fichier ` : affiche les numéros de ligne

### Afficher le fichier page par page
`less nom_fichier`

### Afficher une ligne d'un fichier
`echo nom_fichier`

### Visualiser le contenu d'un fichier
`more nom_fichier`

### Afficher le début d'un fichier
`head nom_fichier`

### Afficher la fin d'un fichier
`tail nom_fichier`

### Supprimer un fichier 
`rm fichier`

- `rm -i fichier` : demande une confirmation pour supprimer.
- `rm -f fichier`: force la suppression.

### Créer un raccourci pour un fichier
`ln -s fichier1 fichier2`
<br>

## Dossier 

### Créer un dossier
`mkdir nom_dossier`

- `mkdir -p dossier/sous_dossier/encore` : permet de créer des dossiers intermédiaires avec `-p`

### Supprimer un dossier
- `rmdir nom_dossier`
- `rm -r [nom]` = supprime dossier avec tout son contenu
- Si le dossier est protégé utiliser : `rm -rf [nom]`
- Si cela ne fonctionne pas, utiliser : `sudo rm -r -f [nom]`

<br>

## Fichier 

### Créer un fichier
`touch nom_fichier`

### Copier un fichier
`cp source destination`

- `cp -R dossier mon_dossier` : copie dossier et tous ses éléments sous le nom 'mon_dossier'.
- `cp *.jpg mon_dossier` : permet de copier tous les fichiers `jpg` dans un sous dossier.
- `cp code* mon_dossier` permet de copier tous les fichiers dont le nom commence par 'code'.

### Déplacer un fichier
`mv source destination`

### Renommer un fichier
`mv ancien_nom.file nouveau_nom.file`

### Déplacer et renommer un fichier 
`mv fichier mon_dossier/nouveau_fichier`

## Rechercher des fichiers
- `locate mon_fichier`
- `find -name "logo.png"` : recherche par nom 

## Déplacement

### Commande `pwd`
Trouve le chemin du répertoire de travail dans lequel on se trouve. La commande retournera un chemin absolu (complet), qui est en fait un chemin de tous les répertoires qui commence par une barre oblique (/). Un exemple de chemin absolu est /home/utilisateur.

### Se déplacer dans un dossier
`cd`

### Reculer d'un dossier
`cd ..`

### Retourner au répertoire précédent
`cd -`

### Revenir à la racine
`cd ~`

<br>

## Terminal 

### Voir l'historique du terminal
`history`

### Rechercher une commande dans le terminal 
`Ctrl + R`

### Effacer le contenu de la console
`Ctrl + L`
<br>
Ou commande `clear`

### Quitter la console 
`Ctrl + D`
<br>
Ou commande `exit`

### Remonter les messages dans la console
`Shift + PgUp` et `Shift + PgDown`

### Ramener le curseur au début de la commande
`Ctrl + A`

### Déplacer le curseur à la fin de la commande
`Ctrl + E`

### Supprimer ce qui est à gauche du curseur 
`Ctrl + U`

### Supprimer ce qui est à droite du curseur 
`Ctrl + K`

### Supprimer le premier mot situé à gauche du curseur
`Ctrl + W`

## `Ctrl + Y` : 
Si vous avez supprimé du texte avec une des commandes `Ctrl + U`, `Ctrl + K` ou `Ctrl + W` alors le raccourci « collera » le texte qui vient d'être supprimé, comme un couper-coller.

## Autres commandes

### Lire un fichier ligne par ligne
`while read line; do echo $line; done < movies.json`

### Ecrire plusieurs lignes dans un fichier
#### Methode 1 :
```
echo "line 1 content" >> myfile.txt
echo "line 2 content" >> myfile.txt
echo "line 3 content" >> myfile.txt
```
#### Methode 2 :
```
echo "line 1 content
line 2 content
line 3 content" >> myfile.txt
```
#### Methode 3 :
```
cat >> greetings.txt <<EOL
line 1 content
line 2 content
line 3 content
EOL
```
### Accéder aux fichiers Ubuntu dans l'explorer de Windows (avec WSL)
`\\wsl$`

### Lancer VSCode
`code .`
