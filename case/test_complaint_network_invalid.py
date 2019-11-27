import unittest
import requests
from common import login
import ddt
from common import dbHelper
from case import add_complaint_network
import json

sql = "select * from test_datas where menuName='投诉管理' and caseName='确认无效'"
datas = dbHelper.selectMethod(sql)

@ddt.ddt
class TestComplaintNetworkInvalid(unittest.TestCase):
    '''确认网络投诉为无效投诉'''

    def setUp(self):
        self.proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
        self.s = requests.session()
        self.url = "http://192.168.0.142:9099/rest/webComplaintDisable"
        self.token = login.Login().loginMethod(url="http://192.168.0.142:9099/rest/authenticate", username="cslasa", pwd="123456")
        self.h = {
            "Authorization": "Bearea " + self.token
        }

    def tearDown(self):
        self.s.close()

    @ddt.data(*datas)
    def test_complaint_net_invalid(self, data):
        '''确认网络投诉为无效投诉用例'''
        # 新增网络投诉
        add_complaint_network.AddComplaintNetwork().test_add_complaint_network()
        # 返回网络投诉id
        id = add_complaint_network.AddComplaintNetwork().test_add_complaint_network_reid()
        a = json.loads(data[6])
        a['id'] = id
        r = self.s.get(self.url, params=a, headers=self.h, proxies=self.proxies)
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


