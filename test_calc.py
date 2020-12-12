import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect", [(3, 5, 8), (-1, -2, -3), (100, 200, 300)], ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [(4, 8, -4), (-6, -5, -1), (99, 108, -9)], ids=["int", "minus", "bigint"])
    def test_sub(self, a, b, expect):
        assert expect == self.cal.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [(4, 8, 32), (-6, -5, 30), (99, 108, 10692)], ids=["int", "minus", "bigint"])
    def test_mul(self, a, b, expect):
        assert expect == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [(60, 5, 12), (-6, -5, 1.2), (500, 100, 5)], ids=["int", "minus", "bigint"])
    def test_div(self, a, b, expect):
        assert expect == self.cal.div(a, b)


