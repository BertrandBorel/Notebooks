# <center>Tailwind css </center>

## FLEX :
Définit un conteneur comme flexible = utilisé pour rendre la page *responsive*.  
La classe "flex" elle-même n'est généralement pas suffisante pour créer une mise en page flexible. Vous devrez également utiliser d'autres classes pour spécifier comment les éléments enfants du conteneur flex doivent se comporter. Par exemple, vous pouvez utiliser "flex-grow" pour indiquer à un élément de prendre autant d'espace que possible, ou "flex-shrink" pour lui permettre de réduire sa taille si nécessaire.

**Exemple :**

```
<div class="flex">
  <div class="flex-1">Élément 1</div>
  <div class="flex-1">Élément 2</div>
  <div class="flex-1">Élément 3</div>
</div>
```

### Classes :
- **flex**: Définit un conteneur comme un conteneur flexible.
- **flex-1, flex-2, flex-3,...** : Contrôle la distribution de l'espace entre les éléments enfants. Par exemple, flex-1 signifie que l'élément prend autant d'espace que possible, tandis que flex-2 signifie que l'élément prendra deux fois moins d'espace que ceux avec flex-1.
- **flex-grow**: Indique que l'élément doit augmenter en taille pour remplir l'espace disponible.
- flex-shrink**: Indique que l'élément peut réduire sa taille si nécessaire pour s'adapter à l'espace disponible.
- **flex-initial**: Réinitialise les propriétés de flex-grow et flex-shrink à leurs valeurs par défaut.
- **flex-auto**: Configure l'élément pour augmenter en taille si l'espace est disponible, mais il peut également réduire sa taille.
- **flex-none**: Empêche l'élément de grandir ou de rétrécir.
- **flex-row**, flex-row-reverse, flex-col, flex-col-reverse: Contrôle la direction des éléments flex (ligne ou colonne) et leur sens.
- **flex-wrap**, flex-nowrap, flex-wrap-reverse: Contrôle le comportement de l'enroulement des éléments flex lorsque l'espace est insuffisant.
- **items-start**, items-center, items-end,... : Contrôle l'alignement vertical des éléments enfants à l'intérieur du conteneur flex.
- **justify-start**, justify-center, justify-end,... : Contrôle l'alignement horizontal des éléments enfants à l'intérieur du conteneur flex.
- **self-start**, **self-center**, **self-end**,... : Contrôle l'alignement vertical de l'élément lui-même à l'intérieur du conteneur flex.
- **order-1**, **order-2**,... : Modifie l'ordre des éléments à l'intérieur du conteneur flex.


## PADDING :
Le padding (rembourrage en français) est un espace ajouté à l'intérieur d'un élément HTML.  
Il est utilisé pour définir l'espace entre le contenu de l'élément et ses bords. Le padding est généralement utilisé pour améliorer la mise en page en ajoutant de l'espace autour du contenu, ce qui peut rendre le texte et d'autres éléments plus lisibles et esthétiques.

### Classes :
- **p-{size}** : Ajoute un padding de taille spécifiée de manière égale sur les quatre côtés de l'élément. Par exemple, p-4 ajoutera un padding de 1rem (16 pixels) autour de l'élément.

- **py-{size}** : Ajoute un padding de taille spécifiée sur les côtés supérieur et inférieur de l'élément, tout en maintenant un padding de zéro sur les côtés gauche et droit. Par exemple, py-6 ajoutera un padding de 1.5rem (24 pixels) en haut et en bas de l'élément.

- **px-{size}** : Ajoute un padding de taille spécifiée sur les côtés gauche et droit de l'élément, tout en maintenant un padding de zéro sur les côtés supérieur et inférieur. Par exemple, px-8 ajoutera un padding de 2rem (32 pixels) à gauche et à droite de l'élément.

- **pt-{size}**, **pr-{size}**, **pb-{size}**, **pl-{size}** : Ces classes ajoutent du padding à un côté spécifique de l'élément (haut, droit, bas ou gauche). Par exemple, pt-3 ajoutera du padding en haut de l'élément.

## MARGIN :
La marge (margin en anglais) fait référence à l'espace ajouté autour d'un élément HTML.  
Contrairement au padding, qui ajoute de l'espace à l'intérieur de l'élément, la marge crée de l'espace autour de l'élément, séparant ainsi cet élément d'autres éléments environnants.

### Classes :
- **m-{size}** : Ajoute une marge de taille spécifiée de manière égale sur les quatre côtés de l'élément. Par exemple, m-4 ajoutera une marge de 1rem (16 pixels) autour de l'élément.
- **my-{size}** : Ajoute une marge de taille spécifiée sur les côtés supérieur et inférieur de l'élément, tout en maintenant une marge de zéro sur les côtés gauche et droit. Par exemple, my-6 ajoutera une marge de 1.5rem (24 pixels) en haut et en bas de l'élément.
- **mx-{size}** : Ajoute une marge de taille spécifiée sur les côtés gauche et droit de l'élément, tout en maintenant une marge de zéro sur les côtés supérieur et inférieur. Par exemple, mx-8 ajoutera une marge de 2rem (32 pixels) à gauche et à droite de l'élément.
- **mt-{size}**, **mr-{size}**, **mb-{size}**, **ml-{size}** : Ces classes ajoutent de la marge à un côté spécifique de l'élément (haut, droit, bas ou gauche). Par exemple, mt-3 ajoutera de la marge en haut de l'élément.
