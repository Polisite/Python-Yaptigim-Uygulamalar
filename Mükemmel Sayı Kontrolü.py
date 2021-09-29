işlem = input("""işlemler:
q = Çıkmak İçin
1 = İşlem yapmak için   """)





while True:
    if işlem == "q":
        print("Çıkış Yapıldı.")
        break
    if işlem == "1":
        a = int(input("Sayı gir:    "))
        t = 0
        for i in range(1,a):
            if a % i == 0:
                t += i
        if a == t:
            print("Girilen Sayı Mükemmel Sayı")
        else:
            print("Girilen sayı mükemmel sayı değil")
        
    
    


