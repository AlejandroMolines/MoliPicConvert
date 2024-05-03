# MoliPicConvert

**MoliPicConvert** es una aplicación simple de conversión de imágenes construida en Python utilizando Tkinter para la interfaz gráfica y Pillow para manipular las imágenes. Con **MoliPicConvert**, puedes convertir fácilmente imágenes a diferentes formatos y redimensionarlas según tus necesidades.

## Instalación

### Paso 1: Clonar el Repositorio

Clona este repositorio en tu máquina local utilizando el siguiente comando:

```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
```
### Paso 2: Instalar Requisitos
Para ejecutar **MoliPicConvert**, necesitarás tener instalado Python en tu sistema. Además, es posible que necesites instalar las dependencias utilizando **pip**. Puedes hacerlo ejecutando el siguiente comando en tu terminal:

```bash
pip install -r requirements.txt
```
```bash
tkinter
Pillow==9.0.0
pyinstaller==6.6.0
```
Para ejecutar la aplicación, simplemente ejecuta el script mpcimg.py:
```bash
python mpcimg.py
```
## Opcional: Crear Ejecutable

### Crear Ejecutable:
#### Windows:
Navega hasta la carpeta donde se encuentra el archivo principal de tu aplicación.
Ejecuta el siguiente comando para crear el ejecutable:
```bash
pyinstaller --onefile --windowed mpcimg.py
```
El ejecutable se generará en una carpeta llamada "dist" dentro de tu directorio de proyecto.

#### Linux:
En una terminal, navega hasta la carpeta donde se encuentra el archivo principal de tu aplicación.
Ejecuta el siguiente comando para crear el ejecutable:
```bash
pyinstaller --onefile --windowed mpcimg.py
```
El ejecutable se generará en una carpeta llamada "dist" dentro de tu directorio de proyecto.

## Funcionalidades

- **Seleccionar una imagen para convertirla:** Permite al usuario seleccionar una imagen desde su sistema de archivos local para ser convertida.

- **Elegir el formato de salida de la imagen:** Proporciona una variedad de formatos de imagen de salida, incluyendo JPEG, PNG, GIF y WebP.

- **Especificar el nombre del archivo de salida:** Permite al usuario especificar el nombre del archivo de salida para la imagen convertida.

- **Seleccionar la carpeta de destino:** Permite al usuario seleccionar la carpeta donde se guardarán las imágenes convertidas.

- **Redimensionar la imagen antes de guardarla (opcional):** Ofrece la opción de redimensionar la imagen antes de guardarla, permitiendo al usuario ajustar el tamaño según sus necesidades.

- **Restablecer todos los campos y la imagen mostrada con un solo clic:** Proporciona un botón de restablecimiento que limpia todos los campos y la imagen mostrada, permitiendo al usuario comenzar de nuevo fácilmente.



## Capturas de pantalla
<p align="center">
  <img src="https://github.com/AlejandroMolines/MoliPicConverter/blob/main/images/Captura%20desde%202024-05-03%2013-03-49.png?raw=true" alt="Descripción de la imagen" width="300">
</p>
<p align="center">
  Foto 1. Interfaz
</p>

<p align="center">
  <img src="https://github.com/AlejandroMolines/MoliPicConvert/blob/main/images/Captura%20desde%202024-05-03%2013-31-57.png?raw=true" alt="Descripción de la imagen" width="300">
</p>
<p align="center">
  Foto 2. Datos Introducidos
</p>

<p align="center">
  <img src="https://github.com/AlejandroMolines/MoliPicConvert/blob/main/images/Captura%20desde%202024-05-03%2013-32-37.png?raw=true" alt="Descripción de la imagen" width="300">
</p>
<p align="center">
  Foto 3. Resultado
</p>



## Contribuciones
Las contribuciones son bienvenidas. Si encuentras un <span style="color:red">error</span> o tienes alguna sugerencia para mejorar la aplicación, no dudes en abrir un problema o enviar una solicitud de extracción.



