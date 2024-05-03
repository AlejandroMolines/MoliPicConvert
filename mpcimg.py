import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageConverterApp:
    def __init__(self, master):
        self.master = master
        self.filepath = None
        self.output_folder_path = None
        self.preview_image = None
        self.master.title("MoliPicConvert")
        self.master.geometry("400x450")
        self.master.configure(bg="#f0f5f5")

        self.label1 = tk.Label(self.master, text="Selecciona la imagen a convertir:", bg="#f0f5f5")
        self.label1.pack()

        self.select_button = tk.Button(self.master, text="Seleccionar Imagen", command=self.select_image, bg="#89b0ae", fg="white")
        self.select_button.pack()

        self.selected_image_label = tk.Label(self.master, text="", bg="#f0f5f5")
        self.selected_image_label.pack()

        self.label2 = tk.Label(self.master, text="Selecciona el formato de salida:", bg="#f0f5f5")
        self.label2.pack()

        self.extension_var = tk.StringVar()
        self.extension_var.set(".jpg")

        self.extension_options = [".jpg", ".png", ".gif", ".webp"]
        self.extension_menu = tk.OptionMenu(self.master, self.extension_var, *self.extension_options)
        self.extension_menu.configure(bg="#f0f5f5", fg="#333333")
        self.extension_menu.pack()

        self.label3 = tk.Label(self.master, text="Nombre del archivo de salida:", bg="#f0f5f5")
        self.label3.pack()

        self.filename_entry = tk.Entry(self.master)
        self.filename_entry.pack()

        self.label4 = tk.Label(self.master, text="Selecciona la carpeta de destino:", bg="#f0f5f5")
        self.label4.pack()

        self.output_folder_button = tk.Button(self.master, text="Seleccionar Carpeta", command=self.select_output_folder, bg="#89b0ae", fg="white")
        self.output_folder_button.pack()

        self.selected_output_folder_label = tk.Label(self.master, text="", bg="#f0f5f5")
        self.selected_output_folder_label.pack()

        self.label5 = tk.Label(self.master, text="Redimensionar imagen (Ancho x Alto):", bg="#f0f5f5")
        self.label5.pack()

        self.width_entry = tk.Entry(self.master)
        self.width_entry.pack()

        self.height_entry = tk.Entry(self.master)
        self.height_entry.pack()

        self.convert_button = tk.Button(self.master, text="Convertir", command=self.convert_image, bg="#89b0ae", fg="white")
        self.convert_button.pack()

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_fields, bg="#89b0ae", fg="white")
        self.reset_button.pack()

    def select_image(self):
        self.filepath = filedialog.askopenfilename()
        if self.filepath:
            image_name = os.path.basename(self.filepath)
            image_directory = os.path.dirname(self.filepath)
            self.selected_image_label.config(text=f"Nombre de la imagen: {image_name}\nDirectorio: {image_directory}")
            self.show_preview()

    def select_output_folder(self):
        self.output_folder_path = filedialog.askdirectory(initialdir="~/Downloads", title="Seleccionar Carpeta de Destino")
        if self.output_folder_path:
            self.selected_output_folder_label.config(text=f"Carpeta de destino seleccionada: {self.output_folder_path}")

    def convert_image(self):
        if not self.filepath or not self.output_folder_path:
            messagebox.showerror("Error", "Por favor, selecciona una imagen y una carpeta de destino primero.")
            return

        output_extension = self.extension_var.get()
        output_filename = self.filename_entry.get() + output_extension
        output_filepath = os.path.join(self.output_folder_path, output_filename)

        image = Image.open(self.filepath)
        width = self.width_entry.get()
        height = self.height_entry.get()

        if width and height:
            if not width.isdigit() or not height.isdigit():
                messagebox.showerror("Error", "Las dimensiones deben ser números enteros.")
                return
            image = image.resize((int(width), int(height)))

        try:
            image.save(output_filepath)
            messagebox.showinfo("Éxito", "La imagen se ha convertido correctamente y se ha guardado en la carpeta de destino.")
        except FileExistsError:
            messagebox.showerror("Error", f"Ya existe un archivo con el nombre '{output_filename}' en la carpeta de destino.")

    def show_preview(self):
        image = Image.open(self.filepath)
        image.thumbnail((100, 100))
        photo = ImageTk.PhotoImage(image)
        if self.preview_image:
            self.preview_image.configure(image=photo)
            self.preview_image.image = photo
        else:
            self.preview_image = tk.Label(self.master, image=photo)
            self.preview_image.image = photo
            self.preview_image.pack(before=self.label2)

    def reset_fields(self):
        self.filename_entry.delete(0, tk.END)
        self.width_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.extension_var.set(".jpg")
        if self.preview_image:
            self.preview_image.pack_forget()
            self.preview_image = None
        self.selected_image_label.config(text="")
        self.selected_output_folder_label.config(text="")

def main():
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
