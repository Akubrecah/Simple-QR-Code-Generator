# QR Code Generator

This project generates a QR code for a given URL using Python. The generated QR code is saved as an image file.

## Features

- Generates QR codes for any URL
- Customizable QR code appearance (color, size, border)
- Saves the QR code as an image file

## Requirements

- Python 3.x
- `qrcode` module
- `Pillow` module

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
   ```
2. Navigate to the project directory:
   ```sh
   cd YOUR_REPOSITORY_NAME
   ```
3. Install the required modules:
     ```sh
    pip install qrcode[pil]
     ```
    ## Usage
        ```sh
        Open the qrcode1.py file.
        Modify the URL in the qr.add_data method to your desired URL.
        Run the script:
        ```

4. The generated QR code will be saved as qr.png in the project directory.
     ```sh
     ## Example
     Here is an example of generating a QR code for a GitHub profile:

    import qrcode as qr

    qr = qr.QRCode(
        version=1,
        error_correction=qr.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data('https://github.com/Akubrecah')
    qr.make(fit=True)

    img = qr.make_image(fill_color='blue', back_color='white')
    img.save('qr.png')
     ```

