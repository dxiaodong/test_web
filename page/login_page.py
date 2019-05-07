from base.base_handle import Base
"""登录页面"""
login_url = "http://ecshop.itsoso.cn/user.php"
class LoginPage(Base):
    """制作定位器,定位所有元素"""
    username_loc = ("name","username")# 用户名输入框
    password_loc = ("name","password")# 密码输入框
    remember_loc = ("name","remember")# 记住登录
    submit_loc = ("name","submit")# 登录按钮
    retrieve_question_loc = ("link text","密码问题")#找回密码通过密码问题
    retrieve_email_loc = ("link text","邮件")#找回密码通过邮件
    retrieve_massage_loc = ("link text", "短信验证")  # 找回密码通过短信验证
    register_img_loc = ("xpath","/html/body/div[6]/div[2]/a/img")# 立即注册图片
    homepage_loc = ("link text","首页")# 返回首页连接
    """元素操作"""
    def inputUsername(self,username):
        """输入用户名"""
        self.sendKeys(self.username_loc,username)
    def inputPassword(self,password):
        """输入密码"""
        self.sendKeys(self.password_loc,password)
    def clickRemember(self):
        """点击记住登录"""
        self.click(self.remember_loc)
    def clickSubmit(self):
        """点击登录按钮"""
        self.click(self.submit_loc)


if __name__ == '__main__':
    loginpage = LoginPage()
    url = "http://ecshop.itsoso.cn/user.php"
    loginpage.openUrl(url)
    loginpage.inputUsername("zhugelian")
    loginpage.close()