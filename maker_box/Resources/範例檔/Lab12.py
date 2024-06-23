# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import Pin, PWM
import time

beeper = PWM(Pin(2, Pin.OUT))    # 用 2 號腳位控制蜂鳴器
button1 = Pin(16, Pin.IN)        # 用 D0 讀 OUT1 
button2 = Pin(14, Pin.IN)        # 用 D5 讀 OUT2
button3 = Pin(12, Pin.IN)        # 用 D6 讀 OUT3
button4 = Pin(13, Pin.IN)        # 用 D7 讀 OUT4 
button5 = Pin(15, Pin.IN)        # 用 D8 讀 OUT5
button6 = Pin(5, Pin.IN)         # 用 D1 讀 OUT6
button7 = Pin(4, Pin.IN)         # 用 D2 讀 OUT7
                                 
tones = {                        # 儲存音名與頻率的字典
    'c': 262,                    # Do
    'd': 294,                    # Re
    'e': 330,                    # Mi
    'f': 349,                    # Fa
    'g': 392,                    # So
    'a': 440,                    # La
    'b': 494,                    # Si
}

while True:                      # 持續讀取觸控按鈕訊號
    if button1.value() == 1:     # 按了 1 號按鈕
        beeper.duty(512)         # 設定一半音量
        beeper.freq(tones['c'])  # 設定 Do 的頻率
        
    elif button2.value() == 1:   # 按了 2 號按鈕
        beeper.duty(512)         # 設定一半音量
        beeper.freq(tones['d'])  # 設定 Re 的頻率
                                 
    elif button3.value() == 1:   # 按了 3 號按鈕
        beeper.duty(512)         # 設定一半音量
        beeper.freq(tones['e'])  # 設定 Mi 的頻率
                                 
    elif button4.value() == 1:   # 按了 4 號按鈕
        beeper.duty(512)         # 設定一半音量
        beeper.freq(tones['f'])  # 設定 Fa 的頻率
                                 
    elif button5.value() == 1:   # 按了 5 號按鈕
        beeper.duty(512)         # 設定一半音量
        beeper.freq(tones['g'])  # 設定 So 的頻率
                                 
    elif button6.value() == 1:   # 按了 6 號按鈕
        beeper.duty(512)         # 設定一半音量
        beeper.freq(tones['a'])  # 設定 La 的頻率
                                 
    elif button7.value() == 1:   # 按了 7 號按鈕
        beeper.duty(512)         # 設定一半音量
        beeper.freq(tones['b'])  # 設定 Si 的頻率
                                 
    else:                        # 沒有按鈕
        beeper.duty(0)           # 設定不發聲

    time.sleep(0.05)

