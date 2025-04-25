'''In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.
You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is 
the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression. '''


def printer_error(s):
    chars = ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    counted = 0
    for i in list(s):
        if i.upper() in chars:
            counted+=1
    return str(counted) + "/" + str(len(s))
