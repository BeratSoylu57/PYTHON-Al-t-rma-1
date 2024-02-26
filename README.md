"""
#Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
boy = float(input("Boyunuzu Giriniz (m):"))
kilo = int(input("Kilonuzu Giriniz (kg):"))

BKI= kilo / (boy ** 2)
if (BKI < 18.5):
    print("Zayıf")
elif (BKI >= 18.5 and BKI < 25):
    print("Normal")
elif (BKI >= 25 and BKI < 30):
    print("Fazla Kİlolu")
else:
    print("obez")
"""

"""
#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
a= int(input("a:"))
b= int(input("b:"))
c= int(input("c:"))

if(a >= b and a >=c):
    print("En Büyük Sayı:",a)
elif(b >= a and b >=c):
    print("En Büyük Sayı:",b)
elif(c >= a and c >= b):
    print("En Büyük Sayı:",c)
"""

"""
#Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
vize1= int(input("Vize1:"))
vize2= int(input("Vize2:"))
final= int(input("Final:"))
genel_not= vize1 * 3/10 + vize2 * 3/10 + final * 4/10
if(genel_not >= 90):
    print("AA")
elif(genel_not >= 85):
    print("BA")
elif(genel_not >= 80):
    print("BB")
elif(genel_not >= 75):
    print("CB")
elif(genel_not >= 70):
    print("CC")
elif(genel_not >= 65):
    print("DC")
elif(genel_not >= 60):
    print("DD")
elif(genel_not >= 55):
    print("FD")
else:
    print("FF")
"""
"""
Şekil= input("Hangi Şeklin Tipini Öğrenmek İstiyorsunuz?")

if(Şekil == "Dikdörtgen"):
    print("Lütfen Kenarları Girin...")
    a= int(input("Kenar-1:"))
    b= int(input("Kenar-2:"))
    c= int(input("Kenar-3:"))
    d= int(input("Kenar-4:"))
    
    if(a==b and a==c and a==d):
        print("Kare")
    elif(a==c and b==d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")

elif(Şekil== "Üçgen"):
    print("Lütfen Kenarları Giriniz:")
    a= int(input("Kenar-1:"))
    b= int(input("Kenar-2:"))
    c= int(input("Kenar-3:"))

    if( abs(a+b)>c and abs(a+c)> b and abs(b+c)>a):
        if(a==b and a==c):
            print("Eşkenar Üçgen")
        elif((a==b and a!=c)or(a==c and a!=b)or(b==c and b!=a)):
            print("İkizkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")
    else:
        print("Üçgen Belirtmiyor...")

else:
    print("Geçersiz Şekil...")
"""
"""
print(""
---------------------------------
Hesap Makinesi Programı

İşlemler:
      
1. Toplama İşlemi
      
2. Çıkarma işlemi

3. Çarpma işlemi

4. Bölme işlemi
---------------------------------
"")

a= int(input("Birinci Sayıyı Giriniz:"))
b= int(input("İkinci Sayıyı Giriniz:"))

işlem= input("İşlemi Giriniz:")
if(işlem == "1"):
    print("{} ile {} toplamı {} dir.".format(a,b,a+b))
elif(işlem == "2"):
    print("{} ile {} farkı {} dir.".format(a,b,a-b))
elif(işlem == "3"):
    print("{} ile {} çarpımı {} dir.".format(a,b,a*b))
elif(işlem == "4"):
    print("{} ile {} bölümü {} dir.".format(a,b,a/b))
else:
    print("Lütfen geçerli bir işlem girin...")
"""


"""
print(""*********************
Kullanıcı Girişi
*********************
"")

sys_kullanıcı_adı= "mmurat"
sys_parola= "12345"

kullanıcı_adı: input("Kullanıcı Adı:")
parola= input("Parola:")

if (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
    print("Parola Hatalı...")

elif(kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
    print("Kullanıcı Adı Hatalı...")
elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    print("Kullanıcı Adı ve Parola Hatalı...")
else:
    print("Sisteme Başarıyla Giriş Yapıldı...")
"""
