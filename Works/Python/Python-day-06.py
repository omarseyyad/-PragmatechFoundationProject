users=[]
def addUser():
    _ad=input('Istifadəçi adı:')
    _soyad=input('Istifadəçi soyadı:')
    user={
        'ad':_ad,
        'soyad':_soyad
    }
    users.append(user)
   
    
def showUsers():
    no=1
    def showUsers():
        global no
    for user in users:
        print(f"""            
Istifadəçi No:{no}
Istifadəçi adı : {user['ad']}
Istifadəçi soyadı : {user['soyad']}
---------------
              """)
        no+=1
def deleteUser():
    print('Istifadəçi silindi')
def editUser():
    print('Istifadəçi məlumatları dəyişdirildi')

menyu="""
--------------------------------------------------------
                    Proqram Ana Sehifə
- Yeni istifadəçi əlavə etmək üçün --1-- yazin
- Var olan istifadəçiləri görmək üçün --2-- yazin
- İstifadəçi silmək üçün --3-- yazin
- İstifadəçi məlumatlarini deyismek ucun --4-- yazin
- Proqramı dayandırmaq üçün --5-- yazın
-------------------------------------------------------
"""

while True:
    print(menyu)
    emeliyat=input("Istediyiniz emeliyat kodunu yazin :")
    if emeliyat=='1':
        addUser()
    elif emeliyat=='2':
        showUsers()
    elif emeliyat=='3':
        deleteUser()
    elif emeliyat=='4':
        editUser()
    elif emeliyat=='5':
        break
    else:
        pass

