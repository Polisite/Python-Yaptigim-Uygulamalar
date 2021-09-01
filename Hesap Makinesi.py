# 29.08.2021 12:15
import time
print(time.strftime('%d/%m/%Y'))
print('Hesap Makinesi\n Çarpma=*\n Bölme= /\n Çıkarma=-\n Toplama=+')
i = input('Hangi İşlemi Yapmak istersin ? ')
if i == 'ç':
    a = float(input('1. Sayıyı gir'))
    b = float(input('2. Sayıyı gir'))
    print(a*b)
if i == 'b':
    a = float(input('1. Sayıyı gir'))
    b = float(input('2. Sayıyı gir'))
    print(a/b)
if i == 'x':
    a = float(input('1. Sayıyı gir'))
    b = float(input('2. Sayıyı gir'))
    print(a-b)
if i == 'y':
    a = float(input('1. Sayıyı gir'))
    b = float(input('2. Sayıyı gir'))
    print(a+b)
else:
    print('Hatalı Harf !!! Lütfen Mevcut Harflerden Seçiniz')