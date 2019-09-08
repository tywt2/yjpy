# from sys import argv
from sys import argv

import requests

from distance import getDistance

distance = 1
idList = []


def GuoTuAreaPoint(LatObject, LonObject, GuoTu_JSON):
    personNum = 0
    monneyNum = 0
    multidStr = '['
    for guotu in GuoTu_JSON:
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
    result = '"Guott_id":{0},"personNum":{1},"monneyNum":{2}'.format(multidStr, personNum, monneyNum)
    return result


def ReportDLBGuoTuPoint(identifier, departmentcode):
    DLBReport_params = {
        'identifier': identifier
    }
    DLBReport_Data = requests.request("post", "http://localhost:8080/report", params=DLBReport_params)
    DLBReport_JSON = DLBReport_Data.json()
    # GuoTu_params = {
    #     'departmentcode': departmentcode
    # }
    # GuoTu_data = requests.request("post", "http://localhost:8080/GuoTu", params=GuoTu_params)
    GuoTu_params = {
        'identifier': identifier,
        'departmentcode': departmentcode
    }
    GuoTu_data = requests.request("post", "http://localhost:8080/GuoTuArea", params=GuoTu_params)
    GuoTu_JSON = GuoTu_data.json()
    out_json = "["
    for report in DLBReport_JSON:
        Lat = report['Lat']
        Lon = report['Lon']
        Lat = float(Lat)
        Lon = float(Lon)
        GuotuStr = GuoTuAreaPoint(Lat, Lon, GuoTu_JSON)
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
    identifier = argv[1]
    departmentcode = argv[2]
    ReportDLBGuoTuPoint(identifier, departmentcode)


if __name__ == '__main__':
    Result()
    #ReportDLBGuoTuPoint('14080041600000_20190814094524', 'Guott001')
