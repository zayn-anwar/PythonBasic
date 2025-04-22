#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.


def descending_order(num):
    numList = list(map(int, str(num)))
    newnumList = []
    i = 0
    x = len(numList)
    while x > i:
        newnumList.append(max(numList))
        numList.remove(max(numList))
        i+=1
    newnewnumList = int("".join(map(str, newnumList)))
    return (newnewnumList)
