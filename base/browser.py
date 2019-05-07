from selenium import webdriver



def open_browser(browser='firefox'):
    """根据不同的浏览器名称打开对应的浏览器"""
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "ie":
        driver = webdriver.Ie()
    else:
        print("请选择正确的浏览器,例如:'firefox','chrome','ie'")

    return driver
