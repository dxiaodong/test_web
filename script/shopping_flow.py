from script.login_flow import LoginFlow
from page.goods_list import GoodsList
from page.goodsdetail_page import GoodsDetail
from page.confirmorder_page import ComfirmOrder
from page.pay_page import Pay,PaySuccess
from page.index_page import IndexPage

class ShoppingFlow:
    def __init__(self):
        self.login = LoginFlow()
        self.login.login("诸葛亮", "Test123456")
        self.login.back_index()
        self.driver = self.login.driver
        self.g_list = GoodsList(self.driver)
        self.g_detail = GoodsDetail(self.driver)
        self.cf_order = ComfirmOrder(self.driver)
        self.pay = Pay(self.driver)
        self.pay_s = PaySuccess(self.driver)
        self.index = IndexPage(self.driver)
    def choice_goods(self,goods_list_loc,goods_name,attribute):
        """选择商品"""
        self.index.sleepTime()
        self.index.click_mobile()
        self.g_list.choice_goods(goods_list_loc,goods_name,attribute)
    def check_goods_detail(self,goods_name):
        """检查商品详情并下单"""
        if self.g_detail.check_goods_name(goods_name):
            self.g_detail.click_buy_now()
        else:
            print("选择的商品与商品详情不符")
    def comfirm_goods_order(self,goods_name):
        """再次确认订单"""
        if self.cf_order.comfirm_goods(goods_name):
            self.cf_order.checkout()
        else:
            print("订单信息不正确")

    def pay_order(self):
        """支付订单"""
        self.pay.pay_order()


if __name__ == '__main__':
    shopping = ShoppingFlow()
    goods_list_loc = ("xpath", "//*[@class='goods-title']/a")
    #url = "http://ecshop.itsoso.cn/category.php?id=25"
    attribute = "title"
    goods_name = "移动电源10000mAh"
    shopping.choice_goods(goods_list_loc,goods_name,attribute)
    shopping.check_goods_detail(goods_name)
    shopping.comfirm_goods_order(goods_name)
    shopping.pay_order()


