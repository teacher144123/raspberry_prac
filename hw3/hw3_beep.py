import RPi.GPIO as gpio
import time

if __name__ == '__main__':
    beep_num = 12
    gpio.setmode(gpio.BCM)
    gpio.setup(beep_num, gpio.OUT)

    p = gpio.PWM(12, 0.5)

    for i in range(3):
        p.start(1)
        p.ChangeFrequency(659)
        time.sleep(0.3)
        p.stop()
        time.sleep(0.7)

    GPIO.cleanup()
