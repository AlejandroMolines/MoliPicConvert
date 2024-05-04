import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QLineEdit, QFileDialog, QMessageBox, QFrame)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pathlib import Path
from PIL import Image
import os
from urllib.request import Request, urlopen
#io es un modulo de entrada/salida que permite leer y escribir datos en diferentes tipos de archivos
import io

#Funcion para obtener la ruta de descarga por defecto
def get_default_download_path():
    return str(Path.home() / "Downloads")

class ImageConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("MoliPicConverter")
        self.setFixedSize(800, 500)
        self.setStyleSheet("background-color: #e1e0ff;")

        # Layout principal
        layout = QVBoxLayout(self)

        # Selector de modo de operación
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Convertir desde archivo", "Convertir desde URL"])
        self.mode_selector.currentIndexChanged.connect(self.switch_mode)
        layout.addWidget(self.mode_selector)

        # Label y entrada para la ruta del archivo o URL
        self.label1 = QLabel("Selecciona la imagen a convertir:")
        self.input_path_edit = QLineEdit()
        self.input_path_edit.setReadOnly(True)
        self.input_path_edit.setStyleSheet("height: 30px; padding: 5px; border-radius: 5px; background: #f0f0ff; color: #000;")
        self.browse_button = QPushButton("Buscar...")
        self.browse_button.clicked.connect(self.browse_file)
        self.browse_button.setStyleSheet("background-color: #a0a0ff; color: #000; border-radius: 5px; padding: 5px;")
        self.url_edit = QLineEdit()
        self.url_edit.setPlaceholderText("Introduce URL de la imagen aquí")
        self.url_edit.setStyleSheet("height: 30px; padding: 5px; border-radius: 5px; background: #f0f0ff; color: #000;")
        self.download_button = QPushButton("Previsualizar imagen")
        self.download_button.clicked.connect(self.download_and_preview_image)
        self.download_button.setStyleSheet("background-color: #a0a0ff; color: #000; border-radius: 5px; padding: 5px;")

        # Configuración del layout de entrada
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.label1)
        input_layout.addWidget(self.input_path_edit)
        input_layout.addWidget(self.browse_button)
        input_layout.addWidget(self.url_edit)
        input_layout.addWidget(self.download_button)
        layout.addLayout(input_layout)

        # Previsualización de la imagen
        self.image_label = QLabel()
        self.image_label.setFrameStyle(QFrame.StyledPanel)
        layout.addWidget(self.image_label)

        # Configuración para guardar la imagen convertida
        self.output_path_edit = QLineEdit()
        self.output_path_edit.setReadOnly(True)
        self.output_path_edit.setStyleSheet("height: 30px; padding: 5px; border-radius: 5px; background: #f0f0ff; color: #000;")
        self.filename_edit = QLineEdit()
        self.filename_edit.setPlaceholderText("Enter file name here")
        self.filename_edit.setStyleSheet("height: 30px; padding: 5px; border-radius: 5px; background: #f0f0ff; color: #000;")
        self.format_cb = QComboBox()
        self.format_cb.addItems([".jpg", ".png", ".gif", ".webp"])
        self.format_cb.setStyleSheet("background: #f0f0ff; color: #000;")
        save_button = QPushButton("Guardar como...")
        save_button.clicked.connect(self.save_file)
        save_button.setStyleSheet("background-color: #a0a0ff; color: #000; border-radius: 5px; padding: 5px;")

        # Configuración del layout de salida
        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_path_edit)
        output_layout.addWidget(self.filename_edit)
        output_layout.addWidget(self.format_cb)
        output_layout.addWidget(save_button)
        layout.addLayout(output_layout)

        # Botones de conversión y reseteo
        buttons_layout = QHBoxLayout()
        convert_button = QPushButton("Convertir")
        convert_button.clicked.connect(self.convert_image)
        convert_button.setStyleSheet("QPushButton { background-color: #a0a0ff; color: #000; border-radius: 5px; padding: 10px; } QPushButton:hover { background-color: #9090ff; }")
        buttons_layout.addWidget(convert_button, 75)
        reset_button = QPushButton("Resetear")
        reset_button.clicked.connect(self.reset_fields)
        reset_button.setStyleSheet("QPushButton { background-color: #a0a0ff; color: #000; border-radius: 5px; padding: 10px; } QPushButton:hover { background-color: #9090ff; }")
        buttons_layout.addWidget(reset_button, 25)
        layout.addLayout(buttons_layout)

        # Ocultar los componentes de URL al inicio
        self.url_edit.hide()
        self.download_button.hide()

        # Establecer el layout principal en el widget
        self.setLayout(layout)
        
    def switch_mode(self):
        if self.mode_selector.currentText() == "Convertir desde archivo":
            self.url_edit.hide()
            self.download_button.hide()
            self.input_path_edit.show()
            self.browse_button.show()
        else:
            self.input_path_edit.hide()
            self.browse_button.hide()
            self.url_edit.show()
            self.download_button.show()

    #Funcion para seleccionar la imagen a convertir
    def browse_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Selecciona la Imagen", get_default_download_path(),
                                                  "Images (*.png *.xpm *.jpg *.jpeg *.gif *.webp)", options=options)
        if filename:
            self.input_path_edit.setText(filename)
            self.update_preview(filename)

    #Funcion para actualizar la previsualización de la imagen
    def update_preview(self, filename):
        pixmap = QPixmap(filename)
        pixmap = pixmap.scaled(600, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setPixmap(pixmap)

    #Funcion para guardar la imagen convertida
    def save_file(self):
        format = self.format_cb.currentText().replace('.', '')
        if not format:
            QMessageBox.warning(self, "Error", "Por favor, selecciona el formato de salida para la imagen.")
            return

        suggested_filename = self.filename_edit.text() + '.' + format
        suggested_path = os.path.join(get_default_download_path(), suggested_filename)
        # Permite al usuario elegir la ubicación y nombre para guardar la imagen después de la conversión
        filename, _ = QFileDialog.getSaveFileName(self, "Guardar Imagen como", suggested_path, f"Images (*.{format})", options=QFileDialog.Options())
        if filename:
            self.output_path = filename  # Almacenar la ruta del archivo donde se guardará la imagen después de la conversión
            QMessageBox.information(self, "Listo", "Ubicación para guardar establecida. Procede a convertir la imagen.")
            
    #Funcion para convertir la imagen
    def convert_image(self):
        if self.mode_selector.currentText() == "Convertir desde archivo":
            input_path = self.input_path_edit.text()
            if not input_path:
                QMessageBox.warning(self, "Error", "Por favor, selecciona una imagen.")
                return
            image = Image.open(input_path)
        else:
            if not hasattr(self, 'temp_image'):
                QMessageBox.warning(self, "Error", "Por favor, descarga y previsualiza una imagen primero.")
                return
            image = self.temp_image

        if not hasattr(self, 'output_path'):
            QMessageBox.warning(self, "Error", "Por favor, establece primero la ubicación para guardar la imagen.")
            return
        #Convertir la imagen al formato seleccionado y guardarla
        image.save(self.output_path)
        QMessageBox.information(self, "Éxito", "Imagen convertida y guardada con éxito en la ubicación especificada.")
        self.reset_fields()  #Limpiar campos después de la conversión y el guardado

    #Funcion para resetear los campos
    def reset_fields(self):
        self.input_path_edit.clear()
        self.output_path_edit.clear()
        self.image_label.clear()
        self.filename_edit.clear()
        self.url_edit.clear()
        self.format_cb.setCurrentIndex(0)
    
    #Funcion para mostrar la previsualización de la imagen descargada o convertida    
    def show_preview(self, image):
        # Guardar la imagen en un formato temporal para mostrar la previsualización
        buffer = io.BytesIO()
        image.save(buffer, format='PNG')
        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        pixmap = pixmap.scaled(600, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
 
    #Funcion para descargar y convertir una imagen
    def download_and_preview_image(self):
        url = self.url_edit.text()
        if not url:
            QMessageBox.warning(self, "Error", "Por favor, introduce una URL válida.")
            return

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        request = Request(url, headers=headers)

        try:
            with urlopen(request) as response:
                if response.getcode() == 200:
                    data = response.read()
                    try:
                        image = Image.open(io.BytesIO(data))
                        self.temp_image = image  # Guardar la imagen en una variable temporal para uso posterior
                        self.show_preview(image)
                    except IOError:
                        QMessageBox.warning(self, "Error", "No se pudo identificar el archivo de imagen.")
                else:
                    QMessageBox.warning(self, "Error", f"Error HTTP: {response.getcode()}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo descargar la imagen: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageConverterApp()
    ex.show()
    sys.exit(app.exec_())
