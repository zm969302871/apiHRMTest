import requests
import app


class EmpApi:
    def __init__(self):
        self.emp_url = app.HOST + '/api/sys/user'
        # 注意:如果我们调用员工管理模块的相关接口,先调用login.py接口
        # 获取到app.HEADERS 才会是{'Content-Type':'application','Authorization':'Bearer xxxx-xxx-xxxx'}
        self.headers = app.HEADERS

    def add_emp(self, username, mobile):
        data = {"username": username,
                "mobile": mobile,
                "timeOfEntry": "2019-12-02",
                "formOfEmployment": 1,
                "workNumber": "1234",
                "departmentName": "测试",
                "departmentId": "1210411411066695680",
                "correctionTime": "2019-12-15T16:00:00.000Z"
                }
        # 发送添加员工接口请求
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        # 返回添加员工接口的响应数据
        return response
        # 封装查询员工接口

    def query_emp(self):
        url = self.emp_url + '/' + app.EMP_ID
        return requests.get(url, headers=self.headers)

    # 封装修改员工接口
    def modify_emp(self, username):
        url = self.emp_url + '/' + app.EMP_ID
        data = {'username': username}
        # 返回的修改结果
        return requests.put(url, json=data, headers=self.headers)
    # 封装删除员工接口
    def delete_emp(self):
        url = self.emp_url + '/' + app.EMP_ID
        return requests.delete(url,headers = self.headers)
