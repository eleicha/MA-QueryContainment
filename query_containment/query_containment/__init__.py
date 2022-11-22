__version__ = '0.1.0'

from containmentGenerator.containmentGenerator import generateFilterContainment
from containmentCases.filterContainment import identifyFilterContainment

if __name__ == '__main__':
    print("Query ---------------------------- | q1 c q2 | q2 c q1 |")

    for x in range(0, 10):
        filterContainment = generateFilterContainment()
        contained = identifyFilterContainment(filterContainment)

        print(str(filterContainment) + " | " + str(contained[0]) + " | " + str(contained[1]))
