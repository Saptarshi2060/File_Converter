# File Converter Web Application

This is a Flask-based web application for converting various file types such as PDFs, Word documents, images, Excel files, and data frames (JSON) to different formats. The application provides endpoints for each conversion type and serves a frontend interface for user interaction.

## Features

- **PDF to Word Conversion**: Converts PDF files to Word documents (.docx).
- **Word to PDF Conversion**: Converts Word documents (.docx) to PDF files.
- **Image to PDF Conversion**: Converts images (supports various formats) to PDF.
- **PDF to Image Conversion**: Converts the first page of a PDF file to an image (.jpg).
- **Excel to DataFrame (JSON)**: Reads an Excel file and returns its data as JSON.
- **DataFrame (JSON) to Excel**: Converts JSON data to an Excel file (.xlsx).
- **Increase File Size**: Adds 1 MB of data to any file, effectively increasing its size.
- **Decrease File Size**: Reduces the size of any file by half.

## Setup

To set up and run the application locally, follow these steps:

```bash
# Clone the repository
git clone <repository-url>
cd file-converter-app

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Usage

Open your web browser and navigate to `http://127.0.0.1:5000`.

Use the interface to choose a file and select the desired conversion or size adjustment operation.

Download the converted or adjusted file from the provided link.

## Technologies Used

- **Python**: Flask framework for backend development.
- **Libraries**: pdf2docx, docx2pdf, Pillow (PIL), pandas for file handling and conversions.
- **Frontend**: HTML, CSS, and JavaScript for the user interface.
