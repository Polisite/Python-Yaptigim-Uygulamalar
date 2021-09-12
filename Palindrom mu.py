print("""*************************************
Palindrom Sorgulama
*************************************
""")
deger = str(input("Sayı veya Metin giriniz: "))
deger_tersi = deger[::-1]

if deger == deger_tersi:
    print("Palindrom.")
else:
    print("Palindrom değil.")
