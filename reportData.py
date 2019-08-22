# from sys import argv
from sys import argv

import requests

from distance import getDistance

GuoTu_URL = "http://localhost:8080/GuoTu"
GuoTu_params = {
    'departmentcode': 'Guott002'
}
GuoTu_data = requests.request("post", GuoTu_URL, params=GuoTu_params)
GuoTu_json = GuoTu_data.json()

idList = []


def GuoTuAreaPoint(LatObject, LonObject, distance):
    personNum = 0
    monneyNum = 0
    result = 0
    multidStr = '['
    for guotu in GuoTu_json:
        LatOther = guotu['t11']
        LonOther = guotu['t10']
        LatOther = float(LatOther)
        LonOther = float(LonOther)
        dis = getDistance(LatObject, LonObject, LatOther, LonOther)
        if (dis < distance):
            tempid = str(guotu['id'])
            if (idList.count(tempid) == 0):
                idList.append(tempid)
                personNum += float(guotu['t13'])
                monneyNum += float(guotu['t14'])
                multidStr += '{"id":"' + str(guotu['id']) \
                             + '","name":"' + str(guotu['t1']) \
                             + '","t2":"' + str(guotu['t2']) \
                             + '","type":"' + str(guotu['t3']) \
                             + '","type2":"' + str(guotu['t4']) \
                             + '","t5":"' + str(guotu['t5']) \
                             + '","t6":"' + str(guotu['t6']) \
                             + '","address":"' + str(guotu['t7']) \
                             + '","person":"' + str(guotu['t8']) \
                             + '","tel":"' + str(guotu['t9']) \
                             + '","Lon":"' + str(guotu['t10']) \
                             + '","Lat":"' + str(guotu['t11']) \
                             + '","pNum":"' + str(guotu['t13']) \
                             + '","mNum":"' + str(guotu['t14']) \
                             + '"},'
    multidStr = multidStr.rstrip(',') + ']'
    result = '"Guott002_id":{0},"personNum":{1},"monneyNum":{2}'.format(multidStr, personNum, monneyNum)
    return result


def ReportDLBGuoTuPoint(distance, Identifier):
    DLBReport_URL = "http://localhost:8080/report"
    DLBReport_params = {
        'Identifier': Identifier
    }
    DLBReport_Data = requests.request("post", DLBReport_URL, params=DLBReport_params)
    DLBReport_JSON = DLBReport_Data.json()
    out_json = "["
    for report in DLBReport_JSON:
        Lat = report['Lat']
        Lon = report['Lon']
        Lat = float(Lat)
        Lon = float(Lon)
        GuotuStr = GuoTuAreaPoint(Lat, Lon, distance)
        out_json += '{"ClientID":"' + report['ClientID'] \
                        + '","Lon":"' + report['Lon'] \
                        + '","Lat":"' + report['Lat'] \
                        + '","Clienttype":"' + report['Clienttype'] \
                        + '","ClientStatus":"' + report['ClientStatus'] \
                        + '","ClientAddress":"' + report['ClientAddress'] \
                        + '","ClientPerson":"' + report['ClientPerson'] \
                        + '","ClientTel":"' + report['ClientTel'] \
                        + '",' + GuotuStr + '},'
    out_json = out_json.rstrip(',') + "]"
    print(out_json)


def Result():
    distance = argv[1]
    Identifier = argv[2]
    distance = int(distance)
    ReportDLBGuoTuPoint(distance, Identifier)


if __name__ == '__main__':
    # Result()
    ReportDLBGuoTuPoint(1, '14080041600000_20190814094524')
