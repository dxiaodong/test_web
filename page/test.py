from selenium import webdriver
from time import sleep


url = "http://ecshop.itsoso.cn/goods.php?id=55"
driver = webdriver.Firefox()
driver.get(url)
goods_name = "移动电源10000mAh"
sleep(3)
element1 = driver.find_element_by_xpath("//*[@id='ur_here']/div/div")
print(element1.text)

element2 = driver.find_element_by_class_name("goods_style_name")
print(element2.text)
element3 = driver.find_element_by_xpath("//*[@class='td1']/a/img")
element3.click()
sleep(5)
driver.quit()
"""
import re
a = "当前位置: 首页 > 手机 > 移动电源10000mAh"
print(len(a))
match = re.compile("手机 > (\S+)").search(a)
if match is not None:
    print(match.group(1))
"""





