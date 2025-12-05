from src.operaciones import suma, es_par

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_es_par():
    assert es_par(2) is True
    assert es_par(3) is False
    assert es_par(0) is True
