from ..query_containment import __version__
from ..query_containment.containmentCases.filer_containment_without_smt import identifyFilterContainment
from ..query_containment.containmentCases.filter_containment_smt_solver_simple import identify_filter_containment_with_SMT_if_else
from ..query_containment.containmentCases.filter_containment_smt_solver import identify_filter_containment_with_SMT


def test_version():
    assert __version__ == '0.1.0'

def test_filter_containment():
    assert identifyFilterContainment(['x > 5', 'x < 6']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x > 5', 'x < 6']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT(['x > 5', 'x < 6']) == [0, 0], "Should be [0, 0]"
    assert identifyFilterContainment(['x >= 5', 'x <= 6']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x >= 5', 'x <= 6']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT(['x >= 5', 'x <= 6']) == [0, 0], "Should be [0, 0]"
    assert identifyFilterContainment(['x < 5', 'x > 6']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x < 5', 'x > 6']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT(['x < 5', 'x > 6']) == [0, 0], "Should be [0, 0]"
    assert identifyFilterContainment(['x <= 5', 'x >= 6']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x <= 5', 'x >= 6']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT(['x <= 5', 'x >= 6']) == [0, 0], "Should be [0, 0]"
    assert identifyFilterContainment(['x == 5', 'x == 6']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x == 5', 'x == 6']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT(['x == 5', 'x == 6']) == [0, 0], "Should be [0, 0]"
    assert identifyFilterContainment(['x == 5', 'x < 5']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x == 5', 'x < 5']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT(['x == 5', 'x < 5']) == [0, 0], "Should be [0, 0]"
    assert identifyFilterContainment(['x == 5', 'x > 5']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x == 5', 'x > 5']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT(['x == 5', 'x > 5']) == [0, 0], "Should be [0, 0]"
    assert identifyFilterContainment(['x == 5', 'x <= 4']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x == 5', 'x >= 6']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT(['x == 5', 'x >= 6']) == [0, 0], "Should be [0, 0]"
    assert identifyFilterContainment(['x != 5', 'x <= 5']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x != 5', 'x <= 5']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT(['x != 5', 'x <= 5']) == [0, 0], "Should be [0, 0]"
    assert identifyFilterContainment(['x != 5', 'x >= 5']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x != 5', 'x >= 5']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT(['x != 5', 'x >= 5']) == [0, 0], "Should be [0, 0]"
    assert identifyFilterContainment(['x != 5', 'x == 5']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x != 5', 'x == 5']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT(['x != 5', 'x == 5']) == [0, 0], "Should be [0, 0]"
    assert identifyFilterContainment(['x != 5', 'x < 8']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x != 5', 'x < 8']) == [0, 0], "Should be [0, 0]"
    assert identify_filter_containment_with_SMT(['x != 5', 'x < 8']) == [0, 0], "Should be [0, 0]"

    assert identify_filter_containment_with_SMT_if_else(['x > 7', 'x > 6']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT(['x > 7', 'x > 6']) == [1, 0], "Should be [1, 0]"
    assert identifyFilterContainment(['x > 7', 'x > 6']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x < 7', 'x < 8']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT(['x < 7', 'x < 8']) == [1, 0], "Should be [1, 0]"
    assert identifyFilterContainment(['x < 7', 'x < 8']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x < 7', 'x <= 8']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT(['x < 7', 'x <= 8']) == [1, 0], "Should be [1, 0]"
    assert identifyFilterContainment(['x < 7', 'x <= 8']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x < 7', 'x <= 7']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT(['x < 7', 'x <= 7']) == [1, 0], "Should be [1, 0]"
    assert identifyFilterContainment(['x < 7', 'x <= 7']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x < 7', 'x != 7']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT(['x < 7', 'x != 7']) == [1, 0], "Should be [1, 0]"
    assert identifyFilterContainment(['x < 7', 'x != 7']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x < 7', 'x != 8']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT(['x < 7', 'x != 8']) == [1, 0], "Should be [1, 0]"
    assert identifyFilterContainment(['x < 7', 'x != 8']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x == 7', 'x > 6']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT(['x == 7', 'x > 6']) == [1, 0], "Should be [1, 0]"
    assert identifyFilterContainment(['x == 7', 'x > 6']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x == 7', 'x < 8']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT(['x == 7', 'x < 8']) == [1, 0], "Should be [1, 0]"
    assert identifyFilterContainment(['x == 7', 'x < 8']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x >= 7', 'x >= 6']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT(['x >= 7', 'x >= 6']) == [1, 0], "Should be [1, 0]"
    assert identifyFilterContainment(['x >= 7', 'x >= 6']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT_if_else(['x <= 7', 'x <= 8']) == [1, 0], "Should be [1, 0]"
    assert identify_filter_containment_with_SMT(['x <= 7', 'x <= 8']) == [1, 0], "Should be [1, 0]"
    assert identifyFilterContainment(['x <= 7', 'x <= 8']) == [1, 0], "Should be [1, 0]"

    assert identify_filter_containment_with_SMT_if_else(['x < 7', 'x < 6']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT(['x < 7', 'x < 6']) == [0, 1], "Should be [0, 1]"
    assert identifyFilterContainment(['x < 7', 'x < 6']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT_if_else(['x <= 7', 'x < 7']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT(['x <= 7', 'x < 7']) == [0, 1], "Should be [0, 1]"
    assert identifyFilterContainment(['x <= 7', 'x < 7']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT_if_else(['x <= 8', 'x < 7']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT(['x <= 8', 'x < 7']) == [0, 1], "Should be [0, 1]"
    assert identifyFilterContainment(['x <= 8', 'x < 7']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT_if_else(['x > 5', 'x > 6']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT(['x > 5', 'x > 6']) == [0, 1], "Should be [0, 1]"
    assert identifyFilterContainment(['x > 5', 'x > 6']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT_if_else(['x >= 5', 'x >= 6']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT(['x >= 5', 'x >= 6']) == [0, 1], "Should be [0, 1]"
    assert identifyFilterContainment(['x >= 5', 'x >= 6']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT_if_else(['x != 5', 'x == 6']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT(['x != 5', 'x == 6']) == [0, 1], "Should be [0, 1]"
    assert identifyFilterContainment(['x != 5', 'x == 6']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT_if_else(['x != 5', 'x > 5']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT(['x != 5', 'x > 5']) == [0, 1], "Should be [0, 1]"
    assert identifyFilterContainment(['x != 5', 'x > 5']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT_if_else(['x != 5', 'x >= 6']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT(['x != 5', 'x >= 6']) == [0, 1], "Should be [0, 1]"
    assert identifyFilterContainment(['x != 5', 'x >= 6']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT_if_else(['x != 5', 'x < 5']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT(['x != 5', 'x < 5']) == [0, 1], "Should be [0, 1]"
    assert identifyFilterContainment(['x != 5', 'x < 5']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT_if_else(['x != 5', 'x <= 4']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT(['x != 5', 'x <= 4']) == [0, 1], "Should be [0, 1]"
    assert identifyFilterContainment(['x != 5', 'x <= 4']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT_if_else(['x > 8', 'x == 39']) == [0, 1], "Should be [0, 1]"
    assert identify_filter_containment_with_SMT(['x > 8', 'x == 39']) == [0, 1], "Should be [0, 1]"
    assert identifyFilterContainment(['x > 8', 'x == 39']) == [0, 1], "Should be [0, 1]"

