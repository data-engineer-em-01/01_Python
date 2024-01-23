

def arrondi(precision):
  def decorator_parms(func):      
        def decorator(*t):
            res = func(*t)
            if res is not None:
                return round(res, precision)
        
        return decorator
    
  return decorator_parms

@arrondi(precision = 2)
def average(*t) :
    if len(t):
        return sum(t) / len(t)
    
print(average(1,2,3,7.90, 87.675))