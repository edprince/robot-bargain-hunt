#File for functions used throughout game

def sort_objects(x):
    '''Order objects by value

    Takes list of objects, each with a value attribute and orders'''
    for i in range(len(x) - 1):
        for i in range(len(x) - 1):
            if x[i].value < (x[i + 1].value):
                tmp = x[i + 1]
                x[i + 1] = x[i]
                x[i] = tmp
    return x

def calculate_distance(x1, y1, x2, y2):
    '''Calculate distance between two coordinates

    Takes 2 sets of coordinates, and calculates the distance between using
    Pythagoras's theorem'''
    width = math.sqrt((x2 - x1)**2)
    height = math.sqrt((y2 - y1)**2)
    return math.sqrt(width**2 + height**2)
