import tkinter as tk
import qrcode
from PIL import Image, ImageTk

class QRCodeApp:
    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.entry.get())
        qr.make(fit=True)

        # Create a Pillow (PIL) image from the QR code
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Convert the Pillow image to a PhotoImage for Tkinter
        self.qr_image = ImageTk.PhotoImage(qr_image)

        # Display the QR code image in the Label
        self.label1.config(image=self.qr_image)
        self.label1.image = self.qr_image

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QR Code Generator")

        self.label = tk.Label(self.root, text="Enter text to generate QR code:", font=("arial", 20))
        self.label.pack()

        self.entry = tk.Entry(self.root, font=("arial", 15))
        self.entry.pack()

        self.button = tk.Button(self.root, text="Generate QR Code", font=("arial", 15), command=self.generate_qr_code)
        self.button.pack()

        self.label1 = tk.Label(self.root, image="")
        self.label1.pack()

        self.root.mainloop()

QRCodeApp()
