# Commandes GIT

## Configuration
- `git config [--local|--global|--system]<clé><valeur> `

Exemple :
- `git config --global user.name 'NAME'`
-`git config --global user.email my_email@email.com`

Récupérer le nom :
- `git config user.name`

## Commandes
- `git init`
- `git status`
- `git add file_name`
- `git commit -m 'my_message`
- `git push origin main`

## Connexion au repo Github
- `git remote add origin PATH.git'` pour une première connexion

## Branches 
- `git branch` : affiche les branches
- `git branch NAME` : création d'une branch NAME
- `git checkout NAME` : déplacement vers la branche NAME
- `git checkout -b NAME` : création et déplacement vers la branche NAME
- `git branch -f NAME HEAD~3` : force la branche NAME à remonter de 3 commits parents
- **Merge :** Fusionne deux branches avec `git merge NAME`
- supprimer une branche : `git branch -d NAME`
- suppresion forcée : `git branch -D NAME`
- supprimer une branche du dépôt distant : `git push origin --delete NAME`
- `git rebase branch1 branch2` : déplacer la branche 2 sur la branche 1

## Voir les modifications effectuées
- `git log`

## Savoir si le dépôt local est lié à un dépôt distant
- `git remote -v`    
(sinon : voir Connexion au repo Github)

## Enregistrer le token (pour éviter de futures identifications)
- `git config --global credential.helper store`

## Graphe des commits
- `git log --oneline --graph --all`

## Tags (identifier un commit)
- `git tag` : liste les tags
- `git tag [TAG]` : tag le dernier commit
- `git tag -a [TAG] [HASH] -m "message` : tag un commit précis
- `git tag [TAG] [HASH]` : créer rapidement un tag
- `git show [TAG]` : montre le commit en question
- `git push origin [TAG]` : push d'un commit précis
- `git push --tags`: pousser tous les tags nommés
- `git describe <ref>` : décrire un tag (ou une branche ou un commit)
    - résultat : `<tag>_<numCommits>_g<hash>` soit tag>le nombre de commits avec le tag>le hash/identifiant du commit décrit

## HEAD :
- `git checkout HEAD^` : déplace le HEAD d'un niveau
- `git checkout HEAD~x` : déplace le HEAD de x niveau

## Annuler des changements (`reset` et `revert`)
- `git reset HEAD~1` : annule le dernier commit (locale)
- `git revert HEAD` : annule le dernier commit en créant un nouveau commit (remote)

## Déplacer son travail
- `git cherry-pick <Commit1> <Commit2> <...>` : copie un ou plusieurs commits
- `git rebase -i HEAD~x` : rebase interactif de x niveau (détruit l'historique)

## Modifier un commit
- `git commit --amend` : change le dernier commit sans créer de nouveau commit

## Conserver des changements
- `git stash` : conserve changements dans un fichier
- `git stash pop` : récupérer les changements

## Régler les conflits avec un dépôt distant
- `git pull --rebase` : récupère les commits du dépôt distant et les ajoute