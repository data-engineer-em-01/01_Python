# Cours d'Introduction à Pytest


## I. Introduction à Pytest

### A. Qu'est-ce que Pytest ?

Pytest est un framework de test pour Python qui offre une syntaxe simple et expressive pour écrire des tests unitaires. Il se distingue par sa facilité d'utilisation, sa puissance et ses fonctionnalités avancées.

### B. Installation de Pytest
Pour installer Pytest, utilisez la commande suivante dans votre terminal :

```bash
pip install pytest
```

### C. Premier Test avec Pytest

Écrivons un test simple dans un fichier test_example.py :

# test_example.py

```python
def test_addition():
    assert 1 + 1 == 2
```

Exécutez le test avec la commande :

```bash
pytest test_example.py
```
## II. Structure des Tests
### A. Conventions de Nom de Fichiers et de Fonctions

Les fichiers de test doivent être nommés avec le préfixe test_ (par exemple, test_example.py). Les fonctions de test doivent également commencer par test_.

### B. Tests de Fonctions Simples
Écrivons un test pour une fonction simple :


# test_functions.py

```python
def test_multiply():
    assert 2 * 3 == 6
```

## C. Tests Paramétrés
Utilisons @pytest.mark.parametrize pour créer des tests paramétrés :


# test_parametrized.py
```python
import pytest

@pytest.mark.parametrize("input, expected", [(1, 2), (2, 4), (3, 6)])
def test_double(input, expected):
    assert input * 2 == expected
```

## III. Organisation des Tests
## A. Groupement des Tests avec les Classes
Organisez vos tests en classes pour une meilleure lisibilité :

# test_classes.py

```python
class TestMathOperations:
    def test_addition(self):
        assert 1 + 1 == 2

    def test_subtraction(self):
        assert 3 - 1 == 2
```

## B. Tests de Fonctions et de Méthodes de Classe
Écrivons un test pour une méthode de classe :

# test_class_methods.py

```python
class Calculator:
    def add(self, a, b):
        return a + b

def test_calculator_addition():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5
```

## C. Fixture de Test
Utilisez les fixtures pour préparer l'environnement de test :

# test_fixture.py

```python
import pytest

@pytest.fixture
def setup_and_teardown():
    print("\nSetup : Connect to database, initialize resources.")
    yield
    print("\nTeardown : Disconnect from database, release resources.")

def test_with_fixture(setup_and_teardown):
    print("Running test with setup and teardown.")
    # ... Votre test ici ...
```

## IV. Assertions Avancées
### A. Utilisation des Méthodes d'Assertion Pytest
Pytest offre des méthodes d'assertion avancées. Utilisons assert x == y pour vérifier l'égalité :


# test_advanced_assertions.py

```python
def test_advanced_assertions():
    x = "hello"
    y = "world"
    assert x == y, f"Les chaînes ne sont pas égales : {x} != {y}"
```

## B. Personnalisation des Messages d'Erreur
Personnalisez les messages d'erreur pour une meilleure compréhension des échecs de test :


# test_custom_error_message.py
```python

def test_custom_error_message():
    expected = 4
    actual = 2 + 2
    assert expected == actual, f"Erreur : {actual} n'est pas égal à {expected}."
```

## C. Contrôle des Exceptions
Utilisez pytest.raises pour tester les exceptions :

# test_exception_handling.py

```python

import pytest

def test_exception_handling():
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0
```

## V. Mocking
### A. Introduction au Mocking
Utilisez pytest-mock pour le mocking dans les tests :


# test_mocking.py

```python
import pytest

def test_mocking_example(mocker):
    mock_object = mocker.Mock()
    mock_object.some_method.return_value = "
```

