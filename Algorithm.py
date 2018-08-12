import requests
import time
import redis
from DataManager import DataManager
import json

class Algorithm:

    postRequestUrl = 'http://localhost:5000/amazonAPI/register-request'
    getRequestRoot = 'http://localhost:5000/amazonAPI/request-data/'

    def __init__(self, dbm):
        self.dbm = dbm
        self.rCon = redis.Redis(host='localhost', port=6379, db=0)

    def execute(self, tickNo):
        last_5_prices = self.get_last_5_competitor_prices(tickNo)
        avg_comp_price = sum(last_5_prices) / len(last_5_prices)

        requestData = '''{ "avg_comp_price": ''' + str(avg_comp_price) + '''}'''

        postResponse = requests.post(Algorithm.postRequestUrl, data=requestData)

        if postResponse.ok:
            respData = json.loads(postResponse.content)
            reqId = respData['Id']

            time.sleep(1)

            getRequestUrl = Algorithm.getRequestRoot + str(reqId)
            getResponse = requests.get(getRequestUrl)

            if getResponse.ok:
                gRespData = json.loads(getResponse.content)
                isSold = bool(gRespData['sold'])

                if isSold is True:
                    print avg_comp_price*1.1
                else:
                    print avg_comp_price*0.9

    def get_last_5_competitor_prices(self, tickNo):
        self.dbm.triggerTick(tickNo)
        last_5_prices = self.rCon.lrange( "prices", 0, -1 )
        last_5_prices_float = map(float, last_5_prices)
        return last_5_prices_float
