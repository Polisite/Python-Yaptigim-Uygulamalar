print("""*************************************
Palindrom Sorgulama
*************************************
""")
deger = str(input("Sayı veya Değer giriniz: "))
deger_tersi = deger[::-1]

if deger == deger_tersi:
    print("Palindrom.")
else:
    print("Palindrom değil.")