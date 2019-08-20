import json

import requests

from distance import getDistance

url_guotu = "http://localhost:8080/GuoTu"
params_guotu = {
    'departmentcode': 'Guott002'
}
guotu_data = requests.request("post", url_guotu, params=params_guotu)
guotu_json = guotu_data.json()

url_jiaotong = "http://localhost:8080/JiaoTong"
params_jiaotong = {
    'departmentcode': 'Jiaott001'
}
jiaotong_data = requests.request("post", url_jiaotong, params=params_jiaotong)
jiaotong_json = jiaotong_data.json()

url_dlb = "http://localhost:8080/statusInfo"
params_dlb = {
    'fileName': 'Status_001814080001_20190521120000384.xml'
}
dlb_data = requests.request("post", url_dlb, params=params_dlb)
dlb_json = dlb_data.json()


#
def areaGuoTUPoint(LatObject, LonObject, distance):
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
            # print(str(guotu['id']) + ' ' + str(guotu['t13']) + ' ' + str(guotu['t14']))
    if (not person.__eq__(0) and not monney.__eq__(0)):
        result = '"Guott002_id":"' + idStr.rstrip(',') + '","person":"' + str(person) + '","monney":"' + str(monney)+'"'
    return result


def areaJTPoint(LatObject, LonObject, dis):
    for jiaotong in jiaotong_json:
        # 起始点经纬度
        Lat1 = jiaotong['t7']
        Lon1 = jiaotong['t6']
        Lat2 = jiaotong['t9']
        Lon2 = jiaotong['t8']
        Lat1 = float(Lat1)
        Lon1 = float(Lon1)
        Lat2 = float(Lat2)
        Lon2 = float(Lon2)
        distance = getDistance(LatObject, LonObject, Lat1, Lon1)
        distance2 = getDistance(LatObject, LonObject, Lat2, Lon2)
        if (distance < dis):
            print(jiaotong)
        if (distance2 < dis):
            print(jiaotong)
    return


def showDLB():
    out_json = "["
    for dlb in dlb_json:
        Lat0 = dlb['Lat']
        Lon0 = dlb['Lon']
        Lat0 = float(Lat0)
        Lon0 = float(Lon0)
        pAndMon = areaGuoTUPoint(Lat0, Lon0, 1)
        if (not pAndMon.__eq__('0')):
            out_json += '{"dlb_id":"' + str(dlb['ClientID']) + '",' + pAndMon + '},'
    out_json = out_json.rstrip(',') + "]"
    #print(json.dumps(out_json))
    #out_json='[{"dlb_id":"001814080001_E011181","Guott002_id":"40573","person":"5.0","monney":"12.5"},{"dlb_id":"001814080001_E011182","Guott002_id":"40573","person":"5.0","monney":"12.5"}]'
    print(out_json)
    # print(str(dlb['ClientID']) + ' ' + pAndMon)


showDLB()
