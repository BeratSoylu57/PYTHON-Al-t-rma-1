"""
#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
a= int(input("a:"))
b= int(input("b:"))
c= int(input("c:"))
print("çarpım:{}".format(a*b*c))
"""

"""
#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
boy= float(input("boy:"))
kilo= int(input("kilo:"))
print("Beden Kitle Endeksi:", kilo/ (boy**2))
"""

"""
yakan_miktar = float(input("Kilometrede yaktığı miktar:"))

kilometre = int(input("Kaç km yol yaptınız?"))

print("Tutar: {} tl".format(yakan_miktar * kilometre))
"""

"""
#Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
ad= input("Ad:")
soyad= input("Soyad:")
numara= input("numara:")
print("\nBilgiler...\n")
print("{}\n{}\n{}".format(ad,soyad,numara))
"""

"""
#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
a= int(input("a:"))
b= int(input("b:"))

print("Değiştirilmeden önce değerler\na: {} b: {} \n".format(a,b))

a,b=b,a

print("Değiştirildikten sonra değerler\na: {} b: {} \n".format(a,b))
"""

"""
#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
a= int(input("Uzun Kenar:"))
b= int(input("Kısa Kenar:"))

c= (a**2 + b**2) ** 0.5
print("Hipotenüs:",c)
"""