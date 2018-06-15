import pytest

class TestClass(object):
    @pytest.fixture(scope="class")
    
    def start(self):
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

# def capital_case(x):
#     return x.capitalize()

# def test_capital_case():
#     assert capital_case('semaphore') == 'Semaphore'

# def test_raises_exception_on_non_string_arguments():
#     with pytest.raises(TypeError):
#         capital_case(9)