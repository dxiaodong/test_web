from base.browser import open_browser
from page.login_page import LoginPage,login_url

class LoginFlow:
    def __init__(self,browser='firefox'):
        self.driver = open_browser(browser)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.openUrl(login_url)
    def login(self,username,password):
        """用户登录"""
        self.loginpage.inputUsername(username)
        self.loginpage.inputPassword(password)
        self.loginpage.clickRemember()
        self.loginpage.clickSubmit()
    def is_login_success(self,username):
        """验证是否 登录成功"""
        result = self.loginpage.isTextInElement(("class name","f4_b"),username)
        if result:
            print("登录成功")
        else:
            print("登录失败")
        return result
    def back_index(self):
        """返回首页"""
        self.loginpage.click(("link text","首页"))
    def close_browser(self):
        self.loginpage.close()
    def logout(self):
        """退出登录"""
        self.loginpage.click(("link text","退出"))
    def re_login(self):
        """点击请登录"""
        self.loginpage.click(("link text","请登录"))

    def refresh(self):
        self.loginpage.refresh()

if __name__ == '__main__':
    username = "诸葛亮"
    password = "Test123456"
    login = LoginFlow()
    login.login(username,password)
    login.is_login_success(username)




