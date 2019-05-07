import random
from base.exceluntil import ExcelUntil

class RegisterData:
    def __init__(self):
        self.excel = ExcelUntil("../data/registerdata.xls")
    def random_uername(self):
        """
        随机生成用户名:
        """
        frist_name = ["赵","钱","孙","李","周","吴","郑","王","Tom","Jerry","Kitty","冯","陈","楚","卫"]
        last_name = ["芷荷","怀瑶","慕易","若芹","紫安","曼冬","寻巧","寄波","尔槐",
                     "以旋","初夏","依丝","怜南","傲菡","谷蕊","笑槐","飞兰","笑卉",
                     "迎荷","元冬","痴安","妙绿","觅雪","寒安","沛凝","白容","乐蓉",
                     "映安","依云","映冬","凡雁","梦秋","梦凡","秋巧","若云","元容",
                     "怀蕾","灵寒","天薇","翠安","乐琴","宛南","怀蕊","白风","访波",
                     "亦凝","易绿","夜南","曼凡","亦巧","青易。冰真","白萱","友安",
                     "海之","小蕊","又琴","天风","若松","盼菡","秋荷","香彤","语梦",
                     "惜蕊","迎彤","沛白","雁山","易蓉","雪晴","诗珊","春冬","又绿",
                     "冰绿","半梅","笑容","沛凝","映秋","盼烟","晓凡","涵雁","问凝",
                     "冬萱","晓山","雁蓉","梦蕊","山菡","南莲","飞双","凝丝","思萱",
                     "怀梦","雨梅","冷霜","向松","迎丝","迎梅","雅彤","香薇","以山",
                     "碧萱","寒云","向南","书雁","怀薇","思菱","忆文","翠巧","怀山",
                     "若山","向秋","凡白","绮烟","从蕾","天曼","又亦","从安","绮彤",
                     "之玉","凡梅","依琴","沛槐","又槐","元绿","安珊","夏之","易槐",
                     "宛亦","白翠","丹云","问寒","易文","傲易","青旋","思真","雨珍",
                     "幻丝","代梅","盼曼","妙之","半双","若翠","初兰","惜萍","初之",
                     "宛丝","寄南","小萍","静珊","千风","天蓉","雅青","寄文","涵菱",
                     "香波","青亦","元菱","翠彤","春海","惜珊","向薇","冬灵","惜芹",
                     "凌青","谷芹","雁桃","映雁","书兰","盼香","向山","寄风","访烟",
                     "绮晴","映之","醉波","幻莲","谷冬","傲柔","寄容","以珊","紫雪",
                     "芷容","书琴","寻桃","涵阳","怀寒","易云","代秋","惜梦","尔烟",
                     "谷槐","怀莲","夜山","芷卉","向彤","新巧","语海","灵珊","凝丹",
                     "小蕾","迎夏"]
        return random.choice(frist_name)+ "".join(random.choice(last_name))
    def random_password(self):
        """随机生成密码6--18位"""
        number = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digit = random.randint(6,18)
        password = "".join(random.choice(number) for i in range(digit))
        return password
    def random_email(self,emailtype=None,rang=None):
        """随机生成邮箱"""
        __emailtype = ["@qq.com","@163.com","@126.com","@189.com"]
        # 如果没有指定邮箱类型,默认在__emailtype中随机选择一个
        if emailtype == None:
            __randomemail = random.choice(__emailtype)
        else:
            __randomemail = emailtype
        # 如果没有指定邮箱长度,默认在4-10之间随机
        if rang == None:
            __rang = random.randint(4,10)
        else:
            __rang = int(rang)
        __number = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        __randomnumber ="".join(random.choice(__number) for i in range(__rang))
        _email = __randomnumber + __randomemail
        return _email
    def random_qq(self):
        """随机生成5--10位qq号"""
        digit = random.randint(5,10)
        number = "1234567890"
        qq = "".join(random.choice(number)for i in range(digit))
        return qq
    def random_mobile(self):
        """随机生成11位手机号"""
        mobile_list = ["133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","180","186","187","188"]
        number = "0123456789"
        mobile = random.choice(mobile_list) + "".join(random.choice(number)for i in range(8))
        return mobile
    def random_index(self):
        """随机生成问题序列号"""
        num = random.randint(1,9)
        return num
    def random_answer(self):
        """随机生成答案"""
        answer_list = ["为人性僻耽佳句,语不惊人死不休.",
                       "白发三千丈,缘愁似个长.",
                       "座客三千人，于今知有谁.",
                       "出师未捷身先死，长使英雄泪满襟。",
                       "兰陵美酒郁金香，玉碗盛来琥珀光。",
                       "庄生晓梦迷蝴蝶，望帝春心托杜鹃。",
                       "靡不有初，鲜克有终。",
                       "一唱雄鸡天下白，万方乐奏有于阗",
                       "高山仰止，景行行止",
                       "一日不见，如三月兮",
                       "有匪君子，如切如磋，如琢如磨"
                       ]
        return random.choice(answer_list)
    def full_register(self):
        """填写全部注册内容"""
        data = {}
        data["username"] = self.random_uername()
        data["email"] = self.random_email()
        data["password"] = self.random_password()
        data["cf_password"] = data["password"]
        data["qq"] = self.random_qq()
        data["mobile"] = self.random_mobile()
        data["question"] = self.random_index()
        data["answer"] = self.random_answer()
        new_data = {}
        for i in range(0,len(data)):
            new_data[list(data.keys())[i]] = self.is_exist(list(data.keys())[i],data[list(data.keys())[i]])
        return new_data

    def not_qq(self):
        """不填写QQ注册"""
        data = {}
        data["username"] = self.random_uername()
        data["email"] = self.random_email()
        data["password"] = self.random_password()
        data["cf_password"] = data["password"]
        data["mobile"] = self.random_mobile()
        data["question"] = self.random_index()
        data["answer"] = self.random_answer()
        new_data = {}
        for i in range(0, len(data)):
            new_data[list(data.keys())[i]] = self.is_exist(list(data.keys())[i], data[list(data.keys())[i]])
        return new_data

    def not_question(self):
        """不填写问题注册"""
        data = {}
        data["username"] = self.random_uername()
        data["email"] = self.random_email()
        data["password"] = self.random_password()
        data["cf_password"] = data["password"]
        data["qq"] = self.random_qq()
        data["mobile"] = self.random_mobile()
        new_data = {}
        for i in range(0, len(data)):
            new_data[list(data.keys())[i]] = self.is_exist(list(data.keys())[i], data[list(data.keys())[i]])
        return new_data

    def all_not(self):
        """不填写QQ和问题注册"""
        data = {}
        data["username"] = self.random_uername()
        data["email"] = self.random_email()
        data["password"] = self.random_password()
        data["cf_password"] = data["password"]
        data["mobile"] = self.random_mobile()
        new_data = {}
        for i in range(0, len(data)):
            new_data[list(data.keys())[i]] = self.is_exist(list(data.keys())[i], data[list(data.keys())[i]])
        return new_data
    def get_data_list(self,data):
        value_list = []
        for key in data.keys():
            value_list.append(data[key])
        return value_list

    def run_main(self,data_name):
        """生成主方法"""
        test_data = None
        if data_name == "username":
            test_data = self.random_uername()
        elif data_name == "email":
            test_data = self.random_email()
        elif data_name == "password":
            test_data = self.random_password()
        elif data_name == "qq":
            test_data = self.random_qq()
        elif data_name == "mobile":
            test_data = self.random_mobile()
        elif data_name == "question":
            test_data = self.random_index()
        elif data_name == "answer":
            test_data = self.random_answer()
        else:
            print("请选择正确的数据")
        return test_data

    def is_exist(self,col_name,col_data):
        """判断新生成的数据是否存在于表格中"""
        col_name_data = self.excel.get_col_data(col_name)
        name_list = ["username","email","qq","mobile"]
        if col_name in name_list:
            if col_data in col_name_data:
                new_col_data = self.run_main(col_name)
            else:
                new_col_data = col_data
        else:
            new_col_data = col_data
        return new_col_data

if __name__ == '__main__':
    data = RegisterData()
    excel = ExcelUntil('../data/registerdata.xls')
    #print(data.random_uername())
    # print(data.random_password())
    # print(data.random_email(rang=11))
    # print(data.random_qq())
    # print(data.random_mobile())
    # print(data.random_index())
    # print(data.random_answer())
    data_all = data.all_not()
    print(data_all)
    value_list = data.get_data_list(data_all)
    print(value_list)
    excel.write_data(value_list)



