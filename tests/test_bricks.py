import sys
import os

# Agregar la ruta de 'src/' al sistema
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from bricks import construir_muro



def test_construir_muro():
    assert construir_muro(10) == "Muro de 10 ladrillos construido"
    assert construir_muro(0) == "No hay ladrillos para construir"
