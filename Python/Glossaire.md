## Décorateur

En Python, un décorateur est une fonction qui prend une autre fonction en entrée et renvoie une nouvelle fonction qui s'enveloppe autour de la fonction d'entrée. Les décorateurs sont utilisés pour ajouter des comportements à une fonction existante sans la modifier directement. Ils sont très utiles pour l'encapsulation de code et la modularité, en permettant de définir une logique générale qui s'applique à plusieurs fonctions.

Les décorateurs peuvent être utilisés pour :

- Ajouter ou changer des comportements d'une fonction sans la modifier directement.
- Ajouter des informations supplémentaires à une fonction, telle que la documentation ou les annotations.
- Imposer des contraintes supplémentaires sur les arguments d'une fonction.
- Ajouter du code avant et après l'exécution de la fonction, tels que les journaux et les statistiques.

Les décorateurs sont définis en utilisant le symbole @ suivi du nom du décorateur et peuvent être utilisés sur n'importe quelle fonction définie dans votre code


## Expressions régulières

Les expressions régulières ("regex") sont un ensemble de règles pour la reconnaissance et la manipulation de chaînes de caractères. En Python, les expressions régulières sont implémentées dans le module **re**.

Les expressions régulières sont utiles pour :

- La validation de données telles que les adresses e-mail, les numéros de téléphone, etc.
- La recherche et le remplacement de sous-chaînes dans des chaînes de caractères plus longues.
- La division de chaînes de caractères en parties plus petites selon des règles prédéfinies.

Les expressions régulières sont basées sur une syntaxe spéciale qui permet de décrire un ensemble de chaînes de caractères. Par exemple, l'expression `\d{3}-\d{2}-\d{4}` décrit un numéro de sécurité sociale américain.

En utilisant le module **re**, vous pouvez trouver des correspondances dans des chaînes de caractères en utilisant des expressions régulières et effectuer des opérations telles que la substitution de sous-chaînes, la division de chaînes en parties plus petites, etc
