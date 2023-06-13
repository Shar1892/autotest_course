# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test():
    # Здесь пишем код
    args = test.pytestmark[0].args
    args_str = ''
    for i in args:
        args_str += f'{i}, '
    print(args_str)
    pass
