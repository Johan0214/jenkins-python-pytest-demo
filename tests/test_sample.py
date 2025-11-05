def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 2 == 3

def test_failure_example():
    # Intentional fail so Jenkins shows red test
    assert 2 * 2 == 5
