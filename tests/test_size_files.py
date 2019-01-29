import os
import sys
import pytest


@pytest.mark.skipif(sys.platform == 'win32', reason="does not run on windows")
class TestSizeFiles:
    def setup(self):
        print("3 basic setup into class")

    def teardown(self):
        print("5 basic teardown into class")

    def setup_class(cls):
        print("1 class setup")

    def teardown_class(cls):
        print("7 class teardown")

    def setup_method(self, method):
        print("2 method setup")

    def teardown_method(self, method):
        print("6 method teardown")
    """
    @pytest.fixture(autouse=True)
    def test_dir1(self, test_dir):
        print("test_dir")
        print(test_dir)
        if test_dir != "":
            print("test_dir = not free")
    """

    def creat_file(self, path, filename, size):
        filepath = os.path.join(path, filename)
        if not os.path.exists(path):
            os.makedirs(path)
        with open(filename, "wb") as f:
            f.seek(size - 1)
            f.write(b'0')


    def test_check_file_size(self, test_dir):
        print("4 test 3*4")
        print("test_dir1")
        print(test_dir)
        file_path = os.getcwd()
        file_name = "testfile1"
        file_size = 1024
        self.creat_file(file_path, file_name, file_size)
        print(os.stat(file_name).st_size)
        assert 3 * 4 == 12


    def test_strings_a_3(self):
        print("test a*3")
        assert 'a' * 3 == 'aaa'