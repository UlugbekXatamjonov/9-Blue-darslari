"""
Thame: if-esle-elif operatorlari
"""

""" if-else """
# a = 4 
# b = 2
# if a > b: # 1-usul
#     print(a)
# else:
#     print(b)

# if a > b: print(a) # 2-usul
# else: print(b)

""" == """
ismlar = ['Ali', 'Olim', 'Kamron', 'Abdulloh']
# for ism in ismlar: # == -> teng bo'lsa, tengmi ?
#     if ism == 'Olim': # if - Agar / Agar ism 'Ali' ga teng bo'lsa
#         print(f"Salom {ism} Admin, sizga yangi habar bor")
#     else:# else - yoki, boshqa barcha holatlarda
#         print(f"Salom {ism}")



""" != """
# for ism in ismlar: 
#     if ism != "Olim": # teng bo'lmasa
#         print(f"Salom {ism}, Olim kelmadimi ?")
#     else:
#         print(f"Salom {ism}")

""" elif """
# sonlar = [1,2,3,4,5,6,7,8,9,10]

# for son in sonlar:
#     if son < 5 : # agar son 5 dan kichik bo'lsa
#         print(f"{son} 5 dan kichik")
#     elif son == 5: # yoki 5 ga teng bo'lsa/ elifni istalgancha ishlatish mumkin
#         print(f"{son} 5 ga teng")
#     else: # qolgan barcha holatlarda
#         print(f"{son} 5 dan katta")

"""
    ==  -> teng bo'lsa
    !=  -> teng bo'lmasa
    >   -> katta bo'lsa
    <   -> kichik bo'lsa
    >=  -> katta yoki teng bo'lsa
    <=  -> kichik yoki teng bo'lsa
    or   -> yoki
    and  -> va 
"""

"""
1-mashq
Foydalanuvchidan 2 ta son kiritishini so'rab, ulardan qay biri katta, kichik yoki  tengligini topib beruvchi dastur tuzing.


2-mashq
ismlar = ['Ali', 'Olim', 'Kamron', 'Abdulloh', 'Karim', “Usmon”]

Yuqoridagi ro'yhatdagi isimlar ichidan faqat “Kamron” va “Karim” uchun:
Salom Karim(Kamron) ahvollaring yaxshimi ?
Degan habarni konsulga chiqaring. Qolgan barcha ismlar uchun esa:
Assalomu aleykum Ali
Ko'rinishidagi habarni konsulga chiqaring.


3-mashq 
mevalar = ["olma", "gilos", "oshqovoq", "sabzi", "anjir", "malina"]
Yuqoridagi ro'yhatdagi ikki sabzavot nomini barcha harflarini katta qilib, qolgan mevalarning nomini esa, 
birinchi harfini katta qilib konsulga chiqaring.(Masalani ishlashda or operatoridan foydalanish shart !)


4-mashq
205 dan 2024 gacha bo'lgan sonladan iborat ro'yhat yarating va ro'yhatdagi:
1000 gacha bo'lgan sonning 3-darajasini toping.
1500 dan katta barcha sonlarning o'zidan 3 taga kichik sonni toping.
Ro'yhatdagi 25 ga qoldiqsiz bo'linadigan sonlarning ildizini toping.
"""

# sonlar = list(range(205, 2024))
# for son in sonlar:
#     if son < 1000:
#         print(f"{son} ning 3-darajasi {son**3} ga teng")
#     elif son > 1500:
#         print(f"{son} ning o'zidan 3 taga kichigi {son-3} ga teng")
    
#     if son % 25 == 0:
#         print(f"{son} ning ildizi {son**0.5} ga teng")
        
        
""" or va and """
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
#     if son < 5 and son > 5: # agar son 5 ga teng yoki son 5 dan katta bo'lsa
#         print(f"{son} 5 ga teng emas")      

# son = int(input("Son kiriting: "))
# if son > 0:
#     print(f"{son} musbat")
#     if son%2 ==0:
#         print(f"{son} - juft")
#     else:
#         print(f"{son} - toq")
# elif son < 0:
#     print(f"{son} manfiy")

# """ pass """
# son = -7
# if son > 0:
#     pass


"""
0 - juda yomon
1  - yomon
2 - qoniqarsiz
3 - qoniqarli
4 - yaxshi
5 - alo
"""

