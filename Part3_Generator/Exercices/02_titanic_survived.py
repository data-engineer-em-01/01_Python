import csv

class Counter:
    def __init__(self, count = 0):
        self.count = count
        
c = Counter()

class Passenger:
    def __init__(self, id, survived,pclass,name,sex,age ):
        pass

# lecture d'un fichier 
def gen_titanic(file, age = 41):
    with open(file, 'r') as csv_file:
        spamreader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for row in spamreader:
            if ( row[1] in ('0', '1') and row[1]  == '1' ) and ( "female" in row ) and ( row[6] != '' and float( row[6] ) < 41 ) :
                yield {"id" : row[0], "name" : row[3], "age" : float( row[6] ) }
    
            
g = gen_titanic("./Data/titanic.csv")


try:
    while True:
        res = next(g)
        print(res)
except StopIteration as e:
    print("stop", c.count )
    
