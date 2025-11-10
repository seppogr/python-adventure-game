CGREEN  = '\33[32m'
CEND      = '\33[0m'

list = ['a', 'b', 'c']
def extractList(listOfItems):
    a = " ".join([str(item) for item in listOfItems])
    print(type(a))
    return a

print(CGREEN + extractList(list) + CEND)