# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')


# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12: 
#     price = 5000
# elif yosh<65: 
#     price = 10000
# elif yosh>=100: 
#     price = 0000   
# else: 
#     price = 8000
# print(f"Sizga kirish {price} so'm")



# kun=input('bugun kuniga qaysi kun?:')
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('bugun mazza qib dam oling !!!')
# else:
#     print('bugun ittak iwlaydiga kuningiz')



# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Bugun xavo juda ham issiq chomilishga bormaymizmi?")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("havo sovuq ekan buyogiga pubg timeeee !!!")
# else:
#     print('bugun ish kuni ishga boring')


# narh = 15000 
# choy = 1
# salat = 0
# if choy and salat: 
#     narh = narh + 10000 
# elif choy or salat: 
#     narh = narh + 5000 
# print(f"Jami {narh} so'm") 


# narh = 30000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 0

# if choy:  
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:   
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot: 
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti: 
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000    
# print(f"Jami {narh} so'm")


# menu = ['osh','qazonkabob','shashlik','norin','lavash','lagmon','burgerlar']
# ovqat = input('Nima ovqat yeysiz?:')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')    
# else:
#     print(f'Afsuski bizda bunday ovqat yoq bizda faqatgina {menu} bor')



# menu = ['osh','qazonkabob','shashlik','norin','lavash','lagmon','burgerlar']
# ovqat = input('Nima ovqat yeysiz?:')
# if ovqat.lower() not in menu:
#     print(f'Afsuski bizda bunday ovqat yoq bizda faqatgina {ovqat} bor')
# else:
#     print(f'Buyurtma qabul qilindi.{ovqat}ni besh daqiqada olib kelamiz')


# menu = ['osh','qazonkabob','shashlik','norin','somsa','lavash']
# buyurtmalar = ["osh","somsa","manti", "shashlik",]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")



# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# if buyurtmalar: 
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: 
#     print("Savatchangiz bo'sh!")

#1
# a=float(input('juft son kiriting:'))
# if a/2:
#     print('rahmat')
# else:
#     print('iltimos juft son kiriting')

#2
# yosh=int(input('iltimos toshingizni kiriting:'))
# if 4>yosh:
#     print('sizga kirish bepul')
# elif 18>yosh:
#     print('sizga kirish 10000 sum')
# elif 60<yosh:
#     print('sizga kirish 0 sum')
# elif 18<=yosh:
#     print('sizga kirish 15000 sum')

#3
# a=float(input('son kiriting:'))
# b=float(input('son kiriting:'))
# if (a==b):
#     print(f'{a}={b}')
# elif (a<b):
#     print(f'{a}<{b}')
# else:
#     print(f'{a}>{b}')


#4
# menu = ['yogurt','kartoshka','sabzi','anor','shaftoli','anor','olma' ]
# savat=[]
# for n in range(5):
#     savat.append(input(f'savatga {n+1}-mahsulotni qoshing:'))

# if savat: 
#     for savatda in savat:
#         if savatda in menu:
#             print(f"Menuda {savatda} bor")
#         else:
#             print(f"Kechirasiz, menuda {savatda} yo'q")
# else: 
#     print("Savatchangiz bo'sh!")


#5
# menu = ['yogurt','kartoshka','sabzi','anor','shaftoli','anor','olma' ]
# savat = []
# for i in range(5):
#     savat.append(input(f'savatga {i+1}-mahsulotni qoshing:'))

# bor=[]
# bow=[]
# for savatda in savat:
#     if savatda in menu:
#         bor.append(savatda)
#     else:
#         bow.append(savatda)
# if bow:
#     print(f'dokonimizda quydagi mahsulotlar yoq')
#     for mahsulot in bow:
#         print(mahsulot)
# else:
#     print('siz tanlagan barcha mahsulotlar dokonimizda bor')




#6
# foyda = ['azam','azim','ibrohim','ali','vali']
# yangi = input('yangi login kiriting:')
# if yangi in foyda:
#     print('bu login band!!!')
# else:
#     print(f'hush kelibsiz {yangi.title()}')


7
son=int(input('istalgan son kiriting:'))
for n in range(2,11):
    if not (son % n ):
        print(f'{son} soni {n} ga qoldiqsiz bolinadi') 









