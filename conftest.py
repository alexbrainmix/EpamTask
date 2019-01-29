import pytest


def pytest_addoption(parser):
    parser.addoption("--test_dir", action="store", default="")


@pytest.fixture (scope='session',)
def test_dir(request):
    print("conftest.py test_dir")
    return request.config.getoption("--test_dir")


def setup():
    print("basic setup into module")


def teardown():
    print("basic teardown into module")


def setup_module(module):
    print("module setup")


def teardown_module(module):
    print("module teardown")


def setup_function(function):
    print("function setup")


def teardown_function(function):
    print("function teardown")
