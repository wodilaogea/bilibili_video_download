import requests
from bs4 import BeautifulSoup

head={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Cookie":"newstatisticUUID=1683203757_741130756; _csrfToken=ZYsNzrLud0XlOCV4mJbFgRaYvJ0hosRTP6xmPKth; fu=967754071; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; supportwebp=true; supportWebp=true; rcr=1031492038%2C1031299526%2C1034928609; navWelfareTime=1684565016690; lrbc=1031492038%7C688124976%7C0%2C1031299526%7C680574508%7C0%2C1034928609%7C724882745%7C0; Hm_lvt_f00f67093ce2f38f215010b699629083=1701595441,1703036816,1703159234,1703688589; traffic_utm_referer=; _gid=GA1.2.1873823329.1703688590; _gat_gtag_UA_199934072_2=1; ywguid=2734905941; ywkey=ywLnlISjfw3g; ywopenid=6B8288CC22793AAF122FC9067BE10D35; Hm_lpvt_f00f67093ce2f38f215010b699629083=1703688610; _ga_FZMMH98S83=GS1.1.1703688589.26.1.1703688609.0.0.0; _ga=GA1.1.109890904.1683203758; _ga_PFYW0QLV3P=GS1.1.1703688589.26.1.1703688609.0.0.0",
    "Referer":"https://ptlogin.qidian.com/"
}
url="https://www.qidian.com/chapter/1037418255/776241240/"
resp=requests.get(url,headers=head)
main_text=BeautifulSoup(resp.text,"html.parser")
print(resp.text)
# text=main_text.find("main",class_="content mt-1.5em text-s-gray-900 leading-[1.8] relative z-0 r-font-black").findAll("p")
# for item in text:
#     print(item.get_text())
# alist=main_text.find("main",id="c-705291131").findAll("p")
# print(alist)