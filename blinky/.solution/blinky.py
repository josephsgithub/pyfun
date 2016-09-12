"""My Library of Blinky Light Functions"""

import RPi.GPIO as GPIO
import time as t

pins  = [4,27,22,5,6,13,19,26]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins,GPIO.OUT)

def on(pins=pins): GPIO.output(pins,GPIO.HIGH)

def off(pins=pins): GPIO.output(pins,GPIO.LOW)

def slowon(delay=.1,list=pins): 
    for pin in list:
        on(pin)
        t.sleep(delay)

def slowoff(delay=.1,list=pins): 
    for pin in list:
        off(pin)
        t.sleep(delay)

def chase(count=1,delay=.1):
    for n in range(count):
        slowon(delay)
        slowoff(delay)

def updown(count=1,delay=.1):
    for n in range(count):
        slowon(delay)
        slowoff(delay,pins[::-1])

def downup(count=1,delay=.1):
    for n in range(count):
        slowon(delay,pins[::-1])
        slowoff(delay)

patterns = [chase,updown]

if __name__ == "__main__":
    for n in range(20):
        chase(2,.01)
