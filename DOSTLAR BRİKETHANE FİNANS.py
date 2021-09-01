print('DOSTLAR BRİKETHANE Finans Sayfasına  Hoşgeldiniz.')
iş = input('Bugün Sac Çıkardınız mı ? ')
if iş == 'e':
    sac = float(input('Kaç sac çıkardınız ? '))
    yükleme = input('Yükleme yaptınız mı ? ')
    if yükleme == 'e':
        pirket = float(input('Kaç pirket yüklediniz ? '))
        kişi = float(input('Kaç kişiydiniz ? '))
        yüklemeparası = (pirket*0.10)/kişi
        indirme = input('İndirme Yaptınız mı ? ')
        if indirme == 'e':
            a = float(input('Kaç pirket indirdiniz ? '))
            b = float(input('Kaç kişiydiniz ? '))
            indirmeparası = (a*0.10)/b
            print((sac*0.18)+yüklemeparası+indirmeparası,'TL kazandınız.')
        elif indirme == 'h':
            print((sac*0.18)+yüklemeparası,'TL kazandınız.' )
        else:
            print('Hatalı giriş')
    elif yükleme == 'h':
        indirme = input('İndirme Yaptınız mı ? ')
        if indirme == 'e':
            a = float(input('Kaç pirket indirdiniz ? '))
            b = float(input('Kaç kişiydiniz ? '))
            indirmeparası = (a * 0.10) / b
            print((sac * 0.18) + indirmeparası, 'TL kazandınız.')
        elif indirme == 'h':
            print((sac * 0.18), 'TL kazandınız.')
        else:
            print('Hatalı giriş')
    else:
        print('Hatalı giriş')
elif iş == 'h':
    yükleme = input('Yükleme yaptınız mı ? ')
    if yükleme == 'e':
        pirket = float(input('Kaç pirket yüklediniz ? '))
        kişi = float(input('Kaç kişiydiniz ? '))
        yüklemeparası = (pirket * 0.10) / kişi
        indirme = input('İndirme Yaptınız mı ? ')
        if indirme == 'e':
            a = float(input('Kaç pirket indirdiniz ? '))
            b = float(input('Kaç kişiydiniz ? '))
            indirmeparası = (a * 0.10) / b
            print(yüklemeparası + indirmeparası, 'TL kazandınız.')
        elif indirme == 'h':
            print(yüklemeparası, 'TL kazandınız.')
        else:
            print('Hatalı giriş')
    elif yükleme == 'h':
        indirme = input('İndirme Yaptınız mı ? ')
        if indirme == 'e':
            a = float(input('Kaç pirket indirdiniz ? '))
            b = float(input('Kaç kişiydiniz ? '))
            indirmeparası = (a * 0.10) / b
            print(indirmeparası, 'TL kazandınız.')
        elif indirme == 'h':
            print('OHH Saldım Çayıra Mevlam Kayıra')
        else:
            print('Hatalı giriş')
    else:
        print('Hatalı giriş')
else:
    print('Hatalı giriş')

