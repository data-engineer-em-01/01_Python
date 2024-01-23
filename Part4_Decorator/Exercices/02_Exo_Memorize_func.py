
def memoize(func):
                
    def decorator (*args):
        try:
            res = decorator.cache[args]
            
            return res
        except KeyError:
            print(args, "keyErrors")
            # on fait vraiment le calcul
            res = func(*args)
            # on le range dans le cache
            decorator.cache[args] = res
            # on le retourne
            return res
    # on initialise l'attribut 'cache'
    decorator.cache = {}
    return decorator

@memoize
def factoriel(n: int )-> int:
    
    return n if n <= 1 else factoriel( n-1 ) * n 

print(factoriel(5))
print(factoriel(6))
