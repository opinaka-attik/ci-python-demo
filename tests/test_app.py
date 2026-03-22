import pytest
from app import add, divide


class TestAdd:
    def test_entiers_positifs(self):
        assert add(1, 2) == 3

    def test_entiers_negatifs(self):
        assert add(-1, -1) == -2

    def test_flottants(self):
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_zero(self):
        assert add(0, 0) == 0

    def test_type_invalide_str(self):
        with pytest.raises(TypeError):
            add("1", 2)

    def test_type_invalide_none(self):
        with pytest.raises(TypeError):
            add(None, 2)


class TestDivide:
    def test_division_normale(self):
        assert divide(10, 2) == 5.0

    def test_division_flottants(self):
        assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)

    def test_dividende_zero(self):
        assert divide(0, 5) == 0.0

    def test_division_par_zero(self):
        with pytest.raises(ValueError, match="Division par zéro"):
            divide(10, 0)

    def test_type_invalide_str(self):
        with pytest.raises(TypeError):
            divide("10", 2)

    def test_type_invalide_none(self):
        with pytest.raises(TypeError):
            divide(10, None)