import os
import time
import shutil
import pytest
import tempfile
from log import log


def timer(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        log.info("Start: {} Finish: {}".format(time1, time2))
        return ret
    return wrap


@pytest.yield_fixture
def create_file(test_dir, request):
    td = ""

    @timer
    def opener(size):
        nonlocal td
        td = tempfile.mkdtemp(prefix="testfile_{}_".format(size), dir=test_dir)
        with tempfile.NamedTemporaryFile(mode='wb', dir=td, delete=False) as f:
            if size > 0:
                f.seek(size - 1)
                f.write(b'0')
        return f.name

    yield opener

    if request.node.rep_setup.failed:
        log.info("Setting up a test failed! {}".format(request.node.nodeid))
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            log.info("Executing test failed! {}".format(request.node.nodeid))
        else:
            if td:
                shutil.rmtree(td, ignore_errors=True)


test_size = [0, 1, 2, -16, 1048576]


# @pytest.mark.skipif(sys.platform == 'win32', reason="does not run on windows")
@pytest.mark.parametrize("file_size", test_size)
def test_file_size(file_size, create_file):
    log.info("test_file_size {}".format(file_size))
    file_path = create_file(file_size)
    log.info("Size: {} Path: {}".format(file_size, file_path))
    statistic = os.stat(file_path)
    log.info(statistic)
    assert statistic.st_size == file_size
