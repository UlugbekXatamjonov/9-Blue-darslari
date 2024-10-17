""" 
Thame: for operatori
"""
"""
    For tsikli ketma-ketlikni takrorlash uchun ishlatiladi.
    For tsikli yordamida biz ro'yxatdagi har bir element uchun bir martadan, qandaydir kod 
    bajarishingiz mumkin.
"""

# ismlar = ['Ali','Bobur', 'Ravshan', "Olim", "hasan", "Husan"]
# print(f"Salom, {ismlar[1]}")

""" for operatori """
# for ism in ismlar: # ismlar ro'yhatidagi har bir ism(element) uchun
#     print(f"Salom {ism}. Ahvollaring yaxshimi ?") # ushbu kodni bajar 
# print("Hurmar bilan Mr Mansurbek !")


# ism = "Azizbek"
# for i in ism:
#     print(i)

""" for va range() funksiyasi  """
# for son in range(1,101):
#     print(f"{son}-fhhfghfg")


# for x in range(100):
#     print(f"{x}-ning kvadrati {x**2} ga teng")


""" for() ichida for() """
# sifat = ["qizil", "katta", "mazali"]
# mevalar = ["olma", "nok", "apelsin"]  

# for s in sifat:
#     for meva in mevalar:
#         print(f"{meva} - {s}")

""" Mashqlar """
""" 1 """
# sonlar = [2, 6, -9, 0, 8.5, 21, 65, -34, 43.6]
# sum = 0

# for son in sonlar:
#     sum = sum + son
#     # sum += son   
# print(f"Sonlar ro'yhatidagi sonlarning yig'insidi {sum} ga teng.")


# son = int(input("Oila azolaringiz sonini kiriting: ")) # foydalanuvchidan oila azolarining sonini so'raymiz
# oila = [] #bo'sh ro'yhat yaratib olamiz
# for n in range(son): # foydalanuvchidan oila azolarini sonicha savol so'raymiz
#     azo = input(f"{n+1}- azongizni ismi kiriting: ") # ola azosinging ismini olamiz
#     oila.append(azo) # qabul qilingan ismni ro'yhatga qo'shamiz
# print(oila)

# print("Sizning oila azolaringiz: ", end=" ")# end -> qator tugashi ' ' bo'shliq bilan tusin, va keyingi qator bn ulanib chiqsin
# for ism in oila:
#     print(f"{ism.title()}", end=" ")
    
"""
Vazifa:
1) Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing.
    -ro'yxatdagi har bir ismga  takrorlanuvchi xabar yozing;
    -Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni 
        chiqaring (n o'rniga kod necha marta takrorlanganini yozing)

2) 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
    -ro'yxatning xar bir elementining kvadratini va kubini yangi qatordan konsolga chiqaring.
    -ro'yhatdagi har bir elementdan 1 ga kichik va 3 ga katta bo'lgan sonni birgalikda konsulga chiqaring

3) Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. 
    Natijani konsolga chiqaring. 

4)Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
    va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

"""

    
    
    
    
    




