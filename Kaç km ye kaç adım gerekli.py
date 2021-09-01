while True:
    print("Kaç Km' ye kaç adım gerekli ? ")
    mesafe = float(input('Mesafeyi Giriniz (km cinsinden): '))
    adım = float(input('Her bir adımınız kaç cm ? : '))
    hesap = float((mesafe*100000)/adım)
    print("Bu kadar adım atmalısınız : ", hesap)
    çıkış = input(print("Çıkmak için 'ç' ya, Tekrar hesaplamak için 'd' ya  basın"))
    if çıkış == "ç":
        print("Çıkılıyor..")
        break
    elif çıkış == 'd':
        continue
        print('Başa dönülüyor')
    else:
        print('Hata')
        break
