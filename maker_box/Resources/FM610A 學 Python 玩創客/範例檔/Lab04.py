# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import Pin

# 建立 16 號腳位的 Pin 物件, 設定為輸入腳位, 並命名為 button
button = Pin(16, Pin.IN)
# 建立 15 號腳位的 Pin 物件, 設定為輸出腳位, 並命名為 led
led = Pin(15, Pin.OUT)

while True:
    if button.value() == 1:  # 如果觸控按鈕被碰觸
        led.value(1)         # 點亮 LED
    else:                    # 否則 (觸控按鈕沒有碰觸)
        led.value(0)         # 熄滅 LED