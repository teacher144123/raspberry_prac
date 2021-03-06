import RPi.GPIO as gpio
import time

def beepTimes(times):
    beep_num = 12
    gpio.setmode(gpio.BCM)
    gpio.setup(beep_num, gpio.OUT)

    p = gpio.PWM(12, 0.5)

    for i in range(times):
        p.start(1)
        p.ChangeFrequency(659)
        time.sleep(0.1)
        p.stop()
        time.sleep(0.4)
