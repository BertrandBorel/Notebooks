# Commandes Linux

## APT (Advanced Package Tool)

### MAJ :
- `sudo apt update`
- `sudo apt upgrade`

- Full command :  `sudo apt update && sudo apt full-upgrade -y`

#### Lister les packages qui peuvent être mis à jour
`apt list --upgradable`

#### Mettre à jour un package particulier :
`sudo apt-get install --only-upgrade <packagename>`

## Vérifier la version d'Ubuntu
`lsb_release -a`




## Visualisation des fichiers

### Afficher les fichiers du dossier cournat
`ls`

### Afficher les fichiers d'un dossier
`ls nom_dossier`

### Afficher tous les fichiers (mêmes cachés)
`ls -a`

### Afficher le contenu d'un fichier
`cat nom_fichier`

### Afficher une ligne d'un fichier
`echo nom_fichier`

### Visualiser le contenu d'un fichier
`more nom_fichier`

### Afficher le début d'un fichier
`head nom_fichier`

### Afficher la fin d'un fichier
`tail nom_fichier`

## Dossier 

### Créer un dossier
`mkdir nom_dossier`

### Supprimer un dossier
- `rmdir nom_dossier`
- `rm -r [nom]` = supprime dossier avec tout son contenu
- Si le dossier est protégé utiliser : `rm -rf [nom]`
- Si cela ne fonctionne pas, utiliser : `sudo rm -r -f [nom]`

## Fichier 

### Créer un fichier
`touch nom_fichier`

### Copier un fichier
`cp source destination`

### Déplacer un fichier
`mv source destination`

### Renommer un fichier
`mv ancien_nom.file nouveau_nom.file`



## Déplacement

### Commande `pwd`
Trouve le chemin du répertoire de travail dans lequel on se trouve. La commande retournera un chemin absolu (complet), qui est en fait un chemin de tous les répertoires qui commence par une barre oblique (/). Un exemple de chemin absolu est /home/utilisateur.

### Se déplacer dans un dossier
`cd`

### Reculer d'un dossier
`cd ..`

### Retourner au répertoire précédent
`cd -`


## Autres commandes !

### Voir l'historique du terminal
`history`



### Lire un fichier ligne par ligne
`while read line; do echo $line; done < movies.json`

### Ecrire plusieurs lignes dans un fichier
#### Methode 1 :
`echo "line 1 content" >> myfile.txt`

`echo "line 2 content" >> myfile.txt`

`echo "line 3 content" >> myfile.txt`

#### Methode 2 :
`echo "line 1 content`

`line 2 content`

`line 3 content" >> myfile.txt`

#### Methode 3 :
`cat >> greetings.txt <<EOL`

`line 1 content`

`line 2 content`

`line 3 content`

`EOL`

### Accéder aux fichiers Ubuntu dans l'explorer de Windows (avec WSL)
`\\wsl$`

### Lancer VSCode
`code .`
