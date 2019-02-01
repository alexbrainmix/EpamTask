import os
import errno
import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


def pytest_addoption(parser):
    parser.addoption("--test_dir", action="store", default="", help="Directory to create test directories and files")


@pytest.fixture(scope='session')
def test_dir(request):
    test_dir = request.config.getoption("--test_dir")
    path = os.getcwd()
    if test_dir:
        path = '{}{}{}'.format(path, "/", test_dir)
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
    yield path

    if not os.listdir(path):
        os.rmdir(path)
