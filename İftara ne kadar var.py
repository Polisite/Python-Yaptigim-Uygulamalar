import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = {"User-Agent": "Mozilla/5.0"}
url = "https://www.vakitci.com/turkiye/sanliurfa/"

content = requests.get(url, headers=headers).content
soup = BeautifulSoup(content, "html.parser")

result = soup.find("div", attrs={"id": "aksam"}).find_all("div")[1].text
hour, minute = result.split(":")

date1 = datetime.now()
date2 = datetime(date1.year, date1.month, date1.day,
                 int(hour), int(minute), date1.second)

difference = str(date2 - date1).split(".")[0]
print(difference)
# .....
