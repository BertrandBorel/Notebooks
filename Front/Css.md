# <center> CSS </center> 

Un document **CSS** (***Cascading Style Sheet***) est un fichier ou une partie d'une page web qui définit la présentation et le style des éléments HTML. Un document CSS suit une structure de règles bien définie. Voici un aperçu de cette structure de règles CSS :

- **Sélecteur** : Le sélecteur est le premier élément d'une règle CSS. Il définit quel élément HTML ou groupe d'éléments sera stylé. Les sélecteurs peuvent être des balises HTML, des classes, des IDs, des attributs, des pseudo-classes, ou des combinaisons de ces éléments. Par exemple :
  - *Sélecteur de balise* : **p** cible tous les paragraphes.
  - *Sélecteur de classe* : **.maClasse** cible tous les éléments ayant la classe "maClasse".
  - *Sélecteur d'ID* : **#monId** cible un élément avec l'ID "monId".
  - *Sélecteur d'attribut* : **[type="text"]** cible les éléments avec l'attribut "type" égal à "text".
- **Propriété** : La propriété est l'aspect que vous souhaitez styliser, comme la couleur, la taille de la police, la marge, la bordure, etc.

- **Valeur** : La valeur est la valeur assignée à la propriété. Par exemple, pour la propriété color (couleur), la valeur pourrait être red (rouge) ou #00ff00 (vert en notation hexadécimale).

- **Déclaration** : La combinaison d'une propriété et d'une valeur constitue une déclaration. Les déclarations sont séparées par des points-virgules.

## Structure : 

```
sélecteur{  
        propriété : valeur ;  
        [ propriété + valeur ] = déclaration ;  
        }
```
