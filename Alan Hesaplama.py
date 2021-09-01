while True:
    print('Geometrik Şekillerin Alanını Bulma: ')
    şekil = input('Hangi Şeklin Alanını Hesaplamak İstersin :\n 1-Kare\n 2-Üçgen\n 3-Dikdörtgen\n 4-Küre: (Çıkmak için q ya basın) ')
    if şekil == "q":
        print("Çıkılıyor..")
        break
    elif şekil == '1':
        print('KARE')
        kare = float(input('Bir kenara ait uzunluğu girin (cm cinsinden): '))
        a = float(kare*kare)
        print('Alan',a,'cm')
        print('Alan',a/100,'m')

    elif şekil == '2':
        print('ÜÇGEN')
        taban = float(input('Tabana ait uzunluk (cm cinsinden): '))
        yükseklik = float(input('Yüksekliğe ait uzunluk (cm cinsinden): '))
        a =(taban*yükseklik)/2
        print('Alan', a, 'cm')
        print('Alan', a / 100, 'm')
    elif şekil == '3':
        print('DİKDÖRTGEN')
        kenar1 = float(input('Uzun kenara ait uzunluğu giriniz (cm cinsinden): '))
        kenar2 = float(input('Kısa kenara ait uzunluğu giriniz (cm cinsinden): '))
        a =kenar1 * kenar2
        print('Alan', a, 'cm')
        print('Alan', a / 100, 'm')
    elif şekil == '4':
        print('KÜRE')
        pi = float(input('Pi sayısını giriniz: '))
        yarıçap = float(input('Yarıçapı giriniz (cm cinsinden): '))
        a =(pi*yarıçap**3)*(4/3)
        print('Alan', a, 'cm')
        print('Alan', a / 100, 'm')
    else:
        print('Ya 1\' i ya 2\' yi ya 3\'ü ya da 4\' ü tuşlayın.')