import pytest
from src.nueva_funcionalidad import es_par, contar_vocales, invertir_lista

def test_es_par():
    assert es_par(2) == True
    assert es_par(3) == False
    assert es_par(0) == True

def test_contar_vocales():
    assert contar_vocales("Hola") == 2
    assert contar_vocales("PyThOn") == 1
    assert contar_vocales("AEIOU") == 5

def test_invertir_lista():
    assert invertir_lista([1, 2, 3]) == [3, 2, 1]
    assert invertir_lista([]) == []
    assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
