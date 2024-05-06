# MoliPicConvert

**MoliPicConvert** is a simple image conversion application built using Python with Tkinter for the graphical interface and Pillow for image manipulation. With **MoliPicConvert**, you can easily convert images to different formats and resize them according to your needs. Compatible with Windows and Linux.

## Installation

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/AlejandroMolines/MoliPicConvert.git
```
### Step 2: Install Requirements
To run **MoliPicConvert**, you will need to have Python installed on your system. Additionally, you may need to install dependencies using pip. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```
```bash
Pillow>=10.3.0
pyinstaller==6.6.0
PyQt5==5.15.10
PyQt5_sip==12.13.0
```
In MacOS, with hombrew:

```bash
brew install tkinter pillow pyinstaller
```

To run the application, simply execute the MoliPicConverter.py script:
```bash
python src/MoliPicConverter.py
```
**OR**
```bash
cd src
python MoliPicConverter.py
```


## Optional: Create Executable
> [!CAUTION]
> The following is under maintenance.
### Windows:
Navigate to the folder where your application's main file is located.
Run the following command to create the executable:
```bash
pyinstaller --onefile --windowed MoliPicConverter.py
```
The executable will be generated in a folder named "dist" within your project directory.

### Linux:
Navigate to the folder where your application's main file is located.
Run the following command to create the executable:
```bash
pyinstaller --onefile --windowed MoliPicConverter.py
```
The executable will be generated in a folder named "dist" within your project directory.

## Features

- **Select an image to convert:** Allows the user to select an image from their local file system to be converted.

- **Choose the output image format:** Provides a variety of output image formats, including JPEG, PNG, GIF, and WebP.

- **Specify the output file name:** Allows the user to specify the name of the output file for the converted image.

- **Select the destination folder:** Allows the user to choose the folder where the converted images will be saved.

- **Resize the image before saving (optional):** Offers the option to resize the image before saving it, allowing the user to adjust the size according to their needs.

- **Reset all fields and the displayed image with a single click:** Provides a reset button that clears all fields and the displayed image, allowing the user to start over easily.


## Screenshots
<p align="center">
  <img src="https://github.com/AlejandroMolines/MoliPicConverter/blob/main/images/Captura%20desde%202024-05-03%2013-03-49.png?raw=true" alt="Descripción de la imagen" width="300">
</p>
<p align="center">
  Photo 1. Interface
</p>

<p align="center">
  <img src="https://github.com/AlejandroMolines/MoliPicConvert/blob/main/images/Captura%20desde%202024-05-03%2013-31-57.png?raw=true" alt="Descripción de la imagen" width="300">
</p>
<p align="center">
  Photo 2. Data Entered
</p>

<p align="center">
  <img src="https://github.com/AlejandroMolines/MoliPicConvert/blob/main/images/Captura%20desde%202024-05-03%2013-32-37.png?raw=true" alt="Descripción de la imagen" width="300">
</p>
<p align="center">
  Photo 3. Result
</p>



## Contributions
Contributions are welcome. If you find an <span style="color:red">error</span> or have any suggestions for improving the application, feel free to open an issue or send a pull request.

