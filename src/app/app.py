# This is a sample Python script.
import os
import requests
from bs4 import BeautifulSoup
import requests
from src.language.en_gb.pack import Language as EN
from src.language.ro_ro.pack import Language as RO
from src.functionality.clear import Clear
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class APP:

    def __init__(self):
        #-----------------------primary var
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.url = 'http://192.168.0.181:8080/api/production'

        # end primary var


        #-----------------------data from api
        self.id = None
        self.resp = None

        #end data from api


        #-----------------------data to insert

        #end data to insert


    def deleteProductionID(self):

        self.payload = '{}'
        X= self.headers
        self.headers = {}
        requests.request('DELETE', url= self.url+'/'+str(self.id),headers = self.headers, data = self.payload)
        self.headers = X
        del X

    def postProduction(self):
        self.payload='{}'

        self.resp = requests.request(
                'POST',
                url=self.url,
                headers=self.headers,
                data=self.payload
            )
        if self.resp.status_code == 201:
            self.id = self.resp.json()['id']


    def putProduction(self,LQA=None,x=None,complete=None,screenout=None):
        if LQA != None:
            self.payload = "{\r\n   \"LQA\":\""+self.LQA+"\"\r\n}"


        elif x != None:
            self.payload = "{\r\n   \""+self.LQA+"\":\""+x+"\"\r\n}"


        elif complete != None:
            self.payload = "{\r\n   \"Status\":\"c\"\r\n}"

        elif screenout !=None:
            self.payload = "{\r\n   \"Status\":\"s\"\r\n}"

        requests.request("PUT", url=self.urlid, headers=self.headers, data=self.payload)

    def selectLanguage(self):
        self.lang = self.dashboardSelection()
        while(self.lang!='ro' and self.lang!='en'): self.lang=self.dashboardSelection()


    def dashboardSelection(self):
        return input(EN().Lch+'|'+RO().Lch+'\n')

    # def __iter__(self):
    #     self.i = 0
    #
    # def __next__(self):
    #     self.i+=1
    #     return self.i

    def execute_QNR(self):
        self.urlid = self.url+'/'+str(self.id)
        input(self.LangClass.intro)
        for i in range(1,5):

            self.LQA = 'Q'+str(i)
            self.putProduction(LQA=True)
            exec('print(self.LangClass.q'+str(i)+')')
            x = input()
            self.putProduction(x=x)
            if self.LQA == 'Q2':
                try:
                    x = int(x)
                except:
                    self.putProduction(screenout=True)
                    return None

                if 18>x:
                    self.putProduction(screenout=True)
                    return None


        self.putProduction(complete=True)


    def runApp(self):
        self.selectLanguage()
        self.LangClass=EN()
        if self.lang == 'ro':
            self.LangClass=RO()
        # self.LangClass=exec(self.lang.upper()+'()')
        self.postProduction()
        self.execute_QNR()
        input(self.LangClass.end)
        #self.deleteProductionID()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
APP().runApp()