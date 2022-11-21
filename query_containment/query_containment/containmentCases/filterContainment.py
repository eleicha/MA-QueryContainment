


def identifyContainment(containment):
    splittedContainment = containment.split(' ')

    switch={
        '<': smallerThan(),
        '>': largerThan(),
        '<=': smallerOrEqual(),
        '>=': largerOrEqual(),
        '=': equal(),
        '!=': unequal(),

    }
