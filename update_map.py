import folium

# 建立地圖
m = folium.Map(location=[24.1235, 120.6753], zoom_start=15)

# 增加標記點
folium.Marker([24.1235, 120.6753], popup="我的地點").add_to(m)

# 必須存成 index.html
m.save("index.html")
