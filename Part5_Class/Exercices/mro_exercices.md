### Correction de l'exercice 1 :

#### Question 1 :
Lorsque vous appelez la méthode `who_am_i()` sur une instance de la classe `C`, la méthode de la classe `A` sera appelée. Cela est dû à l'ordre d'héritage défini dans la classe `C` où `A` est spécifié en premier.

```python
c = C()
c.who_am_i()  # Output: "Je suis A"
```

#### Question 2 :
Si vous modifiez l'ordre des classes de `C` pour que `B` soit la première classe dans l'héritage multiple, alors la méthode `who_am_i()` de la classe `B` sera appelée.

```python
class C(B, A):
    pass

c = C()
c.who_am_i()  # Output: "Je suis B"
```

### Correction de l'exercice 2 :

#### Question 1 :
Utilisons la méthode `mro()` pour déterminer l'ordre de résolution des méthodes de la classe `A` :

```python
print(A.mro())
# Output: [<class '__main__.A'>, <class '__main__.Z'>, <class '__main__.W'>, <class '__main__.Y'>, <class '__main__.X'>, <class 'object'>]
```

#### Question 2 :
Lorsque vous appelez la méthode `who_am_i()` sur une instance de la classe `A`, la méthode de la classe `Z` sera appelée car elle est la première classe rencontrée dans l'algorithme MRO.

```python
a = A()
a.who_am_i()  # Output: "Je suis A"
```

### Correction de l'exercice 3 :

#### Question 1 :
Créez une instance de `GoldenPersian` et appelez sa méthode `make_sound()` :

```python
gp = GoldenPersian()
gp.make_sound()  # Output: "Woof"
```

#### Question 2 :
Ajoutons une classe `Bird` avec une méthode `make_sound()` qui imprime "Tweet", et modifions la classe `GoldenPersian` pour qu'elle hérite également de `Bird` :

```python
class Bird:
    def make_sound(self):
        print("Tweet")

class GoldenPersian(GoldenRetriever, PersianCat, Bird):
    pass

gp = GoldenPersian()
gp.make_sound()  # Output: "Woof"
```

#### Question 3 :
Modifions la classe `GoldenPersian` pour que la méthode `make_sound()` soit définie à l'intérieur de `GoldenRetriever` au lieu de `Dog` :

```python
class GoldenRetriever(Dog):
    def make_sound(self):
        print("Woof")

class GoldenPersian(GoldenRetriever, PersianCat, Bird):
    pass

gp = GoldenPersian()
gp.make_sound()  # Output: "Woof"
```

Dans cet exemple, la méthode `make_sound()` de `GoldenRetriever` est appelée car elle est définie à l'intérieur de `GoldenRetriever` et c'est la première classe rencontrée dans l'algorithme MRO.