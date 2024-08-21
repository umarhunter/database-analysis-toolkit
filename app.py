import time
import os
import redis
import secrets
from flask import Flask, request, jsonify, flash, redirect, url_for, send_from_directory, Request

from werkzeug.utils import secure_filename
from database_analysis import main as run_analysis # main function from database_analysis.py


app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data') # Use absolute path to avoid issues with relative paths
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'json', 'parquet', 'feather'} # Add more file types as needed

# Set the secret key to a random value
app.secret_key = secrets.token_hex(16)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
#cache = redis.Redis(host='redis', port=6379)
cache = redis.Redis(host='localhost', port=6379)
@app.route('/', methods=['GET', 'POST'])
def home():
    count = get_hit_count()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect(request.url)
    return f'''
    <!doctype html>
    <title>Upload new File</title>
    <h1>This web page has been viewed {count} times.</h1>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/run-analysis', methods=['POST'])
def run_analysis_route():
    config_file = request.json.get('config_file', 'config/config.yaml')
    input_file = request.json.get('input_file')
    output_file = request.json.get('output_file')

    args = ['--config', config_file]

    if input_file:
        args.extend(['--input_file', input_file])
    if output_file:
        args.extend(['--output_file', output_file])

    # Run the analysis using the provided arguments
    run_analysis(args)

    return jsonify({"status": "Analysis completed successfully"})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

app.add_url_rule(
    "/uploads/<name>", endpoint="download_file", build_only=True
)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)