

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from pandas import DataFrame


urls = ['https://movie.douban.com/top250?start={}&filter='.format(i) for i in range(0,250,25)]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
count =0
print("豆瓣电影TOP250" + "\n" + " 影片名              评分       评价人数     链接 ")
df_ret = DataFrame(columns=[" 影片名","评分","评价人数","链接 "])

for q in range(0,10,1):
    ret = Request(urls[q], headers=headers)
    res = urlopen(ret)
    contents = res.read()
    soup = BeautifulSoup(contents, "html.parser")
    #print("豆瓣电影TOP250" + "\n" + " 影片名              评分       评价人数     链接 ")

    #df_ret = DataFrame(columns=[" 影片名","评分","评价人数","链接 "])

    
    for tag in soup.find_all('div', class_='info'):
        m_name = tag.find('span', class_='title').get_text()
        m_rating_score = float(tag.find('span', class_='rating_num').get_text())
        m_people = tag.find('div', class_="star")
        m_span = m_people.findAll('span')
        m_peoplecount = m_span[3].contents[0]
        m_url = tag.find('a').get('href')
        print(m_name + "        " + str(m_rating_score) + "           " + m_peoplecount + "    " + m_url)
        df_ret.loc[count] = [m_name, str(m_rating_score),m_peoplecount, m_url]
        count = count +1
    # 保存输出结果到csv
df_ret.to_csv('movies_names_set.csv', encoding= 'gbk')
#print(df_ret.head())

