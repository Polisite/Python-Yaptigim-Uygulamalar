print("""*************************************
Adın Kaç Harfli Ve Hangi Harf Kaç Defa Geçiyor \n
*************************************
""")

sisteme_kayıtlı_kullanıcı_adı = "a"
sisteme_kayıtlı_kullanıcı_şifresi = "a"

giriş_hakkı = 3

while True:
    girilen_kullanıcı_adı = input("Kullanıcı adınızı giriniz: ")
    girilen_kullanıcı_şifresi = input("Şifrenizi giriniz: ")

    if sisteme_kayıtlı_kullanıcı_adı != girilen_kullanıcı_adı and sisteme_kayıtlı_kullanıcı_şifresi == girilen_kullanıcı_şifresi:
        print("Kullanıcı adı hatalı girildi !!!")
        giriş_hakkı -= 1
    elif sisteme_kayıtlı_kullanıcı_adı == girilen_kullanıcı_adı and sisteme_kayıtlı_kullanıcı_şifresi != girilen_kullanıcı_şifresi:
        print("Şifre hatalı girildi !!!")
        giriş_hakkı -= 1
    elif sisteme_kayıtlı_kullanıcı_adı != girilen_kullanıcı_adı and sisteme_kayıtlı_kullanıcı_şifresi != girilen_kullanıcı_şifresi:
        print("Kullanıcı adı ve Şifre hatalı girildi !!!")
        giriş_hakkı -= 1
    else:
        print("Sisteme başarıyla giriş yapıldı")
    if giriş_hakkı == 0:
        print("Çok fazla hatalı giriş")
        break
