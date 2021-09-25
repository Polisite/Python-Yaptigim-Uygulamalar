print("Sözlüğe Hoşgeldiniz")
tercih = input("İngilizce (ing) Sözlük mü ?\t Türkçe (tr) Sözlük mü ?")
if tercih == "ing":
    turkce = {"araba": "car", "elma": "apple", "fare": "mouse"}
    for i in range(int(input("Kaç kelimenin anlamına bakacaksın"))):
        a = input("Hangi kelime ? ")
        print(turkce[a])
elif tercih == "tr":
    turkce = {"car": "araba", "Apple": "elma", "mouse": "fare"}
    for i in range(int(input("Kaç kelimenin anlamına bakacaksın"))):
        a = input("Hangi kelime ? ")
        print(turkce[a])


