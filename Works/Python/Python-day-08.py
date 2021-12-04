
class User:
    def __init__(self,_ad,_soyad):
        self.ad=_ad
        self.soyad=_soyad
    def melumatlariGoster(self):
        print(f'{self.ad} / {self.soyad}')
class Telebe(User):
    pass
   
class Muellim(User):
    def __init__(self,_ad,_soyad,_ixtisas):
        User.__init__(self,_ad,_soyad)
        self.ixtisas=_ixtisas
    def melumatlariGoster(self):
        print(f'{self.ad} / {self.soyad} /{self.ixtisas}')
    def melumatlariGoster(self,*args):
        print(args)

telebe=Telebe('Samir','Kerimov')
m=Muellim('Senan','Mansurov','Python')
              