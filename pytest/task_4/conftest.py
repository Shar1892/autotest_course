import pytest
import datetime


@pytest.fixture(scope='class')
def print_start_end():
    start = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'Начало {start}\n')
    yield
    end = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'Конец {end}\n')


@pytest.fixture(scope='function')
def print_duration():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    print(f'Тест прошел за {(end - start)}')
