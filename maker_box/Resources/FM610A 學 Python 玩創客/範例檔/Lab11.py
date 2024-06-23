# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import Pin, PWM
import time

beeper = PWM(Pin(2, Pin.OUT)) # 使用 2 號腳位控制蜂鳴器
#|5 3 3 -|4 2 2 -|1 2 3 4 5 5 5|
# 0 表示休止符
notes = [
    392, 330, 330, 0, 
    349, 294, 294, 0,
    262, 294, 330, 349, 392, 392, 392, 0]

for note in notes:        # 一一取出音符
    if note == 0:         # 休止符不發音
        beeper.duty(0)
    else:
        beeper.duty(512)  # 設定為一半音量
        beeper.freq(note) # 依照音符設定頻率
    time.sleep(0.2)       # 讓聲音持續 02秒
    beeper.duty(0)        # 停止發聲
    time.sleep(0.1)       # 持續無聲 01 秒    
