from random import randint
def randomColorGen(ColorGroup):
    red = 0
    blue = 0
    green = 0
    dic = {"red": 0, "blue": 1, "green": 2}
    if dic[ColorGroup] == 0:
        while (red < blue) or (red < green):
            red = randint(0,255)
            blue = randint(0,255)
            green = randint(0,255)
    elif dic[ColorGroup] == 1:
        while (blue < red) or (blue < green):
            red = randint(0,255)
            blue = randint(0,255)
            green = randint(0,255)
    else:
        while (green < red) or (green < blue):
            red = randint(0,255)
            blue = randint(0,255)
            green = randint(0,255)
    color = '#%02x%02x%02x' % (red, green, blue)
    return color
