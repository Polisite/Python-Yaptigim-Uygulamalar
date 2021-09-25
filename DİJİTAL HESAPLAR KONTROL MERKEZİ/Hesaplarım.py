print("""*************************************
DİJİTAL HESAPLAR KONTROL MERKEZİ
*************************************
""")


def hesap_ekleme():
    kayit_yeri = input("Nereye kaydoldunuz ?\t")
    e_posta = input("Hangi e-posta ile kayıt oldunuz:\t")
    tlf = input("Hangi numara ile kayıt oldunuz veya hangi numrayı kurtarma numarası olarak ayarladınız:\t")
    k_adi = input("Kullanıcı adınızı giriniz:\t")
    sifre = input("Şifrenizi giriniz:\t")
    hesaplar = open("Hesaplar.txt", "a")
    hesaplar.write(kayit_yeri + "\n" + "e-posta: " + e_posta + "\t" + "telefon: " + tlf + "\t" + "kullanıcı adı: " + k_adi + "\t" + "şifre: " + sifre + "\n")
    hesaplar.close()


def hesaplari_gormek():
    hesaplar = open("hesaplar.txt", "r", encoding="utf-8")
    print(hesaplar.read())


while True:
    islemler = int(input("Ne yapmak istersiniz:\n 1 = Hesap Eklemek.\n 2 = Hesapları Görmek.\n Sistemden Çıkış Yapmak İçin 3 e Basın:\t"))
    if islemler == 1:
        print("Hesap Eklemek")
        hesap_ekleme()
    elif islemler == 2:
        print("Hesapları Görmek")
        hesaplari_gormek()

    elif islemler == 3:
        print("Çıkış yapıldı.")
        break
    else:
        print("Geçerli bir işlme numarası girmediniz...")
