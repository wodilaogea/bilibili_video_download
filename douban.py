from bs4 import BeautifulSoup
import requests

head={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
for i in range(0,250,25):
    print(i)
    response=requests.get("https://movie.douban.com/top250?start="+str(i)+"&filter=",headers=head)
    content = response.text
    # print(content)
    soup=BeautifulSoup(content,"html.parser")
    allTitle=soup.findAll("span",{"class":"title"})
    for title in allTitle:
        print(title.string)
