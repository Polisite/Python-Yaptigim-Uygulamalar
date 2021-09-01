# Mehmet Emin, [17.01.21 10:31]
print('KASAYA HOŞGELDİNİZ')
a = input('Birşeyler aldınız mı ? ')
if a == 'e':
    print('''biskivi : 2 tl
kola : 3 tl
kek : 1.5 tl
tost : 7 t
döner : 10 tl
cips : 2 tl''')
    b = input('Ne aldınız ? ')
    if b == 'biskivi':
        c = int(input('Kaçlık masada oturdunuz bir iki üç dört ? '))
        d = float(input('Kaç saat oturdunuz ? '))
        if c == 1:
            print(float(c*d)+2,('ücret ödeyeceksiniz'))
        elif c == 2:
            print(float(c*d)+2,('ücret ödeyeceksiniz'))
        elif c == 3:
            print(float(c*d)+2,('ücret ödeyeceksiniz'))
        elif c == 4:
            print(float(c*d)+2,('ücret ödeyeceksiniz'))
    elif b == 'kola':
        c = float(input('Kaçlık masada oturdunuz ? '))
        d = float(input('Kaç saat oturdunuz ? '))
        if c == 1:
            print(float(c*d)+3,('ücret ödeyeceksiniz'))
        elif c == 2:
            print(float(c*d)+3,('ücret ödeyeceksiniz'))
        elif c == 3:
            print(float(c*d)+3,('ücret ödeyeceksiniz'))
        elif c == 4:
            print(float(c*d)+3,('ücret ödeyeceksiniz'))
    elif b == 'kek':
        c = float(input('Kaçlık masada oturdunuz ? '))
        d = float(input('Kaç saat oturdunuz ? '))
        if c == 1:
            print(float(c*d)+1.5,('ücret ödeyeceksiniz'))
        elif c == 2:
            print(float(c*d)+1.5,('ücret ödeyeceksiniz'))
        elif c == 3:
            print(float(c*d)+1.5,('ücret ödeyeceksiniz'))
        elif c ==4:
            print(float(c*d)+1.5,('ücret ödeyeceksiniz'))
    elif b == 'tost':
        c = float(input('Kaçlık masada oturdunuz ? '))
        d = float(input('Kaç saat oturdunuz ? '))
        if c == 1:
            print(float(c*d)+7,('ücret ödeyeceksiniz'))
        elif c == 2:
            print(float(c*d)+7,('ücret ödeyeceksiniz'))
        elif c == 3:
            print(float(c*d)+7,('ücret ödeyeceksiniz'))
        elif c == 4:
            print(float(c*d)+7,('ücret ödeyeceksiniz'))
    elif b == 'döner':
        c = float(input('Kaçlık masada oturdunuz ? '))
        d = float(input('Kaç saat oturdunuz ? '))
        if c == 1:
            print(float(c*d)+10,('ücret ödeyeceksiniz'))
        elif c == 2:
            print(float(c*d)+10,('ücret ödeyeceksiniz'))
        elif c == 3:
            print(float(c*d)+10,('ücret ödeyeceksiniz'))
        elif c ==4:
            print(float(c*d)+10,('ücret ödeyeceksiniz'))
    elif b == 'cips':
        c = float(input('Kaçlık masada oturdunuz ? '))
        d = float(input('Kaç saat oturdunuz ? '))
        if c == 1:
            print(float(c*d)+2,('ücret ödeyeceksiniz'))
        elif c == 2:
            print(float(c*d)+2,('ücret ödeyeceksiniz'))
        elif c == 3:
            print(float(c*d)+2,('ücret ödeyeceksiniz'))
        elif c == 4:
            print(float(c*d)+2,('ücret ödeyeceksiniz'))
elif a == 'h':
    c = float(input('Kaçlık masada oturdunuz ? '))
    d = float(input('Kaç saat oturdunuz ? '))
    if c == 1:
        print(float(c*d),('TL ücret ödeyeceksiniz'))
    elif c == 2:
        print(float(c*d),('TL ücret ödeyeceksiniz'))
    elif c == 3:
        print(float(c*d),('TL ücret ödeyeceksiniz'))
    elif c == 4:
        print(float(c*d),('TL ücret ödeyeceksiniz'))
else:
    print('Hatalı giriş ')

input('ENTER tuşuna basarak Çıkabilirsiniz')