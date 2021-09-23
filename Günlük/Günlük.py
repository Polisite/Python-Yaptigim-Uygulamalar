
kullanici_adi = "m"
sifre = "1"

giris_hakki = 3

while True:
    k_a = input("Kullanıcı adı giriniz: ")
    k_s = input("Sifreyi giriniz: ")
    if k_a == kullanici_adi and k_s == sifre:
        print("sisteme başarıyla giriş yapıldı.")
        a = int(input("""Neler yapmak istersiniz:\n
        1 = Yeni bir günlük yazmak\n
        2 = Olan bir sayfayı düzenlemek\n
        3 = Çıkış yapmak: """))

        while True:
            if a == 1:
                dosya = open(input("Günlüğüne isim ver (.txt yapmayı unutma): "), "w")
                dosya.write(input("Bişeyler yaz... :"))
                break
            elif a == 2:
                dosya = open(input("Hangi dosyayı açmak istersin ? (.txt yapmayı unutma): "), "a")
                dosya.write(input("  Bişeyler yaz... : "))
                break
            elif a == 3:
                break
            elif a > 3:
                a = int(input("Hatalı giriş. İşlem kodları:\n 1\n 2\n 3\n bunlardan birini seçiniz."))
    else:
        giris_hakki -= 1
        if giris_hakki > 0:
            print("Kullanıcı adı hatalı tekrar giriş yap")
        else:
            print("Hakkınız bitti. eve dönün")
            break
