from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class WatermarkGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Add watermark to image")
        self.window.geometry("300x100")

        self.button_load_image = tk.Button(self.window, text="Load image(s)", command=self.load_images)
        self.button_load_image.grid(column=0, row=2)

        self.button_load_watermark = tk.Button(self.window, text="Load watermark", command=self.load_watermark)
        self.button_load_watermark.grid(column=0, row=1)

        self.button_start = tk.Button(self.window, text="Start", command=self.add_watermark)
        self.button_start.grid(column=0, row=3)

        self.label_images = tk.Label(self.window, text="")
        self.label_images.grid(column=1, row=2)

        self.label_watermark = tk.Label(self.window, text="")
        self.label_watermark.grid(column=1, row=1)

        self.label_result = tk.Label(self.window, text="")
        self.label_result.grid(column=1, row=3)

        self.paths_images = []
        self.path_watermark = None

    def load_images(self):
        self.paths_images = filedialog.askopenfilenames()
        if not self.paths_images:
            self.label_images.config(text="No images selected")
        else:
            self.label_images.config(text=f"{len(self.paths_images)} images loaded successfully")

    def load_watermark(self):
        self.path_watermark = filedialog.askopenfilename()
        if os.path.splitext(self.path_watermark)[1] not in ('.jpg', '.jpeg', '.png', '.bmp'):
            messagebox.showwarning("Warning", "Invalid watermark image format")
            self.label_watermark.config(text="Invalid watermark format")
        else:
            self.label_watermark.config(text="Watermark loaded successfully")

    def add_watermark(self):
        if not self.paths_images or not self.path_watermark:
            messagebox.showwarning("Warning", "Please select both image and watermark")
            self.label_result.config(text="Please select both image and watermark")
        else:
            for path_image in self.paths_images:
                if os.path.splitext(path_image)[1] not in ('.jpg', '.jpeg', '.png', '.bmp'):
                    self.label_result.config(text=f"Invalid format: {path_image}")
                    continue
                with Image.open(path_image) as imagem:
                    draw = ImageDraw.Draw(imagem)
                    watermark_imagem = Image.open(self.path_watermark)

                    # resize watermark
                    width, height = imagem.size
                    watermark_width, watermark_height = watermark_imagem.size
                    watermark_imagem = watermark_imagem.resize((int(watermark_width * 0.2), int(watermark_height * 0.2)))

                    draw.bitmap((0, 0), watermark_imagem, fill=None)
                    filename = os.path.basename(path_image)
                    directory = os.path.dirname(path_image)
                    watermarked_filename = os.path.join(directory, f"watermarked_{filename}")
                    imagem.save(watermarked_filename)
                    self.label_result.config(text="Watermark added successfully")

if __name__ == '__main__':
    gui = WatermarkGUI()
    gui.window.mainloop()
