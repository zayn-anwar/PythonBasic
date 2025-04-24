"""Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"""

def likes(names):
    x = 0
    if names:
        if len(names) == 1:
            return (names[0] + " likes this")
        elif len(names) == 2:
            return (names[0] + " and " + names[1] + " like this")
        elif len(names) == 3:
            return (names[0] + ", " + names[1] + " and " + names[2] + " like this")
        elif len(names) >= 3:
            x = len(names)-2
            return (names[0] + ", " + names[1] + " and " + str(x) + " others like this")
    else:
        return "no one likes this"
