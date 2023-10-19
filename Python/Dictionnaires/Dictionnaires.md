## Récupérer la valeur d'une clé :
`value = dictionary[key]`

**Privilégier `get` pour éviter les erreurs (si une clé n'existe pas) :**
`value = dictionary.get(key)`

Il est également possible d'utiliser des valeurs par défauts. Si la valeur n'est pas trouvée, alors la valeur par défaut est renvoyée :

`value = dictonary.get(key, default_value`)
