#File for functions used throughout game
import random

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

def random_move():
    '''Generates a movement in a random direction

    Moves the player sprite by one tile in a random direction'''
    #True equates to x, False equates to y
    direction = random.choice([True, False])
    value = random.choice([-1, 1])
    return (direction, value)


    
