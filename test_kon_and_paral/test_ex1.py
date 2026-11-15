import pytest

from kon_and_paral.ex1 import fibonachi, prime_number, factorial


@pytest.fixture
def data():
    return 10

def test_fibonachi(data):
    assert fibonachi(data) == 5

def test_prime_number(data):
    assert prime_number(data) == [2,3,5,7]

def test_factorial(data):
    assert factorial(data) == 3628800