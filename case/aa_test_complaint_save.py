import requests
import unittest
from common.login import Login
import common.dbHelper
import ddt
import json
from case import add_complaint_network

sql = "select * from test_datas where menuName='投诉管理' and caseName='保存'"
datas = common.dbHelper.selectMethod(sql)

@ddt.ddt
class AATestComplaintSave(unittest.TestCase):
    '''投诉保存'''

    def setUp(self):
        self.proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
        self.s = requests.session()
        self.url = "http://192.168.0.142:9099/rest/saveComplaint"
        self.token = Login().loginMethod(url="http://192.168.0.142:9099/rest/authenticate", username="cslasa", pwd="123456")
        self.h = {
            "Authorization": "Bearea " + self.token
        }

    def tearDown(self):
        self.s.close()

    @ddt.data(*datas)
    def test_complaint_save(self, data):
        '''投诉保存用例'''
        # 新增网络投诉
        code = add_complaint_network.AddComplaintNetwork().test_add_complaint_network()
        # 返回网络投诉id
        id = add_complaint_network.AddComplaintNetwork().test_add_complaint_network_reid()
        # 替换数据库中用例数据网络id
        datas = json.loads(data[6])
        datas["networkId"] = id
        # 执行保存操作
        r = self.s.post(self.url, params=json.loads(data[6]), headers=self.h,  proxies=self.proxies)
        self.assertEqual(200, r.status_code)
        try:
            if r.status_code == 200:
                self.assertEqual(data[7], r.json()["code"])
                if (r.json()["message"]):
                    self.assertEqual(data[8], r.json()["message"])
        except:
            pass


if __name__ == '__main__':
    unittest.main()


