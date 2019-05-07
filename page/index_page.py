from base.base_handle import Base

class IndexPage(Base):
    """制作定位器,定位所有元素"""
    mobile_loc = ("link text","手机")

    """元素操作"""
    def click_mobile(self):
        self.click(self.mobile_loc)

