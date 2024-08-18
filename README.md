
# QR Code Generator App

This project is a Python-based desktop application that allows users to generate QR codes from comma-separated words. The application was built using the Tkinter GUI framework and utilizes the `qrcode` and `Pillow` libraries to generate and display QR codes. Users can view the generated QR codes within the app and have the option to download them as PNG files.

## Features

- **Generate QR Codes:** Enter multiple words separated by commas, and the app will generate individual QR codes for each word.
- **View QR Codes:** The generated QR codes are displayed in the application for easy viewing.
- **Download QR Codes:** Users can download the generated QR codes to their local system as PNG files.

## Technologies Used

- **Python**: Core programming language used.
- **Tkinter**: GUI framework for creating the application interface.
- **qrcode**: Library for generating QR codes.
- **Pillow (PIL)**: Used for image manipulation and display.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HarithaMihimal/QR-Code-Generator-App.git
   ```

2. Install the required dependencies:

   ```bash
   pip install qrcode[pil]
   pip install pillow
   ```

3. Run the application:

   ```bash
   python QRCodeGeneratorApp.py
   ```

## Usage

1. Launch the application.
2. Enter comma-separated words into the input field.
3. Click the **Generate QR Codes** button to generate and view the QR codes within the app.
4. Optionally, click the **Download** button below each QR code to save it as a PNG file.

## Example

After generating QR codes, the app will display them within the interface, like this:

```
Enter comma-separated words:
[Generate QR Codes Button]
------------------------------------
[QR Code Image] [Download Button]
[QR Code Image] [Download Button]
```

## Future Improvements

- Add options for customizing QR code colors and sizes.
- Implement functionality to save all QR codes at once to a specified folder.
- Improve UI/UX with more modern styles and themes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
