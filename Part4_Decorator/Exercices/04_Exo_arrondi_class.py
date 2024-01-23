import typing

class Arrondi:
    def __init__(self, precision ):
        self.precision = precision

    def __call__(self, f):
        def decorator(*args, **kwargs):
            res = f(*args, **kwargs)

            return round( res, self.precision )

        return decorator

# Utilisation du décorateur de classe avec paramètre
@Arrondi(precision = 10)
def average(*t):
    if len(t):
        return sum(t)/len(t)
    
print(average(1, 2, 3, 178))