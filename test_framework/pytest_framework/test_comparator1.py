import pytest

class Test_comparator:#Test Suite--->collecvtion of test cases
    @pytest.mark.sanity
    def test_greaterthan(self, setup, setup_class, setup_Module):
        print("this is greater than func")

    @pytest.mark.xfail
    @pytest.mark.sanity
    def test_lesserthan(self, setup2, setup_class, setup_Module):
        var = setup2
        print(var[0])
        print(var[1])

        print("this is lesser than func")

    @pytest.mark.sanity
    def test_notequalto(self, setup, setup_class, setup_Module):
        print("this is not equal to func")