import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QLineEdit, QFileDialog, QMessageBox, QFrame)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pathlib import Path
from PIL import Image
import os

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

        layout = QVBoxLayout()

        #Entrada de la imagen a convertir
        self.input_path_edit = QLineEdit()
        self.input_path_edit.setReadOnly(True)
        self.input_path_edit.setStyleSheet("height: 30px; padding: 5px; border-radius: 5px; background: #f0f0ff; color: #000;")  # Light blue background with black text
        self.label1 = QLabel("Selecciona la imagen a convertir:")
        browse_button = QPushButton("Buscar...")
        browse_button.clicked.connect(self.browse_file)
        browse_button.setStyleSheet("background-color: #a0a0ff; color: #000; border-radius: 5px; padding: 5px;")  # Slightly darker blue
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.label1)
        top_layout.addWidget(self.input_path_edit)
        top_layout.addWidget(browse_button)
        layout.addLayout(top_layout)

        #Previsualización de la imagen
        self.image_label = QLabel()
        self.image_label.setFrameStyle(QFrame.StyledPanel)
        layout.addWidget(self.image_label)

        #Salida de la imagen convertida
        self.output_path_edit = QLineEdit()
        self.output_path_edit.setReadOnly(True)
        self.output_path_edit.setStyleSheet("height: 30px; padding: 5px; border-radius: 5px; background: #f0f0ff; color: #000;")
        self.format_cb = QComboBox()
        self.format_cb.addItems([".jpg", ".png", ".gif", ".webp"])
        self.format_cb.setStyleSheet("background: #f0f0ff; color: #000;")
        save_button = QPushButton("Guardar como...")
        save_button.clicked.connect(self.save_file)
        save_button.setStyleSheet("background-color: #a0a0ff; color: #000; border-radius: 5px; padding: 5px;")
        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_path_edit)
        output_layout.addWidget(self.format_cb)
        output_layout.addWidget(save_button)
        layout.addLayout(output_layout)
        
        #Nombre del archivo de salida
        self.filename_edit = QLineEdit()
        self.filename_edit.setPlaceholderText("Enter file name here")
        self.filename_edit.setStyleSheet("height: 30px; padding: 5px; border-radius: 5px; background: #f0f0ff; color: #000;")
        
        #Añadir el nombre del archivo de salida al layout
        output_layout.insertWidget(1, self.filename_edit)

        #Botones de conversión y reseteo
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

        self.setLayout(layout)

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
        options = QFileDialog.Options()
        suggested_filename = self.filename_edit.text() + self.format_cb.currentText()
        suggested_path = os.path.join(get_default_download_path(), suggested_filename)
        filename, _ = QFileDialog.getSaveFileName(self, "Guardar Imagen como", suggested_path,
                                                "Images (*.png *.xpm *.jpg *.jpeg *.gif *.webp)", options=options)
        if filename:
            self.output_path_edit.setText(filename)

    #Funcion para convertir la imagen
    def convert_image(self):
        input_path = self.input_path_edit.text()
        output_path = self.output_path_edit.text()
        if not input_path or not output_path:
            QMessageBox.warning(self, "Error", "Por favor, selecciona la imagen de entrada y la de salida.")
            return

        image = Image.open(input_path)
        image.save(output_path)
        QMessageBox.information(self, "Exito", "Imagen convertida con éxito.")
        
    #Funcion para resetear los campos
    def reset_fields(self):
        self.input_path_edit.clear()
        self.output_path_edit.clear()
        self.image_label.clear()
        self.filename_edit.clear()
        self.format_cb.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageConverterApp()
    ex.show()
    sys.exit(app.exec_())
