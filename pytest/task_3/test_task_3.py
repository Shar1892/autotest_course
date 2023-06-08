# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("numerator, denominator, expected_result", [
    (-10, -2, 5),
    (-10, 2, -5),
    (0, 2, 0),
    pytest.param(10, 2, 5, marks=pytest.mark.smoke),
    pytest.param(10, 0, ZeroDivisionError, marks=pytest.mark.skip(reason="Деление на 0"))
    ])
def test_all_division(numerator, denominator, expected_result):
    result = all_division(numerator, denominator)
    assert result == expected_result
