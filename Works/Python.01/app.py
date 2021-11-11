# a=int(input('Yasinizi daxil edin:'))
# print(a+5)

# yas=int(input('yasinizi daxil edin:'))
# if yas>0 and yas<30:
#     print('kef ele')
# elif yas>25 and yas<30:
#     print('ne vaxt terpenirsen')
# if yas>35:
#     print('kefen hazirdir')

# numbers=[1,2,3,4,5,78,45,23]

# numbers.append(15)
# numbers.append(22)
# numbers.append(33)
# print(numbers)

# List metodları və tuple metodlarını qarşılaşdırın aradakı fərqləri kod nümumələri ilə izah edin.

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)


fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)