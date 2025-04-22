#the function nb_year should return n number of entire years needed to get a population greater or equal to p.

def nb_year(p0, percent, aug, p):
    currentPop = 0
    year = 0
    while currentPop < p:
        currentPop = (p0 + (p0*(percent/100)) + aug)
        p0 = round(currentPop)
        year+=1
    return year
