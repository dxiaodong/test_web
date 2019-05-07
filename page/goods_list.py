from base.base_handle import Base
"""商品列表页"""
class GoodsList(Base):
    #self.openUrl(url)
    def _get_goods_title(self,goods_list_loc,attribute=None):
        """遍历页面所有商品,获取商品title"""

        # 获取页面所有商品的元素
        elements = self.findElements(goods_list_loc)
        # 定义一个元素属性list
        goods_list = []
        if attribute == None:
            for i in range(len(elements)):
                text = elements[i].text
                print(text)
                goods_list.append(text)
        else:
            for i in range(len(elements)):
                attr = elements[i].get_attribute(attribute)
                goods_list.append(attr)
        return goods_list
    def _get_goods_loc(self,goods_list_loc,attribute=None):
        """根据页面所有商品的title获取每一个商品的locator"""
        goods_list = self._get_goods_title(goods_list_loc,attribute)
        # 定义商品locator
        goods_loc = []
        if attribute == None:
            for j in range(len(goods_list)):
                # 拼接xpath 定位属性
                a = ("xpath", "//*[contains(text(),'{}')]".format(goods_list[j]))

                goods_loc.append(a)
        else:
            for j in range(len(goods_list)):
                # 拼接xpath 定位属性
                a = ("xpath", "//*[@{} = '{}']".format(attribute, goods_list[j]))
                goods_loc.append(a)
        return goods_loc
    def click_goods_list(self,goods_list_loc,attribute=None):
        """点击页面所有商品"""
        goods_loc = self._get_goods_loc(goods_list_loc,attribute)
        for i in range(len(goods_loc)):
            if i in [4,8]:
                self.scroll_to_end()
            self.click(goods_loc[i])
            self.sleepTime()
            self.back()
            self.scroll_to_end()
    def choice_goods(self,goods_list_loc,goods_name,attribute=None):
        """选择某一个商品"""
        goods_list = self._get_goods_title(goods_list_loc=goods_list_loc,attribute=attribute)
        goods_loc = self._get_goods_loc(goods_list_loc=goods_list_loc,attribute=attribute)
        for i in range(len(goods_list)):
            if goods_name == goods_list[i]:
                self.click(goods_loc[i])

if __name__ == '__main__':
    gl = GoodsList()
    goods_list_loc = ("xpath", "//*[@class='goods-title']/a")
    url = "http://ecshop.itsoso.cn/category.php?id=25"
    attribute = "title"
    goods_name = "移动电源10000mAh"
    gl.choice_goods(url,goods_list_loc,goods_name,attribute)