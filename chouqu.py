import random
from random import randint
 
oldf=open('top-1m-2.csv','r',encoding='UTF-8')
newf=open('goodurl.csv','w',encoding='UTF-8')
n = 0
# sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素
resultList = random.sample(range(0,896343),1000)

lines=oldf.readlines()
for i in resultList:
    newf.write(lines[i])