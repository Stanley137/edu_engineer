# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import Pin
import time

# 建立串列, 依序儲存 D0、D5、D6、D7、D8、D1、D2 腳位編號
leds = [16, 14, 12, 13, 15, 5, 4]

while True:                    # 重複跑馬燈效果
    for i in leds:             # 依序取出個別腳位編號
        led = Pin(i, Pin.OUT)  # 設定當前腳位為輸出功能
        led.value(1)           # 點亮對應的 LED
        time.sleep(0.1)        # 等待 0.1 秒
        led.value(0)           # 熄滅剛剛點亮的 LED