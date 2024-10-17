"""
Thame:Sonlar(Integers) bilan ishalsh
"""
""" Sonlarning turlari """
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

""" Butun son turlari """
a = 15
b = -8
c = 0
print(a)
print(type(a))

""" O'nlik son turlari """
x = 35e3 # 35000.0
y = 12E4 # 120000.0
z = 14.76
print(z)
print(type(z))

"""Arifmetik amallar"""
a = 5
b = 7
print(a+b) # qo'shish
print(a-b) # ayrish
print(a/b) # bo'lish
print(a*b) # ko'paytirish

c = a+(b-a)*b
print(c)

"""Sonni kvadradga ko'tarish"""
from math import pow # power -> pow -> darajaga ko'tarish
print(pow(3, 4))

f = 3**4 #  ** kvadrat belgisi
print(f)

"""" Sonni ildizdan chiqarish  """
d = 16
from math import sqrt
print(sqrt(d))

""" Sonni yaxlidlash """
print(round(4.225 , 2))
print(round(4.225))


""" random moduli - tasodifiy son """
import random
print(random.randrange(1, 10))

""" int()/ str()/ float() """
a = 5           # butun son  --> int
b = 12.3        # o'nlik son --> float
c = "Salom"     # matn       --> str

print(type(a))  # a ni turini tekshiramiz
print(a)        # a ni konsulga chiqaramiz
a1 = float(a)   # a ni turini o'nlik son(float) ga "a1" o'zgartiramiz
print(type(a1)) # a1 ni turini tekshiramiz
print(a1)       # a1 ni konsulga chiqaramiz

"""Bir vaqting o'zida bir nechta o'zgaruvchi yaratish"""
x,y,z  = 4,9,-7
print(x,y,z)

""" Ko'p honali sonlar """
uzb = 36_032_123
yer = 800_321_215_245
print(uzb)
print(yer)


"""  Topshiriq
Yoshni topuvchi dastur tuzing.
Sonni kvga va kubga ko'taruvchi dastur tuzing.
Kvadratning perimetri va yuzin topuvchi dastur tuzing.   F-->  P=a*4  S=a**2
To'g'ri burchakli uchburchakning gipotenuzasini hisoblovchi dastur tuzing.  F--> c**2 = a**2 + b**2
"""

"""
Vazifa:
1) Alanani uzunligini topuvchi dastur tuzing. Aylananing radiusini 
foydalanuvchidan so'rang.  
   Formulasi: S=2*pi*r  / pi=3.14 / r= radius
2) Doirani yuzini topuvchi dastur. Aylananing radiusini 
foydalanuvchidan so'rang.
   Formulasi: S=pi*r**2 / pi=3.14 / r = radius
3) Tog'ri burchakli uchburchakni katetlari ni foydalanuvchidan 
so'rab, shu uchburchakning 
   gipotenuzasini hisoblaydigan dastur tuzing. 
   Formulasi: c**2 = a**2 + b**2   / a va b - katetlar, 
   c - gipotenuza
4) Foydalanuvchidan ikkita son kiritishini so'rab shu 
kiritilgan sonlarning o'rta 
   arifmetigini hisoblang.
   Formulasi: (a+b)/2
5) Foydalanuvchidan ikkita son kiritishini so'rab shu kiritilgan 
sonlarning yig'indisi, 
   ayirmasi, ko'paytmasi
   bo'linmasi, o'rta arifmetigi va har ikkala sonning kvadrati va 
   kuni aniqlang.
   Formulasi: a+b, a-b, a*b, a/b, (a+b)/2, a**2, a**3, b**2, b**3
6) Foydalanuvchidan ikkita A va B sonlarini kiritishini so'rang 
va sonlar qiymatini 
   almashtirib konsulga chiqaring.
7) Foydalanuvchidan ikkita A, B va C sonlarini kiritishini 
so'rang va A ni qiymatini 
   B ga , Bni qiymatinni C ga
   C ni qiymatini A ga almashtirib konsulga chiqaring
8) Foydalanuvchidan 'x' ni kiritishini so'rab quidagi 'y' ning zxc 
qiymatini toping.
   y = 4*(x-3)**5-7*(x-3)**3+2
9) Quidagi ammalarning natijasini yaxlidlang:
   231/4.7    24/1.4   541/7.6
10) math va random modullaring har biridan 5 tadan funksiyani 
o'rganib, undan foydalanish(misol yozib kelish).
    Darsda ko'rganlarimizdan tashqari ! 
"""