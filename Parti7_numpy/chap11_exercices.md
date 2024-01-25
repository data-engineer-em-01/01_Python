# Exercices

## Exercice utiliser une fonction pour rechercher une séquence

L'objectif de cet exercice est de déterminer la première position dans chaque ligne du tableau **dataNumbers** de la séquence **w** ci-dessous.

1. Créez une fonction **search_word** qui prendra en paramètre : une liste d'entiers (séquence à chercher). Cette fonction retournera la position de la première occurence de la séquence à rechercher.

Dans l'exemple suivant search_word(w) doit retourner l'indice 2.

```python
w = [1,2,3,4]
line =  [ 6,  9,  1,  2,  3,  4,  3,  1,  4,  3,  9,  6,  2,  2]
```

2. Utilisez maintenant cette fonction avec les données du tableau **dataNumbers**. Trouvez toutes les positions des séquences dans chacune des lignes du tableau, si la séquence n'existe pas retournez None. Pour appliquer une fonction à un tableau Numpy vous utiliserez la fonction **apply_along_axis**, voyez l'exemple ci-dessous :

```python

# paramètres : fonction, axis = 0, 1, dataset
np.apply_along_axis(search_word, 1, dataNumbers)
```

Vous retournerez un tableau de dimension 1 avec les positions de chacune des séquences si elles existent et None sinon.

```python

w = [1, 2, 3, 4]

dataNumbers = np.array([
       [ 6,  3,  3,  7,  7,  4,  7,  8,  5,  3,  7,  8,  4,  2],
       [ 6,  9,  1,  2,  3,  4,  3,  1,  4,  3,  9,  6,  2,  2],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
       [ 4,  9,  2,  1,  1,  2,  3,  4,  3,  1,  9,  8,  2,  6],
       [ 3,  2,  9,  9,  2,  3,  6,  9,  8,  2,  1,  2,  3,  4],
       [ 1,  4,  1,  2,  3,  4,  4,  5,  8,  8,  1,  5,  7,  1],
       [ 1,  4,  3,  8,  2,  1,  2,  3,  4,  3,  9,  3,  5,  8],
       [ 7,  8,  8,  5,  1,  8,  3,  3,  6,  1,  2,  3,  4,  7],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
       [ 7,  7,  1,  6,  1,  2,  3,  4,  9,  2,  4,  4,  5,  9],
       [ 5,  6,  6,  2,  3,  7,  1,  9,  9,  5,  1,  2,  3,  4],
       [ 7,  7,  2,  3,  3,  7,  9,  4,  3,  9,  1,  1,  1,  1],
       [ 6,  1,  2,  3,  4,  5,  5,  3,  1,  3,  1,  2,  3,  4]
       ],dtype='int8'
)

```

## Exercice température

Nous avons relevé des températures au mois de Janvier. Répondez aux questions suivantes :

1. Donnez toutes les températures qui sont supérieures à 0.

2. Comparez les températures supérieures et inférieures à 0.

3. Donnez la moyenne des températures positives sur le mois.

4. Créez un tableau days pour les jours du mois et donnez les jours pour lesquels la température était supérieure à 0.

5. Donnez toutes les températures supérieures à 0 à partir du dixième jour du mois.

6. Remplacez maintenant les températures négatives par la  moyenne des températures positives.

```python

january = np.array([-2,  5, -5,  6, -2,  0,  6,  2,  8,  0,  6, -1,  3,  3,  7,  0, -5,
        7,  4,  7,  8, -1,  5, -2,  3, -3, -2,  7,  8,  4,  2])
```

## Exercice multiple de 11

Soit le tableau suivant, c'est un tableau random d'entiers de 1 à 200. Nous souhaitons l'explorer pour rechercher tous les multiples de 11.

```python
dataset = np.random.randint(1, 200, size=(20, 20) )
```

1. Générez un array Numpy y de tous les multiples de 11 inférieurs à 200.

2. En utilisant la fonction Numpy suivante récupérez tous les multiples de 11 du dataset.

```python
np.isin(dataset, y)
```

3. Supprimez toutes les lignes comportant au moins un multiple de 11.

## Exercice données manquantes

1. Soit le tableau x suivant supprimer toutes les lignes qui comportent des données manquantes :

```python
x = np.array([[1,2,3], [4,5,np.nan], [7,8,9]])
```

2. à partir du même tableau x supprimer maintenant les colonnes qui comportent des données manquantes.
