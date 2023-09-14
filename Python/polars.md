# Polars


## Création d'un dataframe

df = pl.DataFrame(
    {
    "colonne1": ["element1", "element2", "element3"],
    "colonne2": [1, 5, 6],
    "colonne3": ["element1", "element2", "element3"],
    "colonne4": [True, False, False],
    }
).with_row_count("rn") # index personnalisé "rn"
print(df)

# sélectionner une colonne
colonne = df.select(pl.col("colonne2"))
print(colonne)

## sélectionner toutes les colonnes
out = df.select(pl.all())
print(out)
ou : out = df.select(pl.col("*"))

## sélectionner une partie des colonnes
out = df.select(pl.col("*").exclude("colonne1", "colonne3"))
print(out)

### En excluant les int :
out = df.select(pl.col("*").exclude(pl.Int64))
print(out)


### idem avec une regex :
Note : la regex doit commencer par ^ et finir par $
out = df.select(pl.col("^.*(1|3).*$"))
print(out)

### idem en sélectionnant le type de données (qu'on exclues)
out = df.select(pl.col(pl.Int64, pl.Boolean))
print(out)

#### idem mais en conservant qu'une ligne :
out = df.select(pl.col(pl.Int64, pl.Boolean).n_unique())
print(out)

## Ne conserver qu'un certain type :
import polars.selectors as cs
out = df.select(cs.boolean())
print(out)

## sélectionner les colonnes numériques sauf la première (l'index)
import polars.selectors as cs
out = df.select(cs.numeric() - cs.first())
print(out)

## sélectionner par le nom et le type non-numérique
import polars.selectors as cs
out = df.select(cs.by_name("rn") | ~cs.numeric())
print(out)

