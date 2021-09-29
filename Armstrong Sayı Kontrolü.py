işlemler = input("""*************************************
Armstrong Sayı Kontrol Programı

işlemler:
q = Çıkış
1 = işlem
*************************************
""")

while True:
    if işlemler == "q":
        break
    elif işlemler == "1":
        a_s = input("Bir sayı gir:    ")
        basamak_sayısı = len(a_s)
        toplam = 0
        for i in a_s:
            sonuc = int(i) ** int(basamak_sayısı)
            toplam += sonuc
        if toplam == int(a_s):
            print("Amstrong sayı")
        else:
            print("Amstrong sayı değil")
    else:
        print("hatalı giriş")
    
