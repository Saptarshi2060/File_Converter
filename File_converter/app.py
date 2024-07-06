from flask import Flask, request, send_file, jsonify, render_template
from pdf2docx import Converter
from docx2pdf import convert as docx_to_pdf
from PIL import Image
import pandas as pd
import os

app = Flask(__name__)

# Ensure uploads directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

# Increase file size (Placeholder)
@app.route('/increase-file-size', methods=['POST'])
def increase_file_size():
    file = request.files['file']
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Placeholder logic to increase file size
    with open(file_path, 'ab') as f:
        f.write(b'\0' * 1024 * 1024)  # Add 1 MB of null bytes

    return send_file(file_path, as_attachment=True)

# Decrease file size (Placeholder)
@app.route('/decrease-file-size', methods=['POST'])
def decrease_file_size():
    file = request.files['file']
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Placeholder logic to decrease file size
    new_file_path = file_path + '_decreased'
    with open(file_path, 'rb') as f:
        data = f.read()
    with open(new_file_path, 'wb') as f:
        f.write(data[:len(data)//2])  # Reduce file size by half

    return send_file(new_file_path, as_attachment=True)

# PDF to Word
@app.route('/pdf-to-word', methods=['POST'])
def pdf_to_word():
    file = request.files['file']
    pdf_path = os.path.join('uploads', file.filename)
    file.save(pdf_path)
    
    docx_path = pdf_path.replace('.pdf', '.docx')
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()
    
    return send_file(docx_path, as_attachment=True)

# Word to PDF
@app.route('/word-to-pdf', methods=['POST'])
def word_to_pdf():
    file = request.files['file']
    docx_path = os.path.join('uploads', file.filename)
    file.save(docx_path)
    
    pdf_path = docx_path.replace('.docx', '.pdf')
    docx_to_pdf(docx_path, pdf_path)
    
    return send_file(pdf_path, as_attachment=True)

# Image to PDF
@app.route('/img-to-pdf', methods=['POST'])
def img_to_pdf():
    file = request.files['file']
    img_path = os.path.join('uploads', file.filename)
    file.save(img_path)
    
    pdf_path = img_path.replace(os.path.splitext(img_path)[1], '.pdf')
    image = Image.open(img_path)
    image.convert('RGB').save(pdf_path)
    
    return send_file(pdf_path, as_attachment=True)

# PDF to Image
@app.route('/pdf-to-img', methods=['POST'])
def pdf_to_img():
    file = request.files['file']
    pdf_path = os.path.join('uploads', file.filename)
    file.save(pdf_path)
    
    # Convert first page of PDF to image
    image_path = pdf_path.replace('.pdf', '.jpg')
    image = Image.open(pdf_path)
    image.save(image_path)
    
    return send_file(image_path, as_attachment=True)

# Excel to DataFrame (JSON)
@app.route('/excel-to-df', methods=['POST'])
def excel_to_df():
    file = request.files['file']
    excel_path = os.path.join('uploads', file.filename)
    file.save(excel_path)
    
    df = pd.read_excel(excel_path)
    return jsonify(df.to_dict(orient='records'))

# DataFrame (JSON) to Excel
@app.route('/df-to-excel', methods=['POST'])
def df_to_excel():
    json_data = request.get_json()
    df = pd.DataFrame(json_data)
    
    excel_path = os.path.join('uploads', 'output.xlsx')
    df.to_excel(excel_path, index=False)
    
    return send_file(excel_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
