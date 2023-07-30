# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
life = 100000000
sleeping = 0

while True:
    if button_a.was_pressed():
        display.scroll(temperature())
 
    if button_a.was_pressed() or button_b.was_pressed():
        display.show(Image.HAPPY)
        life = 100000000
        sleeping = 0
    
    if accelerometer.was_gesture('shake'):
        display.show(Image.CONFUSED)
    
    if button_b.is_pressed():
        display.scroll(display.read_light_level())

    if pin_logo.is_touched():
        display.show(Image.COW)
        sleep(1000)

        life += 100
        sleeping -= 10

    if sleeping >= 10000:
        display.show(Image.ASLEEP) 
    if life <= 0:
      display.show(Image.SKULL)
    if life >= 10:
       display.show(Image.SAD)
    if life >= 1000:
        display.show(Image.CONFUSED)
    if life >= 100000:
        display.show(Image.FABULOUS)
    if life >= 10000000:
        display.show(Image.HAPPY)

    sleep(1000)
    life -= 10
    sleeping += 10


    




