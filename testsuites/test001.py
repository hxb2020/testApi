import pymysql
import unittest
import requests





class test001(unittest.TestCase):

    def test_GetInfo(self):
        a={
            "cookie": "adminer_permanent=; adminer_key=139eecc155714ad755d0b4fd626d50b3; adminer_sid=o8u6ib2rdad4i76ifvh34r74v4; adminer_version=4.8.1; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImRmNDNiYzk5LWYxNDQtNDllZC05YjZiLWI2MjA1OTgzZDM3OCJ9.YnFCpg-tEXlSXKi0XK5ml7DWhrqSulWyqCcRhxLM9EsquFa8Q7KTRtFT47oXb4Ke2278AD1Vo7o-n8aVv7n64Q"
        }
        params= {'username':'writeqa','db':'aienglish','script':'db'}
        r=requests.get("http://47.94.218.252/adminer/?username=writeqa&db=aienglish&script=db",params=params,headers=a)
        print(r.text)


