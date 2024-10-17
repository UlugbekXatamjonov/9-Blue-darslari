"""
Thame: Dictionary(Lug'atlar)
"""

# taomlar = {
#     'ali':'osh',
#     'vali':'shashlik',
#     'hasan':"lag'mon",
#     "olim":"Sho'rva",
    
# }

""" 
taomlar = {'ali':'osh'}
nomi    = {'key':'value'}
"""

# print(taomlar['ali'])
# print(f"Alinging sevimli taomi {taomlar['ali'].title()}")

# buyumlar = {
#     "ism":"Ali",
#     "yosh":12,
#     "student":True,
#     "oila":["ota","ona",'aka'],
#     "fanlar":{
#         "matematika":50,
#         "ingliz_tili":45
#     }
# }
# print(buyumlar)


""" Qiymat qo'shish """
# taomlar["nodir"] = 'norin'
# taomlar['azimjon'] = input("Azimjoning taomi ? ")
# print(taomlar)

# taomlar.update({"akramjon":"lag'mon"})
# print(taomlar)

""" Qiymatni o'zgartirish / update() """
# taomlar["hasan"] = 'qozon_kabob'
# print(taomlar)

# taomlar.update({"olin":"manti"})
# print(taomlar)


""" Qiymatni o'chirish """
# del taomlar["olim"]
# print(taomlar)

# taomlar.pop("hasan")
# print(taomlar)

# taomlar.popitem() # lug'atning oxiridagi elementni olib tashlaydi
# print(taomlar)

# """ Lug'atni tozalash """
# taomlar.clear()
# print(taomlar)


"""
1) otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta 
    m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida 
    konsolga chiqaring M: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

2) Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z(atamani) kiriting 
    (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
    
3) Fanlar deb nomlangan lug'at yarating, unda {“kalit”:”fan nomi”}  ko'rinishidagi 2 ta fan bo'lsin.  Keyin esa:
    2 ta yangi qiymat qo'shing(2 xil usulda);
    2 ta qiymatni o'zgartiring(2 xil usulda);
    3 ta qiymatni o'chiring(3 xil usulda);
    So'ngra Fanlar ro'yhatini tozalab tashlang;
    
"""



# """ Ro'yhatdan nusha olish """
# meals = taomlar.copy()
# print(meals)

# meals2 = dict(taomlar)
# print(meals2)

# """ get() metodi """
# ismlar = {
#     "axrorbek":"5",
#     "mansurbek":"4",
# }
# print(f"Salom, {ismlar['ali']}")
# print(f"Salom, {ismlar.get("ali", "55")}")

# """ items() metodi """
# print(taomlar)
# print(taomlar.items())
# for key, value in taomlar.items():
#     print(f"{key.title()}ning sevimli taomi {value.title()}")


davlatlar = {
    'uzbekistan':"Tashkent",
    'usa':"Vashington",
    'russian':"Russian",
}

""" keys() va values() metodlar """
# print(davlatlar.keys())
# print(davlatlar.values())

# for key in davlatlar.keys():
#     print(f"{key}")

# for value in davlatlar.values():
#     print(f"{value}")

""" Do'kon """
ombordagi_mahsulotlar = {
    "olma":4500,
    "nok":2000,
    "non":3000,
    "asal":15000,
    "tuz":2500,    
}

print(f"Bizning do'konimizda quidagi {len(ombordagi_mahsulotlar)} ta mahsulotlar bor: ")
for mahsulot, narx in ombordagi_mahsulotlar.items():
    print(f"{mahsulot.title()} - {narx} so'm")

bor = []
yoq = []
ummumiy_narx = 0

son = int(input("Nechta mahsulot olmoqchisiz: "))
for s in range(son):
    tavar = input(f"{s+1} - mahsulot nomini kiriting: ").lower()

    for mahsulot, narx in ombordagi_mahsulotlar.items():
        if tavar == mahsulot:
            bor.append(tavar)
            ummumiy_narx = ummumiy_narx + narx
            # ummumiy_narx += narx
    if tavar not in  ombordagi_mahsulotlar:
        yoq.append(tavar)

if bor:
    print(f"Quidagi {len(bor)} ta mahsulot bizda bor va ularning ummumiy narxi {ummumiy_narx} so'm ekan: ", end=" ")
    for b in bor:
        if b == bor[-1]:
            print(f"{b}", end=".")
        elif b == bor[0]:
            print(f"{b.title()}", end=", ")
        else:
            print(f"{b}", end=", ")

if yoq:   # if len(yoq) > 0: 
    print(f"\nQuidagi {len(yoq)} ta mahsulot bizda yo'q ekan: ", end=" ")
    for y in yoq:
        if y == yoq[-1]:
            print(f"{y}", end=".")
        elif y == yoq[0]:
            print(f"{y.title()}", end=", ")
        else:
            print(f"{y}", end=", ")
            
            

"""
1) Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
    Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

2) Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni 
    alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
    
3) Foydalanuvchidan istalgan davlatni kiritishni so'rang agar foydalanuvchi davlar kiritsa uning poytaxini, 
    poytaxt kiritsa uning davlatini konsulga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
    "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
    
4) Restoran menusi lug'atini tuzing(kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat
    buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda 
    bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
"""         
            
            
            
            
            
            
