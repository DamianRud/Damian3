# andmetüüp
# muutujad


# arv1=int(input("sisesta arv1:"))
# arv2=int(input("sisesta arv2:"))
# tulemus = arv1 + arv2
# print("text")

#ülesandeid 1

arv1 = int(input("sisesta esimene arv1"))
arv2 = int(input("sisesta teine arv2"))

summa = arv1+arv2
vahe = arv1-arv2
korritus = arv1*arv2

print("Esimene ja teise arvu summa:",summa)
print("Esimine ja teise arvu vahe:",vahe)
print("Esimine ja teise arvu korritus",korritus)

#Ülesandeid 2

aasta = 2025

nimi = input("sisesta oma nimi: ")
vanus = int(input("sisesta oma vanus:"))

sünniaasta = aasta-vanus

print (f"Tere,{nimi}")
print(f"sinu sünniaasta on ilmselt{sünniaasta}")

#Ülesandeid 3

a = int(input("sisesta esimene arv (a):"))
b = int(input("sisesta teine arv (b):"))
print(f"Enne vahetamist a={a},b={b}")

a = a+b
b = a-b
a = a-b
print(f"Peale vahetamist: a={a},b={b}")

#Ülesandeid 4

s = int(input("sisesta sekundid:"))
if s<0:
    print("vigane sisend:")
else:
 t = s // 3600
 m =(s%3600)//60
 s = s%60
 print(f"{t:02}:{m:02}:{s:02}")

#Ülesandeid 5

#firma = "National Airline"
#laius = 40

#number = input("Sisesta lennu number:")
#Väljumislennujaama = input("sisesta Väljumislennujaama kood:")
#Sihtlennujaama = input ("sisesta Sihtlennujaama kood:")
#väljumise_aeg = input("sisesta väljumise aeg(TT:MM):")

#tunnid = int(väljumise_aeg)
#minutid =int(väljumise_aeg)




 
 
 
       