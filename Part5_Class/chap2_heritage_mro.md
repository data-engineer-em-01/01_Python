# Héritage complément

## Quelques fonctions utiles

### issubclass

La fonction `issubclass()` permet de vérifier si une classe est une sous-classe d'une autre classe. Voici un exemple :

```python
class Product:
    def __init__(self, name, price, tva=.2):
        self.name = name
        self.price = price
        self.tva = tva

# Héritage
class Bike(Product):
    pass

print(issubclass(Bike, Product))  # True
print(issubclass(Product, Bike))  # False
print(issubclass(Product, object))  # True
```

### isinstance

La fonction `isinstance()` permet de vérifier si un objet est une instance d'une classe ou de ses sous-classes. Voici un exemple :

```python
b = Bike("Mountain Bike", 500)
print(isinstance(b, Product))  # True
print(isinstance(b, Bike))  # True
print(isinstance(b, object))  # True

class Model:
    pass

print(isinstance(b, Model))  # False
```

## Héritage Multiple et Algorithme MRO ~ résolution de recherche des attributs

Python permet l'héritage multiple, où une classe peut hériter de plusieurs autres classes. L'ordre dans lequel les classes sont spécifiées affecte l'algorithme MRO (Method Resolution Order), qui détermine l'ordre dans lequel les méthodes sont recherchées lorsqu'elles sont appelées.

L'algorithme MRO peut être obtenu en utilisant l'attribut de classe `mro()`. Voici un exemple :

```python
class superA:
    pass

class superB:
    pass

# Héritage multiple
class normalA(superA, superB):
    pass

print(normalA.mro())
# [<class '__main__.normalA'>, 
#  <class '__main__.superA'>, 
#  <class '__main__.superB'>, 
#  <class 'object'>]
```

Dans cet exemple, `normalA` hérite de `superA` et `superB`. L'algorithme MRO est `[normalA, superA, superB, object]`, ce qui signifie que Python recherchera d'abord les méthodes dans `normalA`, puis dans `superA`, puis dans `superB`, et enfin dans `object`.

L'utilisation de `super()` dans le contexte d'héritage multiple peut être délicate car cela dépend de l'ordre dans lequel les classes sont spécifiées. Voici un exemple :

```python
class superA:
    def __init__(self):
        print("superA")

class superB:
    def __init__(self):
        print("superB")

# Héritage multiple
class normalA(superA, superB):
    def __init__(self):
        super().__init__()

normalA()  # affichera superA
```

Si vous inversez l'ordre des classes dans `normalA`, cela changera l'ordre de l'algorithme MRO :

```python
# Héritage multiple
class normalA(superB, superA):
    def __init__(self):
        super().__init__()

normalA()  # affichera superB
```

### Algorithme MRO : Méthode de résolution des ordres

L'algorithme MRO résout l'ordre dans lequel les méthodes sont recherchées dans l'héritage multiple en suivant un parcours spécifique dans l'arbre d'héritage.

L'algorithme MRO consiste à parcourir l'arbre d'héritage de bas en haut et de gauche à droite, en évitant les classes déjà rencontrées. Voici un schéma illustrant l'algorithme MRO :

```mermaid
graph TD
    A
    B
    C
    D
    A --> B
    A --> C
    B --> D
    C --> D
```

Dans cet exemple, l'ordre de résolution des méthodes serait `D`, `B`, `C`, `A`.:

### Exercice 1 : Héritage Multiple

Considérez les trois classes suivantes :

```python
class A:
    def who_am_i(self):
        print("Je suis A")

class B:
    def who_am_i(self):
        print("Je suis B")

class C(A, B):
    pass
```

1. Créez une instance de la classe `C` et appelez sa méthode `who_am_i()`. Quelle méthode est appelée et pourquoi ?
2. Modifiez l'ordre des classes de `C` de sorte que `B` soit la première classe dans l'héritage multiple. Comment cela affecte-t-il la méthode appelée ?

### Exercice 2 : Résolution de l'algorithme MRO

Considérez les classes suivantes :

```python
class X:
    pass

class Y:
    pass

class Z(X, Y):
    pass

class W(Y, X):
    pass

class A(Z, W):
    pass
```

1. Utilisez la méthode `mro()` pour déterminer l'ordre de résolution des méthodes de la classe `A`.
2. Appelez la méthode `who_am_i()` sur une instance de la classe `A`. Quelle classe implémentant `who_am_i()` est appelée et pourquoi ?

### Exercice 3 : Implémentation d'une hiérarchie de classe

Considérez les classes suivantes :

```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class GoldenRetriever(Dog):
    pass

class PersianCat(Cat):
    pass

class GoldenPersian(GoldenRetriever, PersianCat):
    pass
```

1. Créez une instance de la classe `GoldenPersian` et appelez sa méthode `make_sound()`. Quel son est émis et pourquoi ?
   
1. Ajoutez une classe `Bird` avec une méthode `make_sound()` qui imprime "Tweet". Modifiez la classe `GoldenPersian` pour qu'elle hérite également de `Bird`. Quel est le résultat lors de l'appel à `make_sound()` sur une instance de `GoldenPersian` maintenant ?
   
1. Modifiez la classe `GoldenPersian` pour que la méthode `make_sound()` soit définie à l'intérieur de `GoldenRetriever` au lieu de `Dog`. Quel est maintenant le résultat lors de l'appel à `make_sound()` sur une instance de `GoldenPersian` ?
