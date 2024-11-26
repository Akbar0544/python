sabzavotlar=['sabzi','kartoshka','piyoz','karam']
narhlar=[8000,9000,10000,11000]
mowina=['mers','volvo','bmw','jiguli','lada']
print('Birinchi sabzavot:',sabzavotlar[0],narhlar[0])
print('Birinchi sabzavot:',sabzavotlar[1],narhlar[3])
print('Birinchi sabzavot:',sabzavotlar[2],narhlar[2])
print('Birinchi sabzavot:',sabzavotlar[3],narhlar[1])
print(narhlar[0]+narhlar[3])
print(narhlar[2]+narhlar[1])
print(mowina[-1])
narhlar[0]=9000
narhlar[3]=13000
narhlar[2]=10000
print(narhlar)
mevalar=['nok','olma','apelsin', 'orik']
mevalar.append('tarvuz')
print(mevalar)
mowina=[]
mowina.append('lacetti')
mowina.append('gentra')
mowina.append('kvadratsikl')
print(mowina)
mowina=['cobalt','lacetti' ,'gentra',]
mowina.insert(0, 'malibu')
mowina.insert(3, 'damas')
print(mowina)
meva=['olma','behi', 'nok','uzum']
del meva[0]
print(meva)
meva=['olma','behi', 'nok','uzum']
meva.remove('behi')
print(meva)
bozorlik=['yog','un','sabzi','kartowka','piyoz']
mahsulot=bozorlik.pop(2)
print('men'+ ' '+mahsulot + ' ' +'sotib oldim')
print('olinmagan mahsulotlar:',bozorlik)
ism=['kamoli','usmon','baxtiyor']
print('qalesan'+' '+ism[0] +' '+'bugun otiramizmi')
print('bilmadim'+' '+ism[1])
print('sen nma deysan'+' '+ism[2])
son=[4,-5,10,3.5]
print(son[0]+son[1])
print(son[2]-son[3])
print(son[0]*son[3])
print(son[2]/son[1])
ism=['dusari', 'tramp','salom','eng']
nat=ism.pop(0)
nat1=ism.pop(-3)
print('men'+ ' ' + nat + ' ' +  'korishib u kishidan oqish sirlarini soramoqchiman')
print('Agar'+ ' ' + nat1+ ' ' +'korib qolsam siyosat haqida gaplashaman')
dos=['ota','shox','ibo','najot','diyor','tolib','tohir']
dos.append('kamol')
dos.append('jamol')
dos.append('temur')
dos.remove('ota')
dos.remove('ibo')
del dos[3]
dos.insert(2,'baxti')
dos.insert(7,'izzat')
kel=dos.pop(1)
print(dos)
print('kelganlar royhati:'+' '+ kel)




