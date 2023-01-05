import random as rn


# generates two filters of form a x b; a y c;
# x and y can take on '<; <=; >; >=; ==; !='
# Todo: add different column generator
def generateFilterContainment():
    # numerical filter predicates
    b = int(rn.random()*100)
    c = int(rn.random()*100)
    # mathematical symbols
    x = rn.random()
    y = rn.random()

    x = chooseSymbol(x)
    y = chooseSymbol(y)

    q_1 = 'x ' + str(x) + ' ' + str(b)
    q_2 = 'x ' + str(y) + ' ' + str(c)

    return [q_1, q_2]


def chooseSymbol(x):
    if x <= (100 / 6 / 100):
        return '<'
    elif x <= 2 * (100 / 6 / 100):
        return '<='
    elif x <= 3 * (100 / 6 / 100):
        return '>'
    elif x <= 4 * (100 / 6 / 100):
        return '>='
    elif x <= 5 * (100 / 6 / 100):
        return '=='
    elif x <= 6 * (100 / 6 / 100):
        return '!='
