import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk
import os

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f4f7")  # Light background color

        # Label styling
        self.label = tk.Label(root, text="Enter comma-separated words:", font=("Arial", 14), bg="#f0f4f7", fg="#333")
        self.label.pack(pady=10)

        # Entry widget styling
        self.entry = tk.Entry(root, width=50, font=("Arial", 12), bd=2, relief="solid")
        self.entry.pack(pady=10)

        # Generate button styling
        self.generate_button = tk.Button(root, text="Generate QR Codes", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049", bd=0, padx=10, pady=5, cursor="hand2", relief="flat", command=self.generate_qr_codes)
        self.generate_button.pack(pady=10)

        self.qr_frame = tk.Frame(root, bg="#f0f4f7")
        self.qr_frame.pack(pady=10)

        self.qr_codes = []

    def generate_qr_codes(self):
        # Clear previous QR codes
        for widget in self.qr_frame.winfo_children():
            widget.destroy()

        # Get words from entry
        words = self.entry.get().split(',')
        self.qr_codes = []

        # Create directory to save QR codes
        qr_dir = "qr_codes"
        if not os.path.exists(qr_dir):
            os.makedirs(qr_dir)

        # Generate QR codes for each word
        for word in words:
            word = word.strip()
            if word:
                qr = qrcode.QRCode(version=1, box_size=10, border=5)
                qr.add_data(word)
                qr.make(fit=True)
                img = qr.make_image(fill='black', back_color='white')

                img_path = os.path.join(qr_dir, f"{word}.png")
                img.save(img_path)
                self.qr_codes.append(img_path)

                # Load the QR code image and display it in the UI
                img = Image.open(img_path)
                img = img.resize((100, 100), Image.Resampling.LANCZOS)
                img = ImageTk.PhotoImage(img)

                qr_frame = tk.Frame(self.qr_frame, bg="#f0f4f7")
                qr_frame.pack(side=tk.LEFT, padx=10)

                # Display the QR code image
                label = tk.Label(qr_frame, image=img, bg="#f0f4f7")
                label.image = img  # Keep a reference to avoid garbage collection
                label.pack()

                # Download button styling
                download_button = tk.Button(qr_frame, text="Download", font=("Arial", 10, "bold"), bg="#007BFF", fg="white", activebackground="#0056b3", bd=0, padx=5, pady=2, cursor="hand2", relief="flat", command=lambda path=img_path: self.download_qr_code(path))
                download_button.pack(pady=5)

    def download_qr_code(self, img_path):
        # Open file dialog to save QR code
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            # Copy the file to the chosen location
            os.rename(img_path, save_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
