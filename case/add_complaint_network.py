import requests
import unittest
import time
import base64
import hashlib
import common.dbHelper


class AddComplaintNetwork(unittest.TestCase):
    '''网页端——添加网络投诉'''

    def __init__(self):
        self.proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
        self.s = requests.session()
        self.url = "http://192.168.0.142:8090/server/api/saveorupdate"

    def setUp(self):
        self.proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
        self.s = requests.session()
        self.url = "http://192.168.0.142:8090/server/api/saveorupdate"

    def tearDown(self):
        self.s.close()

    # 新增网络投诉 返回查询码
    def test_add_complaint_network(self):
        '''
        新增网络投诉
        :return: 查询码
        '''
        # 第1步：URL中添加client(公钥)及时间戳
        sjc = int(time.time())
        param = {
            "clientId": "2cbe74dc3d",  # 公钥
            "timestamp": sjc  # 时间戳，取整数部分
        }
        # 第2步：获取URL所有参数（包括body参数）
        allParam ={
            "clientId": "2cbe74dc3d",  # 公钥
            "timestamp": sjc,  # 时间戳，取整数部分
            "visitorVoucher": "",
            "reasonDetail": "JK投诉事由",
            "serviceRegion": 540100,
            "companyName": "JK被投诉单位名称",
            "phone": "15100000001",
            "sex": "男性",
            "name": "JK上报人名称",
            "type": 0
        }
        # 第3步：对参数中的key进行字典排序
        params = sorted(allParam.items(), key=lambda item: item[0])
        # 第4步：将参数以KEY VALUE的形式拼接成一条字符串
        arr = []
        for i in params:
            # arr.append("".join(list(i)))  # 有数字报错，不能用"".join 报错：TypeError: sequence item 1: expected str instance, int found
            arr.append("".join('%s' %id for id in list(i)))
        dataStr = "".join(arr)
        # 第5步：将密钥再拼接到字符串尾部
        dataStr = dataStr + "47f1df0e5a3e2592b81cdc719b"
        # 第6步：使用Base64将字符转码
        tempSign = base64.b64encode(dataStr.encode('utf8'))  # python3不太一样：因为3.x中字符都为unicode编码，而b64encode函数的参数为byte类型，所以必须先转码
        # 第7.8步：使用sha1对转码后的字符进行摘要计算,,计算结果转换成16进制并大写
        signature = hashlib.sha1(tempSign).hexdigest().upper()
        # 第9步：最后将所得结果作为参数sign的值添加到URL中
        param["sign"] = signature
        # 发送请求
        data = {
            "visitorVoucher": "",
            "reasonDetail": "JK投诉事由",
            "serviceRegion": 540100,
            "companyName": "JK被投诉单位名称",
            "phone": "15100000001",
            "sex": "男性",
            "name": "JK上报人名称",
            "type": 0
        }
        r = self.s.post(self.url, params=param, data=data, proxies=self.proxies)
        # self.assertEqual(200, r.status_code)
        try:
            if r.status_code == 200:
                self.assertEqual(0, r.json()["code"])
                if (r.json()["message"]):
                    self.assertEqual("success", r.json()["message"])
                    return r.json()["data"]["querycode"]
        except:
            pass

    # 新增网络投诉 返回投诉id
    def test_add_complaint_network_reid(self):
        '''
        新增网络投诉
        :return: 投诉id
        '''
        sql = "select * from COMPLAINT_NETWORK where name like '%JK上报人名称%' ORDER BY COMPLAINT_DATE DESC"
        datas = common.dbHelper.selectMethod(sql, type='ywDB')
        id =datas[0][1]
        return id


if __name__ == '__main__':
    # unittest.main()
    AddComplaintNetwork.test_add_complaint_network_reid()

