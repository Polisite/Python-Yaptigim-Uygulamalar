import time
print("""*************************************
ATM Makinasına Hoşgeldiniz\n

işlemler:\n
1 = Bakiye Sorgulama\n
2 = Para Yatırma\n
3 = Para Çekme\n

Programdan Çıkmak İçin Klavyede 'q' ya basın.
*************************************
""")

bakiye = 0


while True:
    işlem = input("İşlem seçiniz:   ")
    if (işlem == "q"):
        print("Programdan Çıkıldı")
        break

    elif işlem == "1":
        print("Bakiyeniz {} tl dir".format(bakiye))

    elif işlem == "2":
        yatırılacak_tutar = float(input("Ne kadar para yatıracaksınız:  "))
        bakiye += yatırılacak_tutar
        print("Yatırmak İstediğiniz Miktar Başarıya Yatırıldı ")

    elif işlem == "3":
        çekilecek_tutar = float(input("Ne kadar para çekeceksiniz:  "))
        if çekilecek_tutar > bakiye:
            print("Yetersiz Bakiye")
            continue
        bakiye -= çekilecek_tutar
        print("Önce Kartınızı Alınız.\n Bekleyiniz...")
        time.sleep(5)
        print("Şimdide Paranızı Alınız")

    else:
        print("Hatalı işlem kodu.")
