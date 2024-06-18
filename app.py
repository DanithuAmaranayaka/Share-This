from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads'

@app.route('/')
def index():
    # List files in the uploads directory
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # You can add logic here to save file details to a database if needed
            return redirect(url_for('index'))
    return render_template('upload.html')

@app.route('/view/<filename>')
def view(filename):
    return render_template('view.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
