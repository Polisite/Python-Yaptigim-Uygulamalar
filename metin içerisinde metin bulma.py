text = input("Metini giriniz: ")
searchPhrase = input("Aranacak metin: ")

index = text.find(searchPhrase)
if index < 0:
    print("Metin içinde bulunamadı")
else:
    resultString = text[index:index + len(searchPhrase)]  # index -1 len(searchPhrase) +1
    print(resultString)
