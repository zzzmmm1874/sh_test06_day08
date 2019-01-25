#import  allure
class Test_001:
    #@allure.step(title="我是test_001测试步骤名称")
    def test_001(self):
        print("---->test_001")
        assert  True
    #@allure.step(title="我是test_002测试步骤名称")
    def test_002(self):
        print("---->test_002")
        assert  False