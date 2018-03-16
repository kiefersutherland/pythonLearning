import pdfkit
from datetime import  datetime
from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.chrome.options import Options
from PIL import ImageGrab
from selenium.webdriver.support import expected_conditions as EC
import os
import string
from selenium.webdriver.support.wait import WebDriverWait
import requests


# 此函数的作用为生成number位不重复的随机字符串，number最大为62
x="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
def singlerandom(number):
  stringy = ''.join(random.sample(x, number)).replace(' ', '')
  return stringy

def take_screenshot(url, save_fn="capture.png"):
  # pdfkit.from_url('http://www.hztongbao.com', 'out.pdf')

 # response = requests.get(url)

  o = Options()
  o.add_argument('--headless')
  o.add_argument('--disable-gpu')
  # browser = webdriver.Chrome(options=o)
  browser = webdriver.Ie()
  # browser.set_window_size(int(1200), int(900))
  browser.get(url)
  sleep(5)
  browser.execute_script("""
         (function () {
             var y = 0;
             var step = 100;
             window.scroll(0, 0);
         
             function f() {
                 if (y < document.body.scrollHeight) {
                     y += step;
                     window.scroll(0, y);
                     setTimeout(f, 100);
                 } else {
                     window.scroll(0, 0);
                     document.title += "scroll-done";
                 }
             }

             setTimeout(f, 5000);
         })();
     """)

  for i in  range(30):
    if "scroll-done" in browser.title:
      print('滚了')
      break
    sleep(10)
  # title=EC.title_is('预览病历')(browser)
  # print(title)
  #browser.save_screenshot(save_fn)
  # checkcodeimg = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[2]")
  # x1 = checkcodeimg.location['x']
  # y1 = checkcodeimg.location['y']
  # x2 = x1 + checkcodeimg.size['width']
  # y2 = y1 + checkcodeimg.size['height']
  # im = ImageGrab.grab((x1,y1,x2,y2))
  # im.save("F:/1.jpg")
  # print(checkcodeimg)
  browser.get_screenshot_as_file(save_fn)
  # print(browser.page_source)
  # pdfkit.from_string(browser.page_source, filename)
  browser.close()
  browser.quit()
  # print(response.text)
  # pdfkit.from_string(response.text, "out.pdf")
  # pdfkit.from_string(doc.html(), "out.pdf")
  # pdfkit.from_string(response.text, filename)
  # pdfkit.from_url(url, filename)

  # pdfkit.from_url('', 'out.pdf')

if __name__ == "__main__":
  # url="http://www.163.com"
  # filename=str(datetime.now().date().isoformat())+singlerandom(5)+'out.pdf'
  filename=str(datetime.now().date().isoformat())+singlerandom(5)+'out.png'
  url = "http://192.168.69.29:6726/ts/html/x?col=his#$EMRDetailPage$20171023193239930A9597F3B2D79345108FEFE0F77FC1E23C"
  take_screenshot(url,filename)