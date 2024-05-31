from flask import Flask, request
app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(f'D:/data_integrated_files{file.filename}')
    # Logic to open the file in VS Code
    open_in_vscode(f'D:/data_integrated_files{file.filename}')
    return 'File received and opened in VS Code!', 200


def open_in_vscode(file_path):
    import os
    os.system(f'code {file_path}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
