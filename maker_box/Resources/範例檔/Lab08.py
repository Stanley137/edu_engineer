# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import Pin, PWM
import time

# 建立 15 號腳位的 PWM 物件, 並命名為 led
led = PWM(Pin(15))

while True:
    # 漸亮
    for i in range(0, 1024, 10): # 從 range() 中讀取 0→1023
        led.duty(i)
        time.sleep(0.01)

    # 漸暗
    for i in range(1023, -1, -10): # 從 range() 中讀取 1023→0
        led.duty(i)
        time.sleep(0.01)