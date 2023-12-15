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

## Flux de redirection
- `>` : redirige dans un fichier et l'écrase s'il existe déjà ;
- `>>` : redirige à la fin d'un fichier et le crée s'il n'existe pas.
- `2>` : redirige les erreurs dans un fichier (s'il existe déjà, il sera écrasé)
- `2>>` : redirige les erreurs à la fin d'un fichier (s'il n'existe pas, il sera créé
- `2>&1` : Fusionner les sorties : redirige les erreurs au même endroit et de la même façon que la sortie standard.
- `<` : lire depuis un fichier : envoie le contenu d'un fichier à une commande
- `<<` : lire depuis le clavier progressivement : passe la console en mode saisie au clavier, ligne par ligne. Toutes ces lignes seront envoyées à la commande lorsque le mot-clé de fin aura été écrit
- `|` : chaîner les commandes

- ## Surveiller l'activité d'un système

- `ps` : liste statique des processus => 4 éléments : <br>
      - `PID` : n° d'identification du processus. <br>
      - `TTY` : nom de la console depuis laquelle a été lancé le processus.<br>
      - `TIME` : durée d'exécution du processus. Plus exactement, cela correspond à la durée pendant laquelle le processus a occupé le processeur depuis son lancement.<br>
      - `CMD` : le programme qui a généré ce processus.<br>
  <br>
- `ps -ef` : lister tous les processus
- `ps -ejH` : afficher les processus en arbre
- `ps -u UTILISATEUR` : lister les processus lancés par un utilisateur                                   
- `top` : liste dynamique des processus

### Commandes pour arrêter un processus
- `Ctrl + C` : arrêter un processus lancé en console
- `kill` : tuer un processus
- `killall` : tuer plusieurs processus

### Autres commandes
- `halt` : arrêter l'ordinateur
- `reboot` : redémarrer l'ordinateur
- `w` : indique quels utilisateurs sont sur la machine, ce qu'ils font et quelques autres statistiques comme la charge de travail de la machine et son uptime.

## Exécuter des programmes en arrière-plan

- `&` : lancer un processus en arrière-plan
- `nohup` : détacher le processus de la console
- `Ctrl + Z` : mettre en pause l'exécution du programme
- `bg` : passer le processus en arrière-plan
- `jobs` : connaître les processus qui tournent en arrière-plan
- `fg` : reprendre un processus au premier plan
- `screen` : plusieurs consoles en une. Il permet d'ouvrir plusieurs consoles virtuelles au sein d'une seule et même console, et donc d'exécuter facilement plusieurs processus en parallèle.

## Exécuter une commande plus tard
-  `at` : Exécuter une commande à une heure précise => `at 15:25`
-  `at now` : Exécuter une commande après un certain délai => `at now +10 minutes/weeks/days...`

## Exécuter plusieurs commandes en 1
`touch fichier.txt; rm fichier.txt` => faire une pause : `touch fichier.txt; sleep 10; rm fichier.txt`

## `crontab` : exécuter une commande régulièrement
Permet de programmer des commandes pour une exécution régulière. Par exemple : tous les jours à 18 h 30, tous les lundis et mardis à 12 h, tous les 5 du mois, etc. On modifie la programmation avec `crontab -e`.

## Compresser des fichiers sous Linux

- `tar`: réunir les fichiers dans un seul gros fichier appelé archive
- compresser le gros fichier ainsi obtenu à l'aide de `gzip` ou de `bzip2`.

### Commandes :
- création d'une archive : `tar -cvf nom_archive.tar nom_dossier/`
   - `-c` : créer une archive tar ;
   - `-v` : afficher le détail des opérations ;
   - `-f` : assembler l'archive dans un fichier.
- `-tf` : afficher le contenu de l'archive sans l'extraire
- `-rvf` : ajouter un fichier
- `-xvf` : extraire les fichiers de l'archive
- Exemple de compression : `gzip tutoriels.tar`
- Décompression : `gunzip tutoriels.tar.gz`

## Transfert de fichiers
- `wget` permet de télécharger un fichier. (`--background` pour le faire en arrière-plan)
- Pour copier des fichiers d'un ordinateur à un autre, on `utilisescp`. Il fonctionne à l'aide de SSH, donc le transfert est sécurisé.
- On peut se connecter à un serveur FTP avec la commande `ftp` pour y télécharger et y envoyer des fichiers.
- Il existe une alternative sécurisée à FTP qui crypte les échanges grâce à SSH : `sftp`.
- `rsync` permet de synchroniser le contenu de deux dossiers sur un même ordinateur ou sur deux ordinateurs différents. Il est particulièrement utile pour effectuer des sauvegardes.
