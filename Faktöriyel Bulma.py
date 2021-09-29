print("""*************************************
Faktöriyel Bulma Programı \n
*************************************
""")
faktöriyel = 1
sayi = int(input("Hangi sayının faktöriyelini bulmak istersiniz :  "))
for i in range(1, sayi+1):
    faktöriyel *= i
print("faktöriyel ", faktöriyel)
    