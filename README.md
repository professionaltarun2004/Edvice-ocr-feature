
# Edvice OCR Feature

## Project Overview

The **Edvice OCR Feature** is a tool designed to extract text from images using Optical Character Recognition (OCR) technology. This feature is integrated into the Edvice platform to enable seamless extraction of text from various types of documents, such as invoices, receipts, or educational materials.

### Key Features:
- **OCR Technology**: Efficiently extract text from images and scanned documents.
- **Multi-language Support**: Process text in multiple languages for diverse document types.
- **High Accuracy**: Provides high precision in text recognition for clean and distorted images.

## Technologies Used
- **OCR Engine**: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- **Programming Language**: Python
- **Libraries**: 
  - `pytesseract` for OCR processing
  - `Pillow` for image handling
  - `opencv-python` for image processing
- **Other Tools**: [Specify any other tools used, e.g., Flask for web interface]

## Installation Instructions

Follow the steps below to set up the project locally:

### Prerequisites:
- Ensure you have Python 3.x installed on your system.
- You will also need Tesseract OCR installed on your machine.

#### Step 1: Clone the repository
```bash
git clone https://github.com/professionaltarun2004/Edvice-ocr-feature.git
cd Edvice-ocr-feature
```

#### Step 2: Install Python dependencies
Ensure you have the `requirements.txt` file in your repository for easy installation:
```bash
pip install -r requirements.txt
```

#### Step 3: Install Tesseract OCR
You can install Tesseract OCR from the official repository or use a package manager for your operating system.

- **Windows**: Download the installer from [Tesseract OCR Windows Installer](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions.
- **macOS**: Use Homebrew:
  ```bash
  brew install tesseract
  ```
- **Linux (Ubuntu)**:
  ```bash
  sudo apt install tesseract-ocr
  ```

## Usage Instructions

To use the OCR feature:

1. Place your image or scanned document in the `images/` folder (or specify the path to the image).
2. Run the `ocr_script.py` to extract text:
   ```bash
   python ocr_script.py --image_path path/to/your/image.png
   ```

### Sample Command:
```bash
python ocr_script.py --image_path images/invoice.jpg
```

The extracted text will be printed to the console or saved in a text file, depending on the configuration.



