from fn import *

class Item():
    def __init__(self, name, value, location, item_type):
        self.name = name
        self.value = value
        self.location = location
        self.item_type = item_type

item_1 = Item('coin', 2, (10, 4), 'treasure')
item_2 = Item('crown', 200, (14, 1), 'treasure')
item_3 = Item('spear', 30, (12, 19), 'weapon')
item_4 = Item('sword', 25, (3, 5), 'weapon')
item_5 = Item('pot', 10, (0, 8), 'tool')

objs = []

objs.append(item_1)
objs.append(item_2)
objs.append(item_3)
objs.append(item_4)
objs.append(item_5)

sorted_list = sort_objects(objs)

for i in range(len(sorted_list)):
    print(sorted_list[i].name)
