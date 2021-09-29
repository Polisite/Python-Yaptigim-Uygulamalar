print("""*************************************
Faktöriyel Bulma Programı \n
*************************************
""")

a = 1
b = 1

fibonacci = [a,b]

for i in range(int(input("Kaç elmanlı bir fibonacci serisi istiyorsun:  "))):
    a,b = b, a+b
    fibonacci.append(b)
print(fibonacci)