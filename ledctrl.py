#!/usr/bin/env python

from daylight import SunRange
from bibliopixel.drivers.visualizer import *
from bibliopixel import LEDStrip
import time

num_leds = 10

driver = DriverVisualizer(num_leds, stayTop=True)
led_strip = LEDStrip(driver)
pdx = SunRange()

def nightRemainingRGB():
    return (178, 102, 255)

def nightFadedRGB():
    return (76, 0, 153)

def dayRemainingRGB():
    return (255, 255, 51)

def dayFadedRGB():
    return (150, 150, 0)


led_strip.fill(dayRemainingRGB())
led_strip.update()

for i in range(0, num_leds):
    time.sleep(1)
    led_strip.fill(dayFadedRGB(), 0, i)
    led_strip.update()

led_strip.fill(nightRemainingRGB())
led_strip.update()

for i in range(0, num_leds):
    time.sleep(1)
    led_strip.fill(nightFadedRGB(), 0, i)
    led_strip.update()
