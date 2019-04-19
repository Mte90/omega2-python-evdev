# omega2-python-evdev
python(3)-evdev library for [Onion Omega2](https://onion.io/)

## Instructions

- ssh to your onion omega2
- download the repo `git clone https://github.com/Mte90/omega2-python-evdev`
- install for python2: `opkg install python-evdev_0.7.0-1_mipsel_24kc`
- install for python3: `opkg install python3-evdev_0.7.0-1_mipsel_24kc`
- use it in your python scripts! For more: http://python-evdev.readthedocs.io

## usb-gamepad.py
Plug a usb joystick/gamepad on your onion [expansion dock](https://docs.onion.io/omega2-docs/expansion-dock.html). After a few seconds a new `device file` should appear in omega's `/dev/input` directory, usually named `event0`. `python-evdev` can read this device file and faciliates the translation of the events. 

For now `usb-gamepad.py` script just connects to `/dev/input/event0` and displays info about the joystick/gamepad controller connected to the usb port. It can be expanded to perform basic functions such as read the buttons' states.

Run it with: `python(3) usb-gamepad.py`

## get-typing.py
Like the previous but this shows only the buttons when they are pressed and not also when they are released.

Run it with: `python(3) get-typing.py`
