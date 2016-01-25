#Code here independent of Pygame currently, keeping compatibility options open
from functions import *
from classes import *

objs = []

#Initialize items
item_1 = Item('coin', 2, (10, 4), 'treasure', 10)
item_2 = Item('crown', 200, (14, 1), 'treasure', 2)
item_3 = Item('spear', 30, (12, 19), 'weapon', 5)
item_4 = Item('sword', 25, (3, 5), 'weapon', 4)
item_5 = Item('pot', 10, (0, 8), 'tool', 10)

objs.extend((item_1, item_2, item_3, item_4, item_5))

sorted_list = sort_objects(objs)

for i in range(len(sorted_list)):
    print(sorted_list[i].name)
