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

def func():
    for i in range(20):
        print(i)
func()

a=5
print(type(a))

ededler=[1,2,3,'salam',True]
for element in ededler:
    if type(element)==int:
        print(element ,' ededdir')
    else:
        print(element, 'eded deyil')

ededler=[1,2,3,'salam',True]
eded=[]
string=[]
Bool=[]

for element in ededler:
    if type(element)==int:
        eded.append(element)

for element in ededler:
    if type(element)==str:
        string.append(element)
    
for element in ededler:
    if type(element)==bool:
        Bool.append(element)
print(eded)
print(string)
print(Bool)