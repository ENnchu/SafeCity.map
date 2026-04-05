import folium

# 1. 建立地圖 (中心點設在台中)
m = folium.Map(location=[24.1235, 120.6753], zoom_start=15)

# 2. 加入一個測試點
folium.Marker(
    location=[24.1235, 120.6753],
    popup="NCHU 中興大學",
    icon=folium.Icon(color='blue')
).add_to(m)

# 3. 儲存成 index.html (這步最重要，檔名不能錯)
m.save("index.html")
print("地圖已成功更新！")
