from base.browser import open_browser
from page.register_page import RegisterPage,register_url

class RegisterFlow:
    def __init__(self,browser='firefox'):
        self.driver = open_browser(browser)
        self.register = RegisterPage(self.driver)
        self.register.openUrl(register_url)
    def full_register(self,data):
        """
        全信息注册
        :param data: 注册数据
        :return:
        """
        self.register.input_register_username(data["username"])
        self.register.input_register_email(data["email"])
        self.register.input_register_password(data["password"])
        self.register.input_register_cfpassword(data["cf_password"])
        self.register.input_register_qq(data["qq"])
        self.register.input_register_mobile(data["mobile"])
        self.register.select_register_question(data["question"])
        self.register.input_question_answer(data["answer"])
        self.register.click_agreement()
        self.register.scroll_to_end()
        self.register.click_register_btn()
    def is_register_success(self, username):
        """验证是否 注册成功"""
        result = self.register.isTextInElement(("class name", "f4_b"), username)
        if result:
            print("登录成功")
        else:
            print("登录失败")
        return result


