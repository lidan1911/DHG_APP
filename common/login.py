
import requests
import base64


class Login:

    proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}

    # 登陆
    def loginMethod(self, url="http://192.168.0.142:90999", username="cslasa", pwd="123456"):
        s = requests.session()
        str = username+':'+pwd
        bstr = base64.b64encode(str.encode())
        loginToken = "Basic "+bytes.decode(bstr)
        h = {
            "Authorization": loginToken
        }
        r = s.post(url, headers=h, proxies=self.proxies)
        token = r.json()['data']['accessToken']['token']
        return token
        s.close()

if __name__ == '__main__':
    Login().loginMethod(url="http://192.168.0.142:9099/rest/authenticate", username="cslasa", pwd="123456")






