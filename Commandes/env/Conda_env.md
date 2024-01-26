# Environnements virtuels avec Conda


## 1- Création d'un environnement virtuel :
`conda create --name myenv`

Avec une version particulière de python :
`conda create -n myenv python=3.9`

Idem mais avec d'autres packages :
`conda create -n myenv python=3.9 scipy=0.17.3 astroid babel`

## 2- Lister les packages de l'environnement
`conda env list`

## 3- Activer l'environnement
`conda activate myenv`

## 4- Obtenir des informations sur les environnements virtuels
`conda info --envs ou conda env list`

## 5- Lister les packages d'un environnement
`conda list`

Sans être dans l'environnement :
`conda list -n myenv`

Pour voir un package particulier :
`conda list -n myenv pmy_package`

## 6- Désactiver un environnement
`conda deactivate nom_env`

## 7- Supprimer un environnement
`conda env remove --name env_test`