"""
<-- 2-mashq -->
200 dan 500 gacha  bo'lgan toq sonlardan iborat bo'lgan ro'yhat yarating. Ro'yhatdagi:
200 dan 300 gacha bo'lgan sonlarni 4 darajaga ko'taring;
350 dan 400 gacha bo'lgan sonlarning ildizini toping;
420 dan 480 gacha bo'lgan sonlarni 3.5 ga bo'lib  3 hona aniqlikda yaxlidlab chiqaring;
480 dan 500 gacha bo'lgan sonlarni 6 darajasini konsulga chiqaring;

<-- 3-mashq --> 
Foydalanuvchidan imtihonda olgan balini so'rang. Agar uning bali:
0-40 ball oralig'ida bo'sa unga, “Sizning natijangiz juda yomon”;
41-60 ball oralig'ida bo'sa unga, “Sizning natijangiz qoniqarli”;
61-80 ball oralig'ida bo'sa unga, “Sizning natijangiz yaxshi”;
81-99 ball oralig'ida bo'sa unga, “Sizning natijangiz a'lo”;
Agar uning bali 100 ball bo'lsa unga “Tabriklaymiz siz 100% lik natija ko'rsatingiz”:
degan habarni konsulga chiqaring.
Shuningdek dasturga manfiy(-) va 100 dan katta sonlar kiritilganda;
“-Siz faqatgin 0-100 oralig'idagi sonlarni tanlashingiz mumkin !”, degan habar chiqsin.

<-- 4-mashq -->
Foydalanuvchidan o'tgan haftadagi Informatika fanidan olgan imtihon bahosini so'rang va 
uning bahosiga nisbatan quidagicha javob qaytaring:
0- 20 "Sizning natijangiz juda yomon:( "                              
21-35 " Sizning natijangiz qoniqarli :| "
36-45 " Sizning natijangiz yaxshi :) "                                      
46-49 " Sizning natijangiz juda yaxshi :)) "
50 - “Tabriklaymiz 100% lik natija :) :) :) ”
Agar foydalanuvchi manfiy(-) yoki 50 dan katta son kiritsa unga: “Siz noto'g'ri son kiritdingiz !” degan javobni qaytaring.

<-- 5-MASHQ -->
dastur: Assalomu aleykum do'konimizga hush kelibsiz !
dastur: Bizda quyidagi mahsulotlar bor: olma, anor, non, shakar, tuz, qaymoq
        Nechta mahsulot sotib olmoqchisiz ?
foydalanuvchi: 4
dastur: 1-mahsulotni kiriting:
foydalanuvchi: olma
dastur: 2-mahsulotni kiriting:
foydalanuvchi: non
dastur: 3-mahsulotni kiriting:
foydalanuvchi: sut
dastur: 4-mahsulotni kiriting:
foydalanuvchi: tuz
dastur: 5-mahsulotni kiriting:
foydalanuvchi: anjir
dastur: Siz tanlagan quyidagi mahsulotlar do'konimizda bor: olma, non, tuz
        Quyidagi mahsulotlar esa do'konimizda yo'q: sut, anjir
        Haridingizdan mamnunmiz ! 
"""
# mahsulotlar = ['olma', 'anor', 'non', 'shakar', 'tuz', 'qaymoq']
# yoq = []
# xarid = []
# print("Assalomu aleykum do'konimizga hush kelibsiz !")
# print("Bizda quyidagi mahsulotlar bor:", end=' ')
# for mahsulot in mahsulotlar:
#     print(f"{mahsulot}", end=' ')

# savol = int(input("\nNechata mahsulot sotib olmoqchisiz: "))
# for n in range(savol): # [0,1,2,3,4]
#     meva = input(f"{n+1}-mahsulotni kiriting: ")
#     if meva in mahsulotlar:
#         xarid.append(meva)
#     else:
#         yoq.append(meva) 
                   
# print(f"Bizda yo'q mahsulotlar:", end=" ")
# for y in yoq:
#         print(f"{y}", end=" ")
# print(f"\nBizda bor mahsulotlar: {xarid}")

# """ Tub sonlar """
# max_son = int(input("Maksimal sonni kiriting: "))
# tub_sonlar = []

# for son in range(2, max_son+1):
#     tub = True
    
#     for i in range(2, son):
#         if son % i == 0:
#             tub = False
#             break

#     if tub:
#         tub_sonlar.append(son)

# print(tub_sonlar)



"""
foydalanuvchidan uning ismini va yoshini kiritishini so'rab unga hayvonot bog'iga kirish narxini ayting.
        Narxlar:
1-7 va 70-100   --> bepul
8-18    --> 5_000 so'm
19- 69  --> 10_000 so'm
manfiy son --> "Musbat son kiriitng ! "
100 dan katta son uchun --> "Faqat 1-100 orasidagi son kiriting!"

"""

"""
3) Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
    -ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
    -GM uchun ikkala harfni katta qiling.
    -Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
    
4) Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini 
    hisoblab konsolga chiqaring. 
    -Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 

5) Parol tizimi. Foydalanuvchidan parol o'rnatishini so'rang. u ikki marta parol kiritsin.
    Kiritiladigan parol eng kamida 8ta belgiga teng bo'lishi kerak.
    Agar ikkala parol bir biriga teng bo'lsa; "Parol fuvaffaqiyatli o'rnatildi" degan
    habar chiqsin. Agar teng bo'lmasa "Xatolik ! Iltimos parolni boshqatdan kiriting"
    degn habar chiqsin.
    -va keyin parolni foydalanuvchidan boshqattan so'rasin, agar foydalanuvchi o'zi kiritgan
    parolni to'g'ri kiritsa, "Hush kelibsiz Admin" desin. Agar parol noto'g'ri kiritilsa
    "Parol xato" degan xabar chiqasin.

6)   Foydalanuvchidan ismi, yoshi va o'g'il yoki qiz bola ekanbligini so'rang.
        Agar u 15 yosh va o'g'il bola bo'lsa "9 Blue" sinfiga, agar 15 yosh va qiz bola bo'lsa 
        9 Green sinfiga qo'shishingiz kerak. 
        Agar u 15 yoshdan boshqa yoshda bo'lsa, "Kechirasiz biz faqat 15
        yoshli o'quvchilarni qabul qilamiz degan javobni qaytarishingiz kerak. 
"""
















