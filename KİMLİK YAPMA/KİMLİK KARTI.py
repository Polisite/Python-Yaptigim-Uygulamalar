from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFilter import SHARPEN

temp = Image.open("card.jpg")  # Boş kimlik

foto = "bill.png"  # Kimlik fotoğrafı
tc = "00000000000"
ad = "İLE"
soyad = "PYTHON"
baba = "KİMLİK"
ana = "YAPMA"
dogum_yeri = "SİVEREK"
dogum_tarihi = "01.01.0000"

pic = Image.open(foto).resize((220, 245))
pic = pic.filter(SHARPEN)
temp.paste(pic, (335, 90))

draw = ImageDraw.Draw(temp)

font = ImageFont.truetype('times.ttf', size=25)

draw.text((215, 390), tc, font=font, fill='black')
draw.text((215, 445), soyad, font=font, fill='black')
draw.text((215, 500), ad, font=font, fill='black')
draw.text((215, 555), baba, font=font, fill='black')
draw.text((215, 610), ana, font=font, fill='black')
draw.text((120, 665), dogum_yeri, font=font, fill='black')
draw.text((330, 665), dogum_tarihi, font=font, fill='black')

temp.save("KİMLİKKARTI.png")  # Son hali kaydetme