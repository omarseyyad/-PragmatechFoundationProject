#Destkopda bir fayl yaradin.
import os
#  C:\users\user\desktop
folderAdresi=os.path.join('C:/users/user/desktop','OsModule')

os.mkdir(folderAdresi)

print(os.path.exists(folderAdresi))

os.rename(os.path.join('c:/users/user/desktop/','OsModule')
,os.path.join('c:/users/user/desktop/','NewOsModule'))

folderPath=os.path.join('c:/users/asus/desktop/','NewOsModule')
filePath=os.path.join(folderPath,'a.txt')
# fileConnection=open(filePath,'r')

# data=fileConnection.read()
# newData=data.replace('coffee','kofe')
# newConnection=open(filePath,'w')
# newConnection.write(newData)


import os
folderPath='Depo'
#    if fileName.endswith('.css'):
#        print(fileName)

# if fileName[-4:]=='.css':
#         print(fileName)
for fileName in os.listdir(folderPath):
    if fileName.split('.')[-1]=='css':
        print(fileName)