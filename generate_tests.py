import os

TEMPLATE = """import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 5, 8)
])
def test_sum(a, b, expected):
    assert a + b == expected
"""

def create_tests():
    tests_dir = os.path.join(os.getcwd(), "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    test_file_path = os.path.join(tests_dir, "test_sample.py")
    with open(test_file_path, "w") as f:
        f.write(TEMPLATE)
    
    print(f"✅ Archivo de pruebas generado: {test_file_path}")

if __name__ == "__main__":
    create_tests()
