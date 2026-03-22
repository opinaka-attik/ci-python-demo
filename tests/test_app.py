import pytest
from app import sum, divide

def test_sum_entiers():
    assert sum(1, 2) == 3

def test_sum_negatifs():
    assert sum(-1, -1) == -2

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_par_zero():
    with pytest.raises(ValueError, match="Division par zéro"):
        divide(10, 0)
```

**`requirements.txt`**
```
pytest==8.2.0
pytest-cov==5.0.0