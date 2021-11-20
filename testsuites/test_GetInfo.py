#encoding:utf-8
import unittest
import requests
from configparser import ConfigParser
from common.logger import Logger

config=ConfigParser()
#绝对路径，config.ini包含汉字
# config.read("D:/pythonProject/testApi/config/config.ini",encoding='utf-8')
#绝对路径，config.ini不包含汉字
# config.read("D:/pythonProject/testApi/config/config.ini")
#相对路径，config.ini不包含汉字
# config.read("../config/config.ini")
#相对路径，config.ini包含汉字
config.read('../config/config.ini',encoding='utf-8')
logger=Logger('GetInfo').getlog()


class GetInfo(unittest.TestCase):
    def test_GetInfo(self):
        host=config.get('url','host')
        a={
            "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImRmNDNiYzk5LWYxNDQtNDllZC05YjZiLWI2MjA1OTgzZDM3OCJ9.YnFCpg-tEXlSXKi0XK5ml7DWhrqSulWyqCcRhxLM9EsquFa8Q7KTRtFT47oXb4Ke2278AD1Vo7o-n8aVv7n64Q"
        }
        params={'pageNum':1,
               'pageSize':10}
        r=requests.get(host+"/bsentry/op-course/course/searchCourse",params=params,headers=a)
        logger.info('调用成功')
        print(r.text)



if __name__ == '__main__':
    unittest.main()
