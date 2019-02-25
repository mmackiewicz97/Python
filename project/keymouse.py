#from pynput.mouse import Listener, Button, Controller
import pynput.mouse
import time
mouse = pynput.mouse.Controller()
#time.sleep(2)
mouse.position = (481, 441)
mouse.position = (650, 259)
#time.sleep(2)
#def on_click(x, y, button, pressed):
#    if pressed:
#        print(x, y, button, pressed)
#with Listener(on_click=on_click) as listener:
#    listener.join()
#import pynput.keyboard 
#from pynput.keyboard import Controller, Key
#keyboard = Controller()
#for i in dir(Key):
#    print(i)
#keyboard = pynput.keyboard.Controller()
#keyboard.release(pynput.keyboard.Key.cmd)

#bashCommand = "pkill -u mateusz"
#import subprocess
#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#output, error = process.communicate()
#with keyboard.pressed(Key.alt):
#    keyboard.press(Key.tab)
#    time.sleep(0.01)
#    keyboarfrom pynput import keyboard
from pynput import keyboard
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
#with keyboard.Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join().release(Key.tab)
