arr=[1,4,5,-3,-6,-8,-7,0,0]
musbet=0
menfi=0
sifir=0
for i in arr:
    if i>0:
        musbet+=1
    elif i<0:
        menfi+=1
    elif i==0:
        sifir+=1
print(musbet,menfi,sifir)  

