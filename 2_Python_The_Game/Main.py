# 🌲🌊🚁🟩🔥🏥💛🪣🏭🌧️🌩️🪙

# 🌲 - Дерево
# 🌊 - Река
# 🚁 - Вертолет
# 🟩 - Свободное поле
# 🔥 - Огонь
# 🏥 - Госпиталь
# 💛 - Жизни
# 🪣 - Резервуар для тушения
# 🏭 - Апгрейд шоп
# 🌧️ - Облако
# 🌩️ - Молния
# 🪙 - Очки

from pynput import keyboard
from Map import Map
import time
import os
from Helicopter import Helicopter as Helico

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)

helico = Helico(MAP_W, MAP_H)

MOVES = {'w': (-1,0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
def procces_key(key):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
        
listener = keyboard.Listener(
    on_press=None,
    on_release=procces_key)
listener.start()

tick = 1

while True:
    os.system("clear")
    print(helico.x, helico.y)
    print("TICK", tick)
    field.process_helicopter(helico)
    helico.print_stats()
    field.print_map(helico)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
