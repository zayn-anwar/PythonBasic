""" Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.
For example, when the input is green, output should be yellow. """


def update_light(current):
    match current:
        case "green":
            return "yellow"
        case "yellow":
            return "red"
        case "red":
            return "green"
