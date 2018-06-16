import pytest


class TestClass(object):
    @pytest.fixture(scope="class")
    
    def start(self):
        '''initialize fixture'''
        print("Fixture started")
        return 10

    def test_one(self, start):
        # x = "this"
        print("log test one")
        assert start==10

    def test_two(self, start):
        # x = "hello"
        # print("log test TWO!!!!!!!!!!!!")
        assert start==2
