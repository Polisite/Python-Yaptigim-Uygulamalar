# 2. dereceden denklem = ax**2 + bx + c
# delta hesaplama =  b**2 - 4*a*c

#Δ(delta) > 0 ise denklemin iki kökü var.
#delta = b**2 - 4*a*c
# x1 = (-b + (delta ** 0.5)) / (2*a)
#x2 = (-b - (delta ** 0.5)) / (2*a)

#Δ = 0 ise birbirine eşit iki kök vardır.
# x1=x2= (-b/2*a)

#Δ < 0 ise denklemin reel sayılarda çözümü yoktur.

while True:
    print("2. Dereceden Bir Denklemin Köklerini Bulma")
    print("DENKLEM: ax**2 + bx + c")
    a = int(input('a değerini giriniz: '))
    b = int(input('b değerini giriniz: '))
    c = int(input('c değerini giriniz: '))
    delta = b**2 - 4*a*c
    if delta == delta > 0:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        print("Denklemin iki Kökü Vardır.\n 1. Kök: ", x1, 'İkinci Kök: ', x2)
        çıkış = input(print("Çıkmak için 'q' ya, Tekrar hesaplamak için 'w' ya  basın "))
        if çıkış == "q":
            print("Çıkılıyor..")
            break
        elif çıkış == 'w':
            continue
            print('Başa dönülüyor')
        else:
            print('Hata')
            break
    elif delta == delta == 0:
        x1 = x2 = (-b / 2 * a)
        print("Denklemin Çakışık Bir Kökü Vardır: ", x1)
        çıkış = input(print("Çıkmak için 'q' ya, Tekrar hesaplamak için 'w' ya  basın "))
        if çıkış == "q":
            print("Çıkılıyor..")
            break
        elif çıkış == 'w':
            continue
            print('Başa dönülüyor')
        else:
            print('Hata')
            break
    elif delta == delta < 0:
        print("Denklemin Reel Sayılarda Bir Kökü Bulunmamatadır.")
        çıkış = input(print("Çıkmak için 'q' ya, Tekrar hesaplamak için 'w' ya  basın "))
        if çıkış == "q":
            print("Çıkılıyor..")
            break
        elif çıkış == 'w':
            continue
            print('Başa dönülüyor')
        else:
            print('Hata')
            break
    else:
        print("hatalı")

