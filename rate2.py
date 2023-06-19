import requests
import json
import csv
import datetime

today = datetime.datetime.today().strftime('%Y%m%d')

# today = '20230616'

url = 'https://bank.shinhan.com/serviceEndpoint/httpDigital'

headers = {
           "dataBody": {
               "ricInptRootInfo": {
                   "serviceType": "GU",
                   "serviceCode": "F3730",
                   "nextServiceCode": "",
                   "pkcs7Data": "",
                   "signCode": "",
                   "signData": "",
                   "useSign": "",
                   "useCert": "",
                   "permitMultiTransaction": "",
                   "keepTransactionSession": "",
                   "skipErrorMsg": "",
                   "mode": "",
                   "language": "ko",
                   "exe2e": "",
                   "hideProcess": "",
                   "clearTarget": "",
                   "callBack": "shbObj.fncF3730Callback",
                   "exceptionCallback": "",
                   "requestMessage": "",
                   "responseMessage": "",
                   "serviceOption": "",
                   "pcLog": "",
                   "preInqForMulti": "",
                   "makesum": "",
                   "removeIndex": "",
                   "redirectUrl": "",
                   "preInqKey": "",
                   "_multi_transfer_": "",
                   "_multi_transfer_count_": "",
                   "_multi_transfer_amt_": "",
                   "userCallback": "",
                   "menuCode": "",
                   "certtype": "",
                   "fromMulti": "",
                   "fromMultiIdx": "",
                   "isRule": "N",
                   "webUri": "/index.jsp",
                   "gubun": "",
                   "tmpField2": ""
               },
               "조회구분": "",
               "조회일자": str(today),
               "고시회차": 1,
               "조회일자_display": "",
               "startPoint": "",
               "endPoint": ""
           },
           "dataHeader": {
               # "day": str(today),
               "trxCd": "RSHRC0213A01",
               "language": "ko",
               "subChannel": "49",
               "channelGbn": "D0"
           }
       }

res = requests.post(url, json=headers)

if res.status_code == 200:
    res = json.loads(res.text)
    today_us = res['dataBody']['R_RIBF3730_1'][0]
    curcode = today_us['통화CODE'] 
    if curcode == 'USD':
        exrate = today_us['전신환매도환율']
    else:
        print('통화 코드 에러')
else: 
    print('something worng!')
