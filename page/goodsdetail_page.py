from base.base_handle import Base
"""商品详情页"""
class GoodsDetail(Base):
    """制作定位器,定位所有元素"""
    current_location_loc = ("xpath","//*[@id='ur_here']/div/div")#当前位置
    goods_name_loc = ("class name","goods_style_name")# 商品名称
    buy_count_loc = ("id","number")# 购买数量
    bonus_points_loc = ("class name","f4")#用户积分余额
    buy_now_loc = ("xpath","//*[@class='td1']/a/img")

    """元素操作"""
    def check_goods_name(self,goods_name):
        """通过当前位置显示的商品名称和详情中的商品名称判断是否是想要购买的商品"""
        current_location = self.findElement(self.current_location_loc).text
        if goods_name in current_location:
            result1 = True
        else:
            result1 = False
        result2 = self.isTextInElement(self.goods_name_loc,goods_name)
        if result1==True and result2==True:
            result = True
        else:
            result = False
            print("购买买的商品信息不正确")
        return result
    def update_goods_count(self,number):
        """修改购买数量"""
        self.sendKeys(self.buy_count_loc,number)
    def click_buy_now(self):
        """点击立即购买"""
        self.click(self.buy_now_loc)
        




