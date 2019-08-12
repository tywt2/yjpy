
import requests

from distance import getDistance

url_guotu="http://localhost:8080/GuoTu"
params_guotu ={
    'departmentcode': 'Guott002'
}
guotu_data = requests.request("post", url_guotu, params=params_guotu)
guotu_json=guotu_data.json()

url_jiaotong="http://localhost:8080/JiaoTong"
params_jiaotong ={
    'departmentcode': 'Jiaott001'
}
jiaotong_data = requests.request("post", url_jiaotong, params=params_jiaotong)
jiaotong_json=jiaotong_data.json()

url_dlb="http://localhost:8080/statusInfo"
params_dlb ={
    'fileName': 'Status_001814080001_20190521120000384.xml'
}
dlb_data = requests.request("post", url_dlb, params=params_dlb)
dlb_json=dlb_data.json()
print(dlb_json)

def areaGuoTUPoint(dis):
    num1=0
    num2=0
    for guotu in guotu_json:
        Lat1 = guotu['t11']
        Lon1 = guotu['t10']
        Lat1 = float(Lat1)
        Lon1 = float(Lon1)
        #distance = geopy.distance.geodesic((Lat0, Lon0), (Lat1, Lon1)).km
        distance=getDistance(Lat0, Lon0,Lat1, Lon1)
        if (distance < dis):
            #print(str(guotu['id']) + ' ' + str(guotu['t13']) + ' ' + str(guotu['t14']))
            num1 +=float(guotu['t13'])
            num2 +=float(guotu['t14'])
            print(guotu)
    return str(num1)+' '+str(num2)

def areaJTPoint(dis):
    for jiaotong in jiaotong_json:
        #起始点经纬度
        Lat1 = jiaotong['t7']
        Lon1 = jiaotong['t6']
        Lat2 = jiaotong['t9']
        Lon2 = jiaotong['t8']
        Lat1 = float(Lat1)
        Lon1 = float(Lon1)
        Lat2 = float(Lat2)
        Lon2 = float(Lon2)
        #distance = geopy.distance.geodesic((Lat0, Lon0), (Lat1, Lon1)).km
        distance=getDistance(Lat0, Lon0,Lat1, Lon1)
        distance2= getDistance(Lat0, Lon0, Lat2, Lon2)
        if (distance < dis):
            #print(str(jiaotong['id']) + ' ' + str(jiaotong['t1']))
            print(jiaotong)
        if (distance2 < dis):
            #print(str(jiaotong['id']) + ' ' + str(jiaotong['t1']))
            print(jiaotong)
        return


n=0
for dlb in dlb_json:
    Lat0 = dlb['Lat']
    Lon0 = dlb['Lon']
    Lat0 = float(Lat0)
    Lon0 = float(Lon0)

    print(str(dlb['ClientID'])+' '+areaGuoTUPoint(1))
    #print(areaJTPoint(10))

# Lat0 = dlb_json[5]['Lat']
# Lon0 = dlb_json[5]['Lon']
# Lat0 = float(Lat0)
# Lon0 = float(Lon0)