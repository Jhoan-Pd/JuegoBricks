import sys
import os

# Agregar la ruta de 'src/' al sistema
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.dados import lanzar_dado
def test_lanzar_dado():
    resultado = lanzar_dado(6)  # Simula el lanzamiento de un dado de 6 caras
    assert 1 <= resultado <= 6  # Verifica que el resultado esté en el rango esperado
