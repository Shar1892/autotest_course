# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_smoke_division_positive_numbers():
    result = all_division(10, 2)
    assert result == 5


@pytest.mark.acceptance
def test_division_negative_numbers():
    result = all_division(-10, -2)
    assert result == 5


@pytest.mark.acceptance
def test_division_negative_number_to_positive_number():
    result = all_division(-10, 2)
    assert result == -5


def test_division_zero_to_positive_number():
    result = all_division(0, 2)
    assert result == 0


@pytest.mark.smoke
def test_smoke_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)