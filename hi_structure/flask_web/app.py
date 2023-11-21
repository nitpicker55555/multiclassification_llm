from flask import Flask, render_template, request, send_from_directory
import os
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # 设置文件上传的目标文件夹

# 确保上传文件夹存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # 检查是否有文件在请求中
        if 'file' not in request.files:
            return 'no file'
        file = request.files['file']
        if file.filename == '':
            return 'no file'
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return render_template('display_image.html')
    return '''
    <!doctype html>
    <title>upload xlsx</title>
    <h1>upload xlsx and analyse column "Overview"</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name="file">
      <input type=submit value="upload">
    </form>
    '''

@app.route('/display')
def display_image():
    time.sleep(36)  # 延迟五秒
    return '''
    <img src="/uploads/sa.png" alt="Image" />
    <br>
    <a href="/uploads/saa.jsonl" download>download labels.jsonl</a>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
