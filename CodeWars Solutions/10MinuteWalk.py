''' create a function that will return true if the walk the app gives you will take you exactly ten minutes 
and will, of course, return you to your starting point. Return false otherwise. '''

def is_valid_walk(walk):
    if len(walk)!=10:
        return False
    x = 0
    y = 0
    for step in walk:
        if step == 'n':
            y += 1
        elif step == 's':
            y -= 1
        elif step == 'e':
            x += 1
        elif step == 'w':
            x -= 1
    return (x == 0 and y == 0)
