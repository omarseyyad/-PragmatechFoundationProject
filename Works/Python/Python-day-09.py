from data import User,users

def registerUser():
    ad=input('Adiniz :')
    soyad=input('Soyadiniz :')
    username=input('Istifadeci adiniz :')
    password=input('Sifreniz :')
    user=User(ad,soyad,username,password)
    users.append(user)
