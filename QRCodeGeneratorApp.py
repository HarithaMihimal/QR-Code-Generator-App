import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk
import os

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        self.label = tk.Label(root, text="Enter comma-separated words:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate QR Codes", command=self.generate_qr_codes)
        self.generate_button.pack(pady=10)

        self.qr_frame = tk.Frame(root)
        self.qr_frame.pack(pady=10)

        self.qr_codes = []

    def generate_qr_codes(self):
        for widget in self.qr_frame.winfo_children():
            widget.destroy()

        words = self.entry.get().split(',')
        self.qr_codes = []

        for word in words:
            word = word.strip()
            if word:
                qr = qrcode.QRCode(version=1, box_size=10, border=5)
                qr.add_data(word)
                qr.make(fit=True)
                img = qr.make_image(fill='black', back_color='white')

                img_path = f"{word}.png"
                img.save(img_path)
                self.qr_codes.append(img_path)

                img = Image.open(img_path)
                img = img.resize((100, 100), Image.Resampling.LANCZOS)  # Updated line
                img = ImageTk.PhotoImage(img)

                label = tk.Label(self.qr_frame, image=img)
                label.image = img
                label.pack(side=tk.LEFT, padx=10)

                download_button = tk.Button(self.qr_frame, text="Download", command=lambda path=img_path: self.download_qr_code(path))
                download_button.pack(side=tk.LEFT, padx=10)

    def download_qr_code(self, img_path):
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            os.rename(img_path, save_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
