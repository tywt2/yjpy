from sys import argv

import requests

from distance import getDistance

url_guotu = "http://localhost:8080/GuoTu"
params_guotu = {
    'departmentcode': 'Guott002'
}
guotu_data = requests.request("post", url_guotu, params=params_guotu)
guotu_json = guotu_data.json()

#####
DLBStatus_URL = "http://localhost:8080/statusInfo"
DLBStatus_params = {
    'fileName': 'Status_001814080001_20190521120000384.xml'
}
DLBStatus_Data = requests.request("post", DLBStatus_URL, params=DLBStatus_params)
DLBStatus_JSON = DLBStatus_Data.json()


#
def GuoTuAreaPoint(LatObject, LonObject, distance):
    person = 0
    monney = 0
    result = 0
    idStr = ''
    for guotu in guotu_json:
        LatOther = guotu['t11']
        LonOther = guotu['t10']
        LatOther = float(LatOther)
        LonOther = float(LonOther)
        dis = getDistance(LatObject, LonObject, LatOther, LonOther)
        if (dis < distance):
            person += float(guotu['t13'])
            monney += float(guotu['t14'])
            idStr += str(guotu['id']) + ','
    idStr = idStr.rstrip(',')
    if (not person.__eq__(0) and not monney.__eq__(0)):
        result = '"Guott002_id":"{0}","person":{1},"monney":{2}'.format(idStr, person, monney)
    return result


def StatusDLBGuoTuPoint(distance):
    out_json = "["
    for dlb in DLBStatus_JSON:
        Lat0 = dlb['Lat']
        Lon0 = dlb['Lon']
        Lat0 = float(Lat0)
        Lon0 = float(Lon0)
        GuotuStr = GuoTuAreaPoint(Lat0, Lon0, distance)
        if (not GuotuStr.__eq__('0')):
            out_json += '{"dlb_id":"' + dlb['ClientID'] + '",' + GuotuStr + '},'
    out_json = out_json.rstrip(',') + "]"
    print(out_json)


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
        if (not GuotuStr.__eq__('0')):
            out_json += '{"dlb_id":"' + report['ClientID'] + '",' + GuotuStr + '},'
    out_json = out_json.rstrip(',') + "]"
    print(out_json)


if __name__ == '__main__':
    distance = argv[1]
    distance = int(distance)
    StatusDLBGuoTuPoint()
