while True:
    print("Kaç km yol yürüdün ? ")
    print(' ')
    print(' ')
    print(' ')
    adım = float(input('Bugün kaç adım attın ? : ' ))
    uzunluk = float(input('Her bir adımın kaç cm ? : '))
    mesafe = float(adım*uzunluk)
    print(mesafe,'cm ')
    print(mesafe/100,'m ')
    print(mesafe/100000, 'sonuç olarak km yol kat etmişsin')
    çıkış = input(print("Çıkmak için 'q' ya, Tekrar hesaplamak için 'w' ya  basın "))
    if çıkış == "q":
        print("Çıkılıyor..")
        break
    elif çıkış == 'w':
        continue
        print('Başa dönülüyor ')
    else:
        print('Hata')







