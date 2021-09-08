from instabot import *
username = input('k.a: ')
password = input('ş: ')
photo = input('f.a: ')
caption = input('a.: ')

bot = Bot()
bot.login(username=username, password=password)
bot.upload_photo(photo, caption=caption)
print('yüklendi.')
# copy