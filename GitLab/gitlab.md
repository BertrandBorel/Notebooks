# <center> Commandes GitLab </center>

## Création d'une branche en locale puis pusher 
- Initialisation d'un référentiel Git local : `git init`
- Ajout de fichier : `git add .`
- Effectuer un commit : `git commit -m "Initial commit`
- Création d'une branche en local : `git branch new_branch`
- Basculement vers la branche : `git checkout new_branch`
- Associer le référentiel local à GitLab : Pour lier votre référentiel Git local à votre projet sur GitLab, vous devrez ajouter une télécommande Git. Vous trouverez l'URL de la télécommande Git sur la page de votre projet GitLab. `git remote add origin URL_de_votre_projet_GitLab
`
- Pousser la nouvelle branche sur gitlab : `git push -u origin dev`

  ## Mise en ligne des applications locales sur GitLab
  - Initialiser un référentiel Git local :
  ```markdown
  git init 
  git add .  
  git commit -m "Premier commit"  
  ```
