import keyboard
import random

y = 0



while y < 1:
    if keyboard.is_pressed('x'):
        x = 0
        while x < 6:
            keyboard.send('tab')
            x += 1
            print(x)
        keyboard.write('mine', delay=.1)
        keyboard.send('return')
        keyboard.send('right')
        continue
    elif keyboard.is_pressed('q'):
        break
    else:
        continue
