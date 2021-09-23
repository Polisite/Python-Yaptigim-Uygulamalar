while True:
    tcKimlikNo = input("TC kimlik numarası: (Çıkmak için ENTER e basın): ")
    if tcKimlikNo == "":
        break
    isim = input("isim: ")
    soyisim = input("soyisim: ")
    borc = input("vergi borcu")
    with open("vergi verileri.txt", "a") as fileObject:
        fileObject.write(f"{tcKimlikNo}, {isim}, {soyisim}, {borc}\n")