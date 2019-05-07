from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
"""
page object:--base类
    1.浏览器打开方式
    2.打开被测网址
    3.封装元素定位方法
    4.封装元素操作方法
        4.1点击
        4.2输入
    5.判断元素是否存在
    6.关闭浏览器
    ...
    鼠标事件
    下拉框
    frame
    单选框复选框
"""
class Base:
    def __init__(self,dirver):
        """初始化"""
        self.driver = dirver
    def openUrl(self,url):
        # 浏览器最大化
        self.driver.maximize_window()
        self.driver.get(url)
        self.sleepTime()
    def findElement(self,locator,timeout=10):
        """
        封装元素定位方法
        :param locator:是一个元组,例:("link text","请登录")
        :param timeout:设置超时时间
        :return element元素
        """
        element = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        return element
    def findElements(self,locator,timeout=10):
        """
        封装定位一组元素方法
        :param locator:是一个元组,例:("link text","请登录")
        :param timeout:设置超时时间
        :return element元素
        """
        elements = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_all_elements_located(locator))
        return elements
    def click(self,locator):
        """封装元素操作方法--点击"""
        element = self.findElement(locator)
        element.click()
    def sendKeys(self,locator,text):
        """
        元素操作方法--输入
        :param locator: 一个元组,例:("link text","请登录")
        :param text: 需要输入的内容
        :return:
        """
        element = self.findElement(locator)
        element.clear()
        element.send_keys(text)

    def isTextInElement(self,locator,text,timeout=10):
        """利用文本判断元素是否存在,如果不存在,则返回False,如果存在则返回result"""
        try:
            result = WebDriverWait(self.driver, timeout,1).until(EC.text_to_be_present_in_element(locator, text))
        except:
            print("元素不存在" + str(locator))
            return False
        else:
            return result
    def isTextInValue(self,locator,text,timeout=10):
        """利用元素属性值判断元素是否存在,如果不存在,则返回False,如果存在则返回result"""
        try:
            result = WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element_value(locator,text))

        except:
            print("元素不存在" + str(locator))
            return False
        else:
            return result

    def is_selected(self,locator,timeout=10):
        """判断是否被选中,返回布尔值"""
        result = WebDriverWait(self.driver,timeout).until(EC.element_located_to_be_selected(locator))
        return result

    def select_by_index(self,locator,index):
        """通过索引选择下拉框内容"""
        element = self.findElement(locator)
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        """通过属性值选择下拉框内容"""
        element = self.findElement(locator)
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        """通过文本选择下拉框内容"""
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)

    def click_radio(self,locator):
        """点击单选框或只选择一个复选框"""
        if self.is_selected(locator)== False:
            self.click(locator)

    def click_checkbox(self,locator):
        """点击复选框(全选)"""
        box_element = self.findElement(locator)
        for box in box_element:
            if box.is_selected() == False:
                box.click()

    def scroll_to_end(self):
        """滚动到底部"""
        js = "window.scrollTo(0,100)"
        self.driver.execute_script(js)
    def scroll_to_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def sleepTime(self):
        # self.driver.implicitly_wait(30)
        sleep(5)

    def back(self):
        """返回"""
        self.driver.back()

    def close(self):
        """关闭浏览器"""
        self.driver.quit()
    def refresh(self):
        """刷新页面"""
        self.driver.refresh()

    def is_alert_present(self,timeout=10):
        '''
        判断页面是否有alert，
       有返回alert(注意这里是返回alert,不是True)
       没有返回False
        '''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
        #print(result)
        return result
    def operation_alter(self):
        """操作alter"""
        alter = self.driver.switch_to_alert()
        alter.accept()

if __name__ == '__main__':
    # 实例化Base
    base = Base()
    url = "http://ecshop.itsoso.cn"
    login_loc = ("link text","请登录")
    search_loc = ("name","imageField")
    username_loc = ("name","username")
    # 打开被测地址
    base.openUrl(url)
    #利用文本判断元素是否存在
    print(base.isTextInElement(login_loc,"请登录"))
    #利用元素属性值判断元素是否存在
    print(base.isTextInValue(search_loc,"搜索"))
    # 点击请登录连接
    base.click(login_loc)
    # 输入用户名
    base.sendKeys(username_loc,"诸葛亮")
    # 关闭浏览器
    base.close()


