

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from pandas import DataFrame

#https://phishtank.org/user_submissions.php?page={}&username=cleanmx
urls = ['https://phishtank.org/user_submissions.php?page={}&username=cleanmx'.format(i) for i in range(0,100,1)]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
count =0
df_ret = DataFrame(columns=["url"])

for q in range(0,100,1):
    ret = Request(urls[q], headers=headers)
    res = urlopen(ret)
    contents = res.read()
    soup = BeautifulSoup(contents, "html.parser")
    #print("豆瓣电影TOP250" + "\n" + " 影片名              评分       评价人数     链接 ")

    #df_ret = DataFrame(columns=[" 影片名","评分","评价人数","链接 "])

    
    
    m_u = soup.find_all('td')[1].get_text()
        #exurl=m_u.find('http')
    str='added'
    m_u=m_u[0:m_u.rfind(str)]
    print(m_u)
    df_ret.loc[count] = [m_u]
    count = count +1
    
df_ret.to_csv('badurl.csv', encoding= 'utf-8')


