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


## Commentaire : 
`/*` et `*/`

## Eléments :
- `font-size` : taille de la police (en **px**)
- `text-align` : alignement du texte
- `line-height` : espacement entre les lignes
- `letter-spacing` : espacement horizontal entre les caractères d'un texte
- `width`, `height` : largeur, hauteur
- `background-color` : la couleur d'arrière-plan
- `text-shadow` : ajouter une ombre au texte
- `display` : contrôle comment un élément HTML est rendu dans le flux du document. Elle définit le comportement de l'élément en termes de mise en page. 
    Les valeurs courantes pour display comprennent :
      - *block* : L'élément occupe toute la largeur disponible et commence sur une nouvelle ligne.
      - *inline* : L'élément occupe uniquement l'espace nécessaire, sans sauter à une nouvelle ligne.
      - *inline-block* : L'élément est en ligne, mais peut avoir des marges et des rembourrages, comme un élément de bloc.
      - *none* : L'élément n'est pas affiché et n'occupe pas d'espace dans la mise en page.


## Pseudo-classes 
Les **pseudo-classes** en CSS sont des sélecteurs spéciaux qui permettent de **cibler des éléments HTML en fonction d'états ou de relations spécifiques**, plutôt que simplement en fonction de leur type ou de leurs attributs.  
Les pseudo-classes sont précédées par deux-points (:) dans une règle CSS.  
Les pseudo-classes permettent d'ajouter de l'interactivité et de personnaliser l'apparence des éléments HTML en fonction des actions de l'utilisateur, améliorant ainsi l'expérience utilisateur et la convivialité d'un site web.

### Utilisations courantes :
- Créer des styles au survol de liens ou de boutons.
- Modifier l'apparence des champs de formulaire lorsque l'utilisateur les sélectionne.
- Créer des mises en page réactives en utilisant :nth-child() pour cibler des éléments spécifiques.
- Cibler des éléments spécifiques au sein d'une liste.

### `:hover`
#### Description : 
La pseudo-classe `:hover` est activée lorsque le curseur de la souris survole un élément HTML. **Elle permet de modifier le style de l'élément lorsque l'utilisateur passe sa souris dessus**.

#### Utilisations courantes :
- Changement de couleur, de fond ou d'opacité d'un bouton lorsqu'il est survolé.
- Afficher des informations contextuelles lorsqu'un lien est survolé.
- Animer des éléments lorsqu'ils sont survolés.

#### Exemple :
```
a:hover {
    color: #ff0000; /* Le texte devient rouge au survol */
}
```

### `:focus`
#### Description : 
La pseudo-classe `:focus` est activée lorsque l'élément reçoit le focus, généralement par le biais de la tabulation (tabulation clavier) ou d'un événement similaire. Elle est particulièrement importante pour l'accessibilité des sites web.

#### Utilisations courantes :
- Mettre en évidence les champs de formulaire lorsqu'ils sont sélectionnés.
- Créer des menus déroulants accessibles avec le clavier.

#### Exemple :
```
input:focus {
    border-color: #007bff; /* Le champ de saisie a une bordure bleue lorsqu'il est sélectionné */
}
```

## Container 
En CSS, le terme "container" n'a pas de signification spécifique définie par les spécifications CSS. Cependant, il est couramment utilisé dans le développement web pour faire référence à **un élément HTML qui agit comme un conteneur pour d'autres éléments**. La notion de conteneur est davantage une convention de nommage qu'une propriété CSS spécifique.

Un "container" est généralement un élément HTML, tel qu'une `<div>`, qui est utilisé pour regrouper d'autres éléments, souvent dans le but de définir une mise en page ou un cadre pour le contenu. Le conteneur peut avoir des styles CSS qui définissent des marges, des rembourrages, des largeurs, des hauteurs, des arrière-plans, des bordures..., qui affectent son contenu.

### Exemple :
```
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Mon Conteneur</h1>
        <p>Ceci est un exemple de conteneur en CSS.</p>
    </div>
</body>
</html>
```

Dans cet exemple, la classe CSS `.container` est appliquée à la `<div>` qui entoure le titre `<h1>` et le paragraphe `<p>`. La classe `.container` définit un conteneur avec une largeur de 80%, des marges automatiques pour le centrer horizontalement, un rembourrage de 20px, et une bordure de 1px.   
Cela permet de créer un cadre autour du contenu et de le centrer dans la fenêtre du navigateur.  