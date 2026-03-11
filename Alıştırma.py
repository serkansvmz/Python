

my_string = "Python Ogreniyorum"
a=my_string[4]
print(a)

#----------------------------------------------

my_new_string = "ProgramlamayaMerhabaDedik"
print(my_new_string[4:8])

#----------------------------------------------

my_last_string = "Afyonkarahisarlilastiramadiklarimizdanmisiniz"
print(my_last_string[::-1])

#-----------------------------------------------

# 6) Bu listeyi en az 2 farkli yoldan olusturunuz: [1,3,"a"]

liste = [1,3,"a"]
print(liste)

liste = list((1,3,"a"))
print(liste)

#--------------------------------------------

my_list = [3.14,4,[2,3,"b"],True]
print(my_list[2][2])

#------------------------------

my_dictionary = {"key1":20.25, "kk2":[40,{"k21":"a"}]}
print(my_dictionary["kk2"][1]["k21"])

#---------------------------------------------

my_list_to_be_set = [3,4,9,3,21,22,4,3,9,10,21,22]
print(set(my_list_to_be_set))

#-------------------------------------------------

x = 30 * 5 + 3
y = 108 - 2 * 4
print(x,",",y)

#----------------------------------

x = 5
y = 3
z = 6
print(x>y,z>x)

#-----------------------------------

yas = 20

if yas < 18:
    print("18 yaşından küçüksünüz")
elif yas >= 18 and yas < 30:
    print("18 ile 30 yaş arasında bir gençsiniz")
elif yas >= 30 and yas < 40:
    print("30 ve 40 arasına gelmişsiniz")
else:
    print("40 yaşından daha büyüksünüz")

#------------------------------------------

my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"} 

for i in my_dictionary:
      if my_dictionary[i]=="c":
          print("geçiyor=> ",i,":", my_dictionary[i])
      else:
          print("geçmiyor")  

#-------------------------------------------------

my_other_dictionary = {"b":203,"c":"a","a":400,"d":"f"}

for i in my_other_dictionary:
      if my_other_dictionary[i]=="a":
          print("geçiyor=> ",i,":", my_other_dictionary[i])
      else:
          print("geçmiyor")  

#-----------------------------------------------------

my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]

for i in my_numbers:
    if i % 2 == 0:
        print(i)

#------------------------------------------------

r_list = [3,2,5,8,4,6,9,12]
pi = 3.14
cevre_list = [ 2 * pi * r for r in r_list]
print(cevre_list)

r_list = [3,2,5,8,4,6,9,12]
pi = 3.14
cevre_list = []
for r in r_list:
    cevre = 2 * pi * r
    cevre_list.append(cevre)
print(cevre_list)

#-----------------------------------------------

ge_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
ge_age_list = [ i[1] for i in ge_name_list]
print(ge_age_list)

#-----------------------------------------------

metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]
import random
print(random.choice(metal_list))

#--------------------------------------------

number_list = [5,7,18,21,20,10,405,24]
print([num % 2 == 0 for num in number_list])

#--------------------------------------------

def toplama(a,b):
    print(a,b)

x = toplama(3,4)
print(x)

#--------------------------------------------

def usselIslem(x=5,y=3):
    print(x ** y)

usselIslem(2,4)
usselIslem()

#----------------------------------------

def myLoop(*args):
    for element in args:
        print(element / 2)

myLoop(3,2,1,5,3,4)

#---------------------------------------

def myFunc(num):
    return num ** 3

myList = [2,3,4,5,6]
new_list = [ myFunc(i) for i in myList ]
print(new_list)

#----------------------------------------

barkodDizisi = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]

print(list(filter(lambda string : "XYZ" in string, barkodDizisi)))

#------------------------------------------------

myVar = "Atil Samancioglu"

def ornekFonksiyon():
    myVar = "Atil"
    
    def digerFonksiyon():
        print(myVar)

    digerFonksiyon()

ornekFonksiyon()

#-----------------------------------------

class Kedi():
        
    def __init__(self,isim,yas=5):
        self.isim = isim
        self.yas = yas
        
    def yasiCarp(self):
        return self.yas * 3
kedim = Kedi("Tonton")

print(kedim.yasiCarp())

#-------------------------------------------------

class Ogrenci():
    
    def __init__(self,isim,sinavNotu):
        self.isim = isim
        self.__sinavNotu = sinavNotu
    
    def notuGoster(self):
        print(f"{self.isim} sınav notu: {self.__sinavNotu}")
ogrenci = Ogrenci("Mehmet",85)
ogrenci.__sinavNotu = 75
print(ogrenci.notuGoster())