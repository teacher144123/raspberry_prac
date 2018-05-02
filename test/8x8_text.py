import RPi.GPIO as gpio
import time

def setupAll():
    gpio.setmode(gpio.BCM)
    global col_led, row_led
    for i in col_led + row_led:
        print(str(i) + 'is setting')
        try:
            gpio.setup(i, gpio.OUT)
        except:
            print(i)
col_led = [17, 27, 22, 5, 6, 13, 19, 26]
row_led = [14, 15, 18, 23, 12, 16, 20, 21]

if __name__ == '__main__':
    try:
        setupAll()


        for i in range(len(col_led)):
            gpio.output(col_led[i], gpio.LOW)
            gpio.output(col_led[i], gpio.HIGH)
        for i in range(len(row_led)):
            gpio.output(row_led[i], gpio.HIGH)
            gpio.output(row_led[i], gpio.LOW)


        time.sleep(10)

    except:
        gpio.cleanup()
