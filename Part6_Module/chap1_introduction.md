# Les Modules en Python

## Introduction
Un module en Python est un fichier contenant des définitions de fonctions, de classes et de variables qui peuvent être réutilisées dans d'autres programmes. Les modules permettent d'organiser et de structurer le code de manière modulaire.

## Création d'un Module

Un module Python est généralement créé en écrivant du code dans un fichier avec l'extension .py. Par exemple :  **mymodule.py**.

```python
# mymodule.py
def greet(name):

    return f"Hello, {name}!"

```

Dans un fichier dans le même dossier 

```python
import mymodule

mymodule.greet("Alan")
```

- Différentes manière d'importer 

```python
import mymodule as m

m.greet("Alan")
```

```python
from mymodule import greet

greet("Alan")

```

- dir et help permettent d'obtenir de documentation et de l'aide sur les modules.

## Module en tant qu'exécutable (programme)

Ajoutez à votre programme Python à la fin du fichier 

```python
if __name__ == "__main__":
    print("Module en tant que programme.")
```

## Structure d'un Package

Répertoire du Package : Un package est généralement un répertoire qui contient un fichier spécial \_\_init\_\_.py. Ce fichier indique à Python que le répertoire doit être traité comme un package. Il peut être vide ou **contenir** des initialisations spécifiques au package.

```txt
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

Modules dans le Package : Les fichiers Python (modules) qui font partie du package peuvent être organisés dans le répertoire du package ou dans des sous-répertoires (sous-packages).

```python
from mypackage import module1

# sous package import
from mypackage.subpackage import module3
# autre méthode 
from mypackage import module1, subpackage
```