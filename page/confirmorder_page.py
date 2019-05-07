from base.base_handle import Base
"""确认订单页"""
class ComfirmOrder(Base):
    """制作定位器,定位所有元素"""
    goods_name_loc = ("class name","f6")# 购买的商品名称
    goods_count_loc = ("class name","inputBg")# 购买的商品数量
    delete_goods_loc = ("link text","删除")# 删除购买的商品
    favorite_loc = ("link text","放入收藏夹")# 放入收藏夹
    clear_shopping_cart_loc = ("xpath","//*[@class='bnt_blue_1'and @type='button']")# 清空购物车
    update_shopping_cart_loc = ("name","submit")# 更新购物车
    continue_loc = ("xpath","//img[@alt='continue']")# 继续购物
    checkout_loc = ("xpath","//img[@alt='checkout']")# 去结算

    """元素操作"""
    def comfirm_goods(self,goods_name):
        """确认订单商品名称"""
        result = self.isTextInElement(self.goods_name_loc,goods_name)
        return result
    def comfirm_count(self,count):
        """确认商品数量"""
        result = self.isTextInValue(self.goods_count_loc,count)
        return result
    def checkout(self):
        """去结算"""
        self.click(self.checkout_loc)
        

