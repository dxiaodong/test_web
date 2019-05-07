from base.base_handle import Base
"""注册页面"""
register_url = "http://ecshop.itsoso.cn/user.php?act=register"
class RegisterPage(Base):
    """制作定位器,定位所有元素"""
    username_loc = ("id","username")# 注册页面用户名输入框
    email_loc = ("id","email")# 注册页面邮箱输入框
    password_loc = ("id","password1")# 注册页面密码输入框
    conform_password_loc = ("id","conform_password")
    qq_loc = ("name","extend_field2")# 注册qq(非必填)
    mobile_loc = ("name","extend_field5")# 注册手机号
    sel_question_loc = ("name","sel_question")# 找回密码提示问题(非必填)
    passwd_answer_loc = ("name","passwd_answer") # 找回密码问题答案(非必填)
    agreement_loc = ("name","agreement")# 同意协议复选框
    register_btn_loc = ("name","Submit")# 立即注册按钮
    login_link_loc = ("partial link text","我要登录")# 登录连接
    forget_loc = ("partial link text","忘记密码")# 忘记密码连接

    username_notice_loc = ("id","username_notice")# 用户名输入框提示
    email_notice_loc = ("id","email_notice")# 邮箱输入框提示
    password_notice_loc = ("id","password_notice")# 密码输入框提示
    conform_password_notice_loc = ("id","conform_password_notice")# 确认密码输入框提示
    """元素操作"""
    def input_register_username(self,username):
        """输入注册用户名"""
        self.sendKeys(self.username_loc,username)
    def input_register_email(self,email):
        """输入注册邮箱"""
        self.sendKeys(self.email_loc, email)
    def input_register_password(self,password):
        """输入注册密码"""
        self.sendKeys(self.password_loc,password)
    def input_register_cfpassword(self,password):
        """输入确认密码"""
        self.sendKeys(self.conform_password_loc,password)
    def input_register_qq(self,qq):
        """输入注册qq号(选填)"""
        self.sendKeys(self.qq_loc,qq)
    def input_register_mobile(self,mobile):
        """输入注册手机号"""
        self.sendKeys(self.mobile_loc,mobile)
    def select_register_question(self,index):
        """选择找回密码问题"""
        self.select_by_index(self.sel_question_loc,index)
    def input_question_answer(self,answer):
        """输入找回密码问题答案"""
        self.sendKeys(self.passwd_answer_loc,answer)
    def click_agreement(self):
        """点击同意协议"""
        self.click_radio(self.agreement_loc)
    def click_register_btn(self):
        """点击立即注册"""
        self.click(self.register_btn_loc)
    def click_login_link(self):
        """点击登录连接"""
        self.click(self.login_link_loc)
    def click_forget_link(self):
        """点击忘记密码连接"""
        self.click(self.forget_loc)


    