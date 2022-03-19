import csv




csv_file=csv.reader(open("badurl.csv","r"))
url=[]
for u in csv_file:
    url.append(u)
long=0
print(str(url[1]))
#for i in range(0,1000):
#    long=long+len(str(url[i]))
#print(long/1000)
