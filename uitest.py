from ptest.decorator import TestClass, Test, BeforeClass, AfterClass
from ptest.assertion import assert_true
from ptest.plogger import preporter
from violent_webdriver import Chrome

# chrome 驱动地址，自行修改
CHROMEDRIVER_PATH = 'C:\\Users\\Administrator\\node_modules\\chromedriver\\lib\\chromedriver\\chromedriver.exe'

Test_Url = 'https://www.baidu.com'


@TestClass()
class BaiduTest:
    @BeforeClass(description='启动浏览器')
    def before(self):
        self.driver = Chrome.violent_chromedriver(CHROMEDRIVER_PATH)
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(10)

    @Test(tags=["regression", "smoke"], timeout=60, description="验证百度首页的title中是否包含「百度一下」字符串")
    def BaiduTest_001(self):
        self.driver.get(Test_Url)
        title_text = self.driver.title
        preporter.info('已进入百度首页并获取页面title，title值为: 「%s」' % title_text, screenshot=True)
        assert_true('百度一下' in title_text)

    @AfterClass(timeout=10, description='关闭浏览器')
    def after(self):
        self.driver.quit()
