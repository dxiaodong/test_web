"""
1.操作目标
    1.1 遍历商品列表
    1.2 点击商品列表中所有商品
    1.3 选择任意一个商品进行购买
2.操作思路
    2.1 先定位操作一个商品并点击
    2.2 观察总结每个商品定位的方法和规律
    2.3 元素定位中的属性值可以拼接

"""
# from selenium import webdriver
# import time
# # 打开浏览器和网址
# driver = webdriver.Chrome()
# driver.get('http://ecshop.itsoso.cn/category.php?id=25')
# driver.maximize_window()
# 操作商品列表
#driver.find_element_by_link_text('ssd').click()
"""
一个一个定位操作十分繁琐
driver.find_element_by_xpath('//a[@title = "ssd"]').click()
time.sleep(3)
driver.back()
driver.find_element_by_xpath('//a[@title = "xyy测试手机2"]').click()
time.sleep(3)
driver.back()
"""
# 定位一组元素来操作
# elements = driver.find_elements_by_xpath('//div[@class = "goods-title"]/a')
# print(len(elements))
# goods_titles = []
# for goods in elements:
#     title = goods.get_attribute('title')
#     goods_titles.append(title)
# print(goods_titles)
# for title in goods_titles:
#     driver.find_element_by_xpath(f'//a[@title = "{title}"]').click()
#     time.sleep(3)
#     driver.back()
#
# driver.quit()
from base.base_handle import Base

class GoodsList(Base):
    def get_goods_title(self,locator,attribute):
        """
        获取商品列表的title
        :param locator: 元组--定位一组元素的定位器
        :param attribute: 定位的元素中的属性
        :return: goods_titles
        """
        elements = self.findElements(locator)
        goods_titles = []
        for good_element in elements:
            title = good_element.get_attribute(attribute)
            goods_titles.append(title)
        return goods_titles
    def get_goods_loc(self,locator,attribute):
        """
        获取所有商品列表中所有商品的locator
        :param locator: 定位一组元素的定位器
        :param attribute: 定位的元素中的属性
        :return: goods_locators 所有商品定位器
        """
        goods_titles = self.get_goods_title(locator,attribute)
        goods_locators = []
        for title in goods_titles:
            loc = ('xpath',f'//a[@{attribute} = "{title}"]')
            goods_locators.append(loc)
        return goods_locators
    def click_all_goods(self,locator,attribute):
        """
        遍历点击商品列表所有商品
        :param locator:
        :param attribute:
        :return:
        """
        goods_locators = self.get_goods_loc(locator,attribute)
        for loc in goods_locators:
            self.click(loc)
            self.sleepTime()
            self.back()
    def chioce_goods(self,locator,attribute,goods_name):
        """
        选择指定商品点击查看
        :param locator:
        :param attribute:
        :param goods_name:
        :return:
        """
        goods_titles = self.get_goods_title(locator, attribute)
        goods_locators = self.get_goods_loc(locator, attribute)
        for i in range(len(goods_titles)):
            if goods_titles[i] == goods_name:
                self.click(goods_locators[i])

if __name__ == '__main__':
    from base.browser import open_browser
    driver = open_browser('chrome')
    gl = GoodsList(driver)
    gl.openUrl('http://ecshop.itsoso.cn/category.php?id=35')
    locator = ('xpath','//div[@class = "goods-title"]/a')
    attribute = 'title'
    goods_name = '小米（MI）3USB接口+3孔位 2A快充 插线板'
    #gl.click_all_goods(locator,attribute)
    gl.chioce_goods(locator,attribute,goods_name)
    gl.close()