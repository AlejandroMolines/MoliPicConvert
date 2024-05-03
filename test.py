import pytest
from PIL import Image
import os
from mpcimg import convert_image, resize_image  # Asume funciones de conversión y redimensionamiento

# Path para imágenes de ejemplo y resultados de tests
TEST_IMAGE_PATH = "mario.png"
TEST_OUTPUT_PATH = "mario.png"

def test_image_conversion():
    """ Testea la conversión de una imagen a otro formato. """
    output_format = 'PNG'  # Cambiar a formato PNG
    convert_image(TEST_IMAGE_PATH, TEST_OUTPUT_PATH, output_format)
    assert os.path.exists(TEST_OUTPUT_PATH), "La imagen convertida no fue creada."

    # Abrir la imagen convertida y verificar el formato
    with Image.open(TEST_OUTPUT_PATH) as img:
        assert img.format == 'PNG', "El formato de la imagen convertida no es PNG"

def test_image_resizing():
    """ Testea el redimensionamiento de una imagen. """
    width, height = 800, 600  # Nuevas dimensiones
    resize_image(TEST_IMAGE_PATH, TEST_OUTPUT_PATH, width, height)
    with Image.open(TEST_OUTPUT_PATH) as img:
        assert img.size == (width, height), "Las dimensiones de la imagen no coinciden con las esperadas"

def test_ui_elements():
    """ Testea la presencia de elementos de UI. """
    # Este test sería más complejo y podría necesitar herramientas como pytest-qt
    assert True  # Placeholder para un verdadero test de UI

# Usar fixtures de pytest para configuración previa y limpieza después de los tests
@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # Setup: Crea directorios o prepara el entorno de test
    yield
    # Teardown: Limpia archivos de prueba, etc.
    if os.path.exists(TEST_OUTPUT_PATH):
        os.remove(TEST_OUTPUT_PATH)
