from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    # Save the uploaded file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Redirect to the index page with the filename
    return redirect(url_for('index', filename=file.filename))

@app.route('/cursor/<filename>')
def cursor(filename):
    return f"Cursor image: {filename}"

if __name__ == '__main__':
    app.run(debug=True)

