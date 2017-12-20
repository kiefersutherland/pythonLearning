import requests
 

response = requests.get("http://www.hztongbao.com/app/getCategoryList",  headers={'user-agent':'Mozilla/5.0'})
# print(response.status_code)
 
# for m,n in response.headers.items():
#     print("%s:%s"% (m, n))
#print(response.text)
args = {"ArticleID": 4}
#res=requests.get("http://www.hztongbao.com/home/AppArticle",params= args)
newArgs={"CategoryID":"20170323170634970AD06C08D7BDAF4E76AC9CC2493767C5DC"}
res=requests.get("http://www.hztongbao.com/app/getArticleList", params=newArgs,timeout=2)
#print(res.url)
#print(res.text)
#print(type(res.content))
with open('cc.txt','w') as f:
    f.write(res.text)
    
# r = requests.get('https://www.v2ex.com/api/topics/hot.json')
# print(r.json())