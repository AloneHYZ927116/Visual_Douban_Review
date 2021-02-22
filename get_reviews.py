# 一个定量获取豆瓣电影评论的函数


import requests
from bs4 import BeautifulSoup


def get_reviews(all_reviews_url_str, num_analysis_int):
    # 功能：一个定量获取豆瓣电影评论的函数
    # 形参：all_reviews_url_str[str]:豆瓣上电影全部评论的http网址
    # 形参：num_analysis_int[int]:用户想分析的评论个数
    # 返回值：未定
    if num_analysis_int == None:
        # 默认为100个
        num_analysis_int = 100
    # 得到评论网址的共同url，可用于获取下一页评论
    serve_url_str = all_reviews_url_str.split('?')
    # print(type(serve_url_str))
    # print(serve_url_str)
    req = requests.get(url=all_reviews_url_str)
    # print(req)
    html_str = req.text
    # print(type(html_str))
    # print(html_str)
    bs = BeautifulSoup(html_str, 'lxml')
    # 获取本页所有评论
    comment_content_list = bs.find_all('div', class_='comment-item')
    print(len(comment_content_list))


if __name__ == '__main__':
    get_reviews('https://movie.douban.com/subject/34841067/comments?limit=20&status=P&sort=new_score', 100)
    print('\nAll done')
