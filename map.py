from pyecharts import Map, Geo

# 区县 -- 具体城市内的区县  xx县
quxian = ['夏县', '临猗县', '稷山县', '新绛县', '万荣县', '闻喜县']
values3 = [3, 5, 7, 8, 2, 4]


# # 商丘地图 数据为商丘市下的区县
map3 = Map("商丘地图",'运城', width=1200, height=600)
map3.add("运城", quxian, values3, visual_range=[1, 10], maptype='运城', is_visualmap=True,visual_text_color='#000')
map3.render(path="./data/04-03运城地图.html")
