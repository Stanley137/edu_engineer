# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

import network, urequests, ujson, machine
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('FLAG-SCHOOL', '12345678')
while not sta_if.isconnected():
    pass
print(sta_if.ifconfig()[0])        # 顯示 IP 位址

res = urequests.get(               # API 網址
    "https://api.openweathermap.org/data/2.5/weather?" +
    "q=" + "Taipei" + ",TW" +      # 指定城市與國別
    "&units=metric&lang=zh_tw&" +  # 使用攝氏單位
    "appid=" +  # 以下填入註冊後取得的 API key
    "be95d10b9f29a0b5dfde30d109afb831")
j = ujson.loads(res.text);         # 從 JSON 轉成字典
gLED = machine.Pin(16, machine.Pin.OUT) # 控制綠燈
rLED = machine.Pin(14, machine.Pin.OUT) # 控制紅燈
weatherID = j["weather"][0]["id"]       # 天氣狀況代碼
weatherDesc = j["weather"][0]["description"] # 天氣狀況
if weatherID < 800:                # 雨天
    rLED.value(1)                  # 亮紅燈
    gLED.value(0)
else:                              # 沒下雨
    rLED.value(0)                  # 亮綠燈
    gLED.value(1)
print("目前天氣：", str(weatherID))
print("代碼意義：", weatherDesc )

