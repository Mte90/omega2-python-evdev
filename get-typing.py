#!/usr/bin/env python3
from evdev import ecodes, InputDevice, categorize

numpad = InputDevice('/dev/input/event0')
print(numpad)
numpad.grab()
for event in numpad.read_loop():
    if event.type == ecodes.EV_KEY:
        press = categorize(event)
        if press.keystate == 1:
            print(press.keycode)
 
