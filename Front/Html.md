# <center> Html </center> 

## Structure d'un élément HTML

**1 élément** = `<balise ouvrante> CONTENU </balise fermante>`   
Les éléments peuvent avoir des **attributs** : `<p class="Attribut" > ...`

## Structure d'un document HTML

- `<html></html>` : l'élément racine.   
- `<head></head>` : conteneur pour le contenu qui n'est pas à afficher sur l'écran (mots-clés, CSS, description...).
- `<meta charset="utf-8">` : jeu de caractères utilisé pour le document.
- `<meta name="viewport" content="width=device-width">` : gère l'affichage.
- `<title></title>` : titre de la page, apparaît sur l'onglet.
- `<body></body>` : contenu affiché sur la page.

## Images 

`<img src="images/umage.png" alt="test image" />`

- `src` : source de l'image
- `alt` : texte alternatif

## Titres
6 niveaux, de  `<h1>` à `<h6>`

## Paragraphes
`<p>Exemple de paragraphe</p>`

## Listes
- listes non-ordonnées : l'ordre des éléments n'a pas d'importance (ex: *liste de courses*) => `<ul>`
- listes ordonnées : ordre important (ex: *recette de cuisine*) => `<ol>`
- chaque élément d'une liste est dans un élément `<li>`

## Liens
`<a href="url">texte de l'url</a>`

## Intégration du CSS dans l'HTML
`<link href="styles/style.css" rel="stylesheet" type="text/css" />`

## Balises Html 
- `<em>` : texte en italique;
- `<strong>` : gras
