# from selenium.webdriver import Chrome
# web=Chrome()
# web.get("www.baidu.com")
# from collections import defaultdict
# class DoubanMovieTop:
#     def __init__(self):
#         self.top_urls = ["https://movie.douban.com/top250?start={0}&filter=".format(x * 25) for x in range(10)]
#         self.data = defaultdict(list)
#         self.columns = ['title', 'link', 'score', 'score_cnt', 'top_no', 'director', 'writers', 'actors', 'types',
#                         'edit_location', 'language', 'dates', 'play_location', 'length', 'rating_per', 'betters',
#                         'had_seen', 'want_see', 'tags', 'short_review', 'review', 'ask', 'discussion']
#         self.df = None
# if __name__ == '__main__':
#     douban=DoubanMovieTop()
#     print(douban.top_urls)
comments = [i for i in range(10)]
comments.append(10)
print(comments)