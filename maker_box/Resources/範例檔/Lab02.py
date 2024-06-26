# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

# 從 machine 模組匯入 Pin 物件
from machine import Pin
# 匯入時間相關的 time 模組
import time

# 建立 15 號腳位的 Pin 物件, 設定為輸出腳位, 並命名為 led
led = Pin(15, Pin.OUT)

while True:          # 一直重複執行
    led.value(1)     # 點亮 LED
    time.sleep(0.5)  # 暫停 0.5 秒
    led.value(0)     # 熄滅 LED
    time.sleep(0.5)  # 暫停 0.5 秒