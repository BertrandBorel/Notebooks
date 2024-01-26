# Créer un environnement virtuel sous Jupyter Notebook

## Etapes :
### 1- Ouvrir une fenêtre de terminal Anaconda Prompt.
### 2- Saississez la commande suivante :
`conda create -n nom_de_lenvironnement python=3 anaconda=5.2.0`

Ce qui permet de créer un nouvel environnement avec le nom désiré, utilsant ici des versions particulières de Python/Anaconda.

### 3- Activation de l'environnement virtuel :
`activate nom_de_lenvironnement`

Sous Linux/Mac :
`source activate nom_de_lenvironnement`

### 4- Installation des packages désirés.
### 5- Lancement de Jupyter Notebook :
Il démarre dans un environnement spécifique.

## Commandes
### Création : `conda create -n myenv`

### Activation : `conda activate myenv`

### Désactivation : `conda deactivate`

### Lister les environnements virtuels : `conda env list`

### Suppression : `conda env remove -n myenv`

### Installation du noyau Jupyter dans l'environnement virtuel
`ipython kernel install --user --name=myenv`

Puis aller sur Jupyter, puis sur Kernel/Change kernel où s'affiche les différents noyaux.

### Suppression du noyau
`jupyter-kernelspec uninstall venv`
