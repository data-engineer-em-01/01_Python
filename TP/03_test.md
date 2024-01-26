# Tests avec Pytest

## 01 Exercice Parser

Testez la classe Parser 

## 02 Exercice Calculator TDD

Pour la problématique suivane, vous allez la traiter en TDD.

1. Voici une chaîne de caractères avec des aditions uniquement, sans parenthèse. Créez une classe et une fonction qui fait la somme de ces valeurs.
   
1. Faites d'abord les tests avant d'implémenter la logique dans la classe métier.

```python
s = "5.5 + 10 + 30 + 13.7"
total # 59.2
```

## 03 Exercice fixtures de tests

Dans cette partie vous allez utiliser des données d'exemple et les passer à un test évident pour vous familiarisez avec la notion de fixtures.

```bash
pip install pytest-datadir
```

1. Automatisez les tests avec les données d'exemple dans le dossier data pour le test de la somme.


## 03 Exercice Calculatrice en notation polonaise inversé

Dans l'esprit TDD faite l'exercice. Nous nous sommes ici inspiré de la NPI pour réaliser la correction, vous pouvez également regarder comment elle est implémentée.

Rappel sur la NPI, par exemple, sur une calculatrice, l'expression : `3x(10+5)` peut s'écrire en NPI sous la forme :

1. `10`
2. Touche Enter
3. `5+3 x`  

Ou de manière équivalente 

1. `3`
1. Touche Enter
1. `10` 
1. Touche Enter
1.  `5 + x`

1. Créez maintenent une classe qui effectue les opérations +, x avec des parenthèses en vous inspirant de la calculatrice NPI.

```python
s = "5.5 + 3*(10 + 30 - 13.7) "
```

