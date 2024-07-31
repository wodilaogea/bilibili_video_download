import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import defaultdict
import pandas as pd

head={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

class DoubanMovieTop:
    def __init__(self):
        self.top_urls = ["https://movie.douban.com/top250?start={0}&filter=".format(x * 25) for x in range(10)]
        self.data = defaultdict(list)
        self.columns = ['rank','title', 'titles0', 'link', 'score', 'score_cnt', 'account', 'comment']
        self.df = None

    def get_bsobj(self, url):#获取返回页面
        request = urllib.request.Request(url=url,headers = head)
        response = urllib.request.urlopen(request)
        html_data = response.read().decode('utf - 8')
        bsobj = BeautifulSoup(html_data, 'html.parser')#lxml
        # html = urlopen(url).read().decode('utf-8')
        # bsobj = BeautifulSoup(html, 'lxml')
        return bsobj

    def get_info(self):#提取信息
        for url in self.top_urls:
            bsobj = self.get_bsobj(url)
            main = bsobj.find('ol', {'class': 'grid_view'})
            # 排名
            rank_objs = main.findAll('div', {'class':'pic'})
            ranks = [i.find('em').text for i in rank_objs]
            print(ranks)
            # 标题及链接信息
            title_objs = main.findAll('div', {'class': 'hd'})
            titles = [i.find('span').text for i in title_objs]
            print(titles)
            #外文名
            titles0s = [i.findAll('span')[1].text.replace('\xa0','') for i in title_objs]#.replace('\xa0/\xa0','')
            print(titles0s)
            links = [i.find('a')['href'] for i in title_objs]
            # 评分信息
            score_objs = main.findAll('div', {'class': 'star'})
            scores = [i.find('span', {'class': 'rating_num'}).text for i in score_objs]
            print(scores)
            score_cnts = [i.findAll('span')[-1].text for i in score_objs]
            print(score_cnts)
            #概述：导演等
            account_objs = main.findAll('div', {'class': 'bd'})
            accounts = [i.find('p').text.replace('\xa0','').replace(' ','').replace('\n','') for i in account_objs]#.replace(' ','').replace('\n','')
            print(accounts)
            #概评
            comment_objs = main.findAll('div', {'class': 'bd'})
            # comments = [i.find('span', {'class': 'inq'}).text for i in comment_objs]
            comments = []
            for i in comment_objs:
                if(i.find('span', {'class': 'inq'})):
                    comments.append(i.find('span', {'class': 'inq'}).text)
                else:
                    comments.append(' ')
            print(comments)
            for rank,title, titles0, link, score, score_cnt, account, comment in zip(ranks,titles, titles0s, links, scores, score_cnts, accounts, comments):
                self.data[title].extend([rank,title, titles0, link, score, score_cnt, account, comment])
                # bsobj_more = self.get_bsobj(link)
                # more_data = self.get_more_info(bsobj_more)
                # self.data[title].extend(more_data)
                print(self.data[title])
                print(len(self.data))
                # time.sleep(0.1)

    def dump_data(self):#保存csv文件
        data = []
        for title, value in self.data.items():
            data.append(value)
        self.df = pd.DataFrame(data, columns=self.columns)
        self.df.to_csv('douban_top250.csv', index=False)

    # def get_more_info(self, bsobj_more):
    #     return ''


if __name__ == '__main__':
    douban = DoubanMovieTop()
    douban.get_info()
    douban.dump_data()
