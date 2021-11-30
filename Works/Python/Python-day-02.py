def ededler(a,b):
    return a+b 
ededler(2,5)

def somemethod(*ededler):
    print(ededler)
somemethod(1,2,3,4,5)

def somemethod(*ededler):
    list(ededler)
    print(list(ededler))
somemethod(1,2,3,4,5)

def somemethod(*ededler):
    cem=0
    for i in ededler:
        print(i)
somemethod(2,4,5)

ededler=[1,2,3,4,5]
def somemethod():
    print(len(ededler))
somemethod()