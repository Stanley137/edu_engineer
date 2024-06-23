# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import ADC, Pin

# 建立 A0 腳位的 ADC 物件，並命名為 adc
adc = ADC(0)
# 建立 15 號腳位的 Pin 物件, 設定為輸出腳位, 並命名為 led
led = Pin(15, Pin.OUT)

while True:
    if adc.read() < 100: # 光線不足
        led.value(1)     # 打開 LED 燈
    else:                # 否則
        led.value(0)     # 關閉 LED 燈