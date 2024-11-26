mehmonlar=['ali','vali','hasan','husan','kamol','ibo','ota']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi")






mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)
    
print(mehmonlar)



sonlar=list(range(1,11))
for son in sonlar:
    print(f'{son} ning kvadrati {son**2} ga teng')


sonlar=list(range(1,11))
son_kvadrati=[]
for son in sonlar:
    son_kvadrati.append(son**2)

print(sonlar)
print(son_kvadrati)




dostlar = [] 
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): 
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)


                                         

ism=['ali','vali','gani','hasan','husan']
for ot in ism:
    print(f'Hush kelibsiz  mono markazga {ot} ' )
    print(f'Sizga qanday yordam bera olamiz')
print(f'{len(ism)} marta qaytarildi')


son=list(range(11,100,2))
for son1 in son:
    print(f'{son1} ning kavadrati {son1**3} ga tehg')
 

son2=list(range(11,100,2))
son_kvadrati=[]
for son3 in son2:
    son_kvadrati.append(son3**3)
    
print(son2)
print(son_kvadrati)



kino=[]
print("5 ta eng kop koradigan kinoyingiz?")
for s in range(5):
    kino.append(input(f"{s+1}-kino"))
print(kino)  



n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)


 