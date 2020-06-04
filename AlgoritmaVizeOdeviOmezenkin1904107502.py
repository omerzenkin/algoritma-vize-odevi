#SORU2
import random
o=list(range(1,50))
 for i in range(6):
     m=random.choice(o)
     print(m)
     random.shuffle(o)
     

#SORU3
    
o = int(input("o değerini giriniz: "))
while a>=100:
   M = 0
    if(o>=100):
        print("o değeri 2 basamaklı olmalıdır.")
    o = int(input("o değerini giriniz: "))
R = open("sayilar.txt", "w") 
for i in range(o+1):
    birlerBasamagi = i%10
    onlarBasamagi = int(i/10)
   E = birlerBasamagi+onlarBasamagi
    if(E%2 != 0):
        dosyaText = str(i) + "\n"
        R.write(dosyaText)

print("Dosyaya  yazıldı.") 
R.close()
input();

#SORU4
M =['Aygun','Cicek','Deniz','Atar','Dener','Yilmaz']
E =[['Ayse',3,6,7],['Ece',5,2,4],[ 'Arya',6,5],['Ali',3],['Can',5,7,9,11],[ 'Aybar',2,3]]


o=[]
ayse_o=[]
ece_o=[]
arya_o=[]
ali_o=[]
can_o=[]
aybar_o=[]


ayse_o.append(E[0][0])
ayse_o.append(M[0])
ayse_o.append(ayse_R)

ece_o.append(E[1][0])
ece_o.append(M[1])
ece_o.append(ece_R)

arya_o.append(E[2][0])
arya_o.append(M[2])
arya_o.append(arya_R)

ali_o.append(E[3][0])
ali_o.append(M[3])
ali_liste.append(ali_R)

can_o.append(E[4][0])
can_o.append(M[4])
can_o.append(can_R)

aybar_o.append(E[5][0])
aybar_o.append(M[5])
aybar_o.append(aybar_R)


o.append(ayse_o)
o.append(ece_o)
o.append(arya_o)
o.append(ali_o)
o.append(can_o)
o.append(aybar_o)



from functools import reduce

ayse = E[0]

ayse.remove('Ayse')

ayse_R = reduce(lambda x,y : x+y ,ayse)


ece = E[1]

ece.remove('Ece')

ece_R = reduce(lambda x,y : x+y,ece)


        