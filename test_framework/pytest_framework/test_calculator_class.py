import pytest

class Test_calc():
    @pytest.mark.skip("skipped with some reason")
    @pytest.mark.parametrize("a",[1,2,3,4,5])
    @pytest.mark.regression
    def test_addition(self,setup,a):
        print("this is addition")
        print(a)

    @pytest.mark.skipif(5<3, reason="skipped becoz cond became true")
    @pytest.mark.parametrize("a,b,c", [(13,2,1), (5,3,1),(100,4,80)])
    @pytest.mark.regression
    def test_subration(self, setup,a,b,c):
        print("this is subration")
        print("subration", a-b-c)

    @pytest.mark.sanity
    def test_multiplication(self,setup):
        print("this is multiplication")