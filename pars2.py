import requests
from bs4 import BeautifulSoup

url = "https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php"

response = requests.get(url)

soup = BeautifulSoup(response.text,"lxml")


data = soup.find("div", id = "pagecontent")
data_ul = data.find_all("ul")
file = open("кафедры.txt","w")
for i in data_ul:
    name = i.find("li").text
    file.write(name)

file.close()