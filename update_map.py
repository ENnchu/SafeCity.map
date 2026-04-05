import folium

# 建立地圖
m = folium.Map(location=[24.1235, 120.6753], zoom_start=15)

# 增加標記點
folium.Marker([24.1235, 120.6753], popup="我的地點").add_to(m)

# 將地圖存成 index.html 檔案
# 這一行會把複雜的 HTML 碼寫入 index.html，覆蓋掉你原本的文字
m.save("index.html")
