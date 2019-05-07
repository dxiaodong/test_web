from base.base_handle import Base

"""支付页面"""
class Pay(Base):
    """制作元素定位器"""
    pay_order_loc = ("xpath","//input[@type = 'image']")

    """元素操作"""
    def pay_order(self):
        """点击提交订单"""
        self.click(self.pay_order_loc)

class PaySuccess(Base):
    """制作元素定位器"""
    order_num_loc = ("xpath", "//font[@style = 'color:red']")

    """元素操作"""
    def get_order_num(self):
        """获取订单号"""
        order_num = self.findElement(self.order_num_loc).text
        return order_num