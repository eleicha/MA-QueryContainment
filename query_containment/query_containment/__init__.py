__version__ = '0.1.0'

from query_containment.query_containment.containmentGenerator.containmentGenerator import generateFilterContainment
from query_containment.query_containment.containmentCases.filer_containment_without_smt import identifyFilterContainment
from query_containment.query_containment.containmentCases.filter_containment_smt_solver_simple import identify_filter_containment_with_SMT_if_else
from query_containment.query_containment.containmentCases.filter_containment_smt_solver import identify_filter_containment_with_SMT

if __name__ == '__main__':
    print("Method | Query ----------------------------------------- | q1 c q2 | q2 c q1 |")

    for x in range(0, 10):
        filterContainment = generateFilterContainment()
        contained = identifyFilterContainment(filterContainment)
        z3_contained_simple = identify_filter_containment_with_SMT_if_else(filterContainment)
        z3_contained = identify_filter_containment_with_SMT(filterContainment)

        print("Simple | " + str(filterContainment) + " | " + str(contained[0]) + " | " + str(contained[1]))
        print("SMT if | " + str(filterContainment) + " | " + str(z3_contained_simple[0]) + " | " + str(z3_contained_simple[1]))
        print("SMT -- | " + str(filterContainment) + " | " + str(z3_contained[0]) + " | " + str(z3_contained[1]))

