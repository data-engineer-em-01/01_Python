# Cours d'Introduction à Pytest

## Installation

Pour installer Pytest, utilisez la commande suivante dans votre terminal :

```bash
pip install pytest
```

Soit vous travaillez avec Anaconda, soit vous utilisez l'environnement proposé Docker dans le cours.

Créez la structure des dossiers dans le dossier work de votre Anaconda ou Docker.

```txt
.
├── app.py
├── notebooks
│   └── main.ipynb
├── src
│   └── helpers
│       ├── __init__.py
│       └── utils.py
└── tests
    ├── __init__.py
    └── test_reverse.py
```

On fait un premier test pour voir si tout est bien installé. Dans le fichier de test test_reverse.py :

```python
from src.helpers.utils import reverse

def test_should_reverse_string():
    assert reverse('abc') == 'cba'
```

Exécutez le test avec la commande :

:shell:

```bash
pytest 
# ou pytest test_reverse.py
```

## Introduction à Pytest

### Qu'est-ce que Pytest ?

Pytest est un framework de test pour Python qui offre une syntaxe simple et expressive pour écrire des tests unitaires. 

>[!NOTE]
>Il se distingue par sa facilité d'utilisation, il est puissant et ses fonctionnalités sont avancées.

## Structure des Tests

### Conventions de Nom de Fichiers et de Fonctions

Les fichiers de test doivent être nommés avec le préfixe test_ (par exemple, test_example.py). 

Les fonctions de test doivent également commencer par test_.

### Exemple 

Écrivons un test pour une fonction simple on utilise le mot clé **assert** :

# test_functions.py


```python
def test_multiply():
    assert 2 * 3 == 6
```

##  Assertions

### Utilisation des Méthodes d'Assertion Pytest

Pytest offre des méthodes d'assertion. 

Utilisons assert x == y pour vérifier une égalité :

# test_advanced_assertions.py

```python
def test_advanced_assertions():
    x = "hello"
    y = "world"
    assert x == y, f"Les chaînes ne sont pas égales : {x} != {y}"
```

## Personnalisation des Messages d'Erreur
Personnalisez les messages d'erreur pour une meilleure compréhension des échecs de test :

# test_custom_error_message.py
```python

def test_custom_error_message():
    expected = 4
    actual = 2 + 2
    assert expected == actual, f"Erreur : {actual} n'est pas égal à {expected}."
```

## Tests Paramétrés

Utilisons @pytest.mark.parametrize pour créer des tests paramétrés.

>[!NOTE]
>Très utile lorsque nous voulons automatiser un ensemble de valeurs pour tester une fonction.

### test_reverse.py

```python
import pytest 
from src.helpers.utils import reverse

@pytest.mark.parametrize("input, expected", [('abc', 'cba'), ('bonjour', 'ruojnob')])
def test_should_reverse_string(input, expected):
    assert reverse(input) == expected
```

## Organisation des Tests

## Groupement des Tests avec les Classes

Organisez vos tests en classes pour une meilleure **lisibilité** :

# test_classes.py

```python
class TestOperator:
    def test_addition(self):
        assert 1 + 1 == 2

    def test_subtraction(self):
        assert 3 - 1 == 2
```

##  Tests de Fonctions et de Méthodes de Classe

Écrivons un test pour une méthode de classe :

# test_class_methods.py

```python
# vous devez importer cette classe depuis la partie applicative
class Calculator:
    def add(self, a, b):
        return a + b

def test_calculator_addition():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5
```

## Fixture de tests

Utilisez les fixtures pour préparer l'environnement de test :

>[!NOTE]
>Vous pouvez créez un fichier configtest.py pour écrire vos fixtues. Ne l'importez pas dans vos tests, il le sera automatiquement.

# configtest.py

```python
import pytest

# Fixture qui renvoie une liste de nombres
@pytest.fixture
def list_numbers():
    return [1, 2, 3, 4, 5]

# Exemple de test utilisant la fixture
def test_sum_list(list_numbers):
    s = sum(liste_de_nombres)
    assert s == 15
```

## Contrôle des Exceptions

Utilisez pytest.raises pour tester les exceptions :

# test_exception_handling.py

```python

import pytest

def test_exception_handling():
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0
```

## Mocking

### Introduction au Mocking

Utilisez pytest-mock pour le mocking dans les tests.

>[!NOTE]
>Pensez à vérifier qu'il est bien installé sur votre machine, et sinon faites un pip install pytest-mock

# test_mocking.py

```python
class Calculator:
    def add(self, a, b):
        return a + b

def test_calculator_add(mocker):
    # Création d'une instance de la classe Calculator
    calc = Calculator()

    # Utilisation de mocker.patch pour remplacer la méthode add par une version modifiée
    mocker.patch.object(calc, 'add', return_value=10)

    # Test avec la méthode modifiée
    result = calc.add(3, 5)

    # Vérification que la méthode modifiée a été appelée avec les bons arguments
    calc.add.assert_called_once_with(3, 5)

    # Vérification du résultat
    assert result == 10
```

>[!NOTE]
>calc.add.assert_called_once_with est une assertion donc un test en soi.

## Test-Driven Development (TDD) Introduction

:rocket:
Le Test-Driven Development (Développement Piloté par les Tests) est une approche de développement logiciel où des tests automatisés sont écrits **avant le code de production**. Le cycle TDD suit généralement ces étapes :

1. Écriture d'un test automatisé qui décrit une fonctionnalité ou une amélioration souhaitée.
1. Exécution du test pour vérifier qu'il échoue initialement (car la fonctionnalité n'a pas encore été implémentée).
1. Écriture du code minimal nécessaire pour faire passer le test avec succès.
1. Exécution à nouveau du test et vérification qu'il réussit.
1. Refactorisation du code pour améliorer la qualité tout en maintenant la fonctionnalité.

:rocket:
Le TDD vise à garantir que le code produit est **robuste**, **maintenable** et répond aux exigences définies par les tests automatisés.

>[!NOTE]
>Cette approche favorise la qualité du code, la réflexion sur la conception logicielle et offre une suite de tests complète pour détecter les régressions.
