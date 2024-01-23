import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *t, **v):
        start = time.time()
        self.func(*t, **v)
        end = time.time()
        
        print(  end - start  )
            
@Timer
def foo(a, b):
    time.sleep(1)
    print(a, b)
    
foo(1, 2)

