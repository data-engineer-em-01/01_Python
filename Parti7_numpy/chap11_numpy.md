# Extraire des données

## 11. Extraire des données avec un opérateur

Vous pouvez utiliser des opérateurs de comparaison pour extraire des données d'un array; c'est très pratique lorsqu'on souhaite extraire uniquement une partie des données selon un critère :

```python
a = np.array([1, 2, 3, 4, 5, 6 ,7])
print(a[ a > 3])
# array([4, 5, 6, 7])
```

Vous pouvez utiliser l'opérateur modulo pour extraire des valeurs paires d'un array par exemple :

```python

a = np.array([9,100,7, 88, 90, 11, 2 ])

a[ a % 2 == 0]
# array([100,  88,  90,   2])

```

Extraire les nombres supérieurs à 2 :

```python

a = np.array([9,100,7, 88, 90, 11, 2 ])

b = a > 2
# array([
# True,  True,  True,  True,  True,  True, False], dtype=bool)

```

Puis il faut appliquer le mask (indexation avancée) :

```python

a[b]
# array([  9, 100,   7,  88,  90,  11])

```

Pour un tableau à deux dimensions :

```python

d = np.array([
    [ 1, 2, 3, 4, 5 ],
    [ 7, 8, 13, 14, 50 ],
    [ 9,89, 0, 78, 1],
    [ 11, 21, 37, 14, 107 ]
])

print(d > 10)

# Le mask appliqué retournera un tableau 1d avec les valeurs vérifiées par la condition
print( d[ d > 10 ])

```

Comparaison de deux tableaux Numpy :

```python

# Ou comparer deux array de même dimension
a = np.array([1, 2, 3, 4, 5, 6 ,7])
b = np.array([10, 20, 3, 4, 5, 6 ,7])
b > a
# array([ True,  True, False, False,
# False, False, False], dtype=bool)

# Vous pouvez appliquer le mask à un des deux tableaux
a[a>b]

```

Vous pouvez également compter avec un mask :

```python
np.sum( a > 2 )
```

En utilisant la méthode all de Numpy vous pouvez appliquer une comparaison totale sur les valeurs du tableau :

```python
# Retourne True si tous les éléments sont supérieur à 0
# et False sinon.
np.all(a > 0)
```

Les opérateurs logique **ET** et **OU** que vous connaissez en Python changent en Numpy, dans un mask vous devez écrire :

- Pour le ET on écrira : &
- Pour le OU on écrira : |

En effet, Numpy manipule des bits pour encoder les valeurs dans un tableau.

Si vous devez construire une proposition avec plusieurs assertions attention à la priorité des opérateurs. Le & est prioritaire par rapport à l'opérateur de comparaison.

```python
a = np.arange(1, 100)

mask1 = (a > 0) & (a < 10)
mask2 = (a > 0) & (a < 10) | (a > 12) & ( a < 100 )

a[mask2]
"""
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9,
       13, 14, 15, 16, 17, 18, 19, 20, 21
       22, 23, 24, 25, 26, 27, 28, 29, ..., 99])
"""
```

La méthode **np.all** retournera True si la condition est vérifiée pour tous les éléments dans la comparaison.

La méthode **np.any** retournera True si au moins une valeur de la comparaison est vraie.

```python
a = np.arange(1, 10)
b = np.arange(1, 10)

# Retourne un tableau de boolean
print( a == b )

# retourne True ou False, ici True
print('all', np.all(a == b))

# On change la première valeur
a[0] = 100
print('all', np.all(a == b))

# Pour la méthode np.any
c = np.array([1,2, 7])
d = np.array([3, 4, 5])
# Retounera True
print('any', np.any( c > d ) )

e = np.array([1,2, 0])
f = np.array([3, 4, 5])
# Retournera False
print('any', np.any( e > f ))
```

## Supprimer des lignes avec des données manquantes

Souvent dans les datasets des données manquent. Elles ont le type NaN dans Numpy. Pour qu'un tableau Numpy puisse contenir ce type de données manquantes il doit avoir le type float64 :

```python

# Sans définir le type du tableau celui-ci aura le type float64
x = np.array([[1,2,3], [4,5,np.nan], [7,8,9]])

print(x.dtype)
# float64

```

La méthode np.isnan suivante permet de créer un masque sur les données manquent du tableau :

```python
np.isnan(x)
"""
[[False False False]
 [False False  True]
 [False False False]]
"""
```
