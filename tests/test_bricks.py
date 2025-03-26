from src.bricks import construir_muro

def test_construir_muro():
    assert construir_muro(10) == "Muro de 10 ladrillos construido"
    assert construir_muro(0) == "No hay ladrillos para construir"
