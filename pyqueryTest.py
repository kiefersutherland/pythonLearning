
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from lxml import etree

for t in range(1,5):
  doc = pq('https://news.cnblogs.com/n/page/'+str(t)+'/')
  #print(doc.html())
  lis=doc('li')
  for li in lis.items():
    #print(li.html())
    pass

  #print(lis.html())
  #print(lis.each(lambda t:t))

  ids=doc('div .content')
  #print(ids)
  for k in ids.items():
    print(k.find('.news_entry').text()+" "+k.find('.entry_footer >span.gray').text()+ "    https://news.cnblogs.com"+ k.find('.news_entry a').attr('href'))

  #print(doc.html())


# cc=pq(etree.fromstring("<html>xx</html>"))
# print(cc.html())