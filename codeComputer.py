import requests
address = '34.925,110.387777777778'
# address=str(i[0])+','+str(i[1])
url = 'http://api.map.baidu.com/geocoder?output=json&key=f247cdb592eb43ebac6ccd27f796e2d2&location=' + str(address)
response = requests.get(url)
answer = response.json()
print(answer)