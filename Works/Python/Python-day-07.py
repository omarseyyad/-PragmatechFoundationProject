telebeler=[]
# Telebe istehsal etmek ucun lazim olan certyoju cekdim
class Telebe:
    def __init__(heci,_ad,_soyad):
        heci.ad=_ad
        heci.soyad=_soyad
    def melumatlariGoster(heci):
        print(f'{heci.ad} / {heci.soyad}')
    
# Cekilen ceryoja esasen telebeler istehsal etdim   
telebe01=Telebe('Senan','Mansurov')
telebe02=Telebe('Ali','Azizov')
telebe03=Telebe('Turyan','Aizov')

class kitab:
    def __init__(self, ad, yazici):
        self.name=ad
        self.writer=yazici
        self.qiymet=30
    def show(self):
        print(f"{self.name}/{self.writer}")
    def changePrice(self,priceAmout=1000):
        self.qiymet=self.qiymet+priceAmout
        
kitab01=kitab('Angels and Demons', 'Dan Brown')
kitab01.changePrice()
kitab01.qiymet
mehsullar=[]
class magaza:
    def __init__(self,_ad ,_mehsul ):
        self.ad=_ad
        self.mehsullar=[]
