# 🌲🌊🚁🟩🔥🏥💛🪣➕🌧️🌩️🪙

# 🌲 - Дерево
# 🌊 - Река
# 🚁 - Вертолет
# 🟩 - Свободное поле
# 🔥 - Огонь
# 🏥 - Госпиталь
# 💛 - Жизни
# 🪣 - Резервуар для тушения
# ➕ - Апгрейд шоп
# 🌧️ - Облако
# 🌩️ - Молния
# 🪙 - Очки

from Map import Map
import time
import os

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
field.generate_forest(3,10)
field.generate_river(10)
field.generate_river(10)
field.print_map()

tick = 1

while True:
    os.system("clear")
    print("TICK", tick)
    field.print_map()
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
