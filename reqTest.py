import requests
from bs4 import BeautifulSoup
import re   #正则

def fun(m):
    img_tag = m.group()
    src = m.group(1)
    if not src.startswith("http:"):
        full_src = "http://www.icoa.cn" + src
    else:
        full_src = src
    new_img_tag = img_tag.replace(src, full_src)
    return new_img_tag


response = requests.get("http://www.icoa.cn/a/512.html",  headers={'user-agent':'Mozilla/5.0'})
# print(response.status_code)
soup=BeautifulSoup(response.text,"html.parser")
# print(soup.title)
# print(soup.body.p.string)
# print(soup.body.p.get_text())
# print(soup.find_all("p","qrcode-name"))
#print(soup.find_all("img"))
#print(soup.find_all(src=re.compile("^http")))

cc=str(soup.find_all("img"))
rex=r'<img.*?src="(.*?)">'
new=re.findall(rex,cc)
#print(new)

a=re.findall(rex,cc)
# print(a)

k=re.sub(rex,fun,cc)
print(k)

# for m,n in response.headers.items():
#     print("%s:%s"% (m, n))
#print(response.text)
args = {"ArticleID": 4}
#res=requests.get("http://www.hztongbao.com/home/AppArticle",params= args)
newArgs={"CategoryID":"20170323170634970AD06C08D7BDAF4E76AC9CC2493767C5DC"}
#res=requests.get("http://www.hztongbao.com/app/getArticleList", params=newArgs,timeout=2)
#print(res.url)
#print(res.text)


#print(type(res.content))
# with open('cc.txt','w') as f:
#     f.write(res.text)
    
# r = requests.get('https://www.v2ex.com/api/topics/hot.json')
# print(r.json())