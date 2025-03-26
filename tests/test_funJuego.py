from src.funJuego import calcular_puntaje

def test_calcular_puntaje():
    assert calcular_puntaje(5, 2) == 10
    assert calcular_puntaje(0, 10) == 0
    assert calcular_puntaje(3, 3) == 9
