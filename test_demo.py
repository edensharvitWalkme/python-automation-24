import pytest


@pytest.fixture()  # decorator
def setup_teardown():
    print("\nBefore test")  # Before test
    yield  # Test execution
    print("\nTaking screenshot")  # After test
    print("Taking Logs")  # After test


def test_demo_1():
    assert 1 == 1


def test_demo_2(setup_teardown):
    print("Testing!")
    assert 2 > 1
