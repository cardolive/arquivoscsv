import csv
import os
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/hello')
def hello_world():
	return 'Hello, World!'


# no pronpt do windows:
# set FLASK_APP=main.py (On Windows you need to use set instead of export)
# set FLASK_ENV=development
# flask run
#  resposta:
# * Serving Flask app "main.py" (lazy loading)
# * Environment: development
# * Debug mode: on
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 664-881-666
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

@app.route('/')
def index():
	return render_template('index.html')


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			flash('No selected file')
			print("sem arquivo")
			return redirect(request.url)
		if file and allowed_file(file.filename):
			print("arquivo:", file.filename)
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('uploaded_file', filename=filename))
	return render_template('upload.html')


# salva o arquivo na pasta uploads
@app.route('/uploads/<filename>')
def uploaded_file(filename):
	# csv_to_dic(filename)
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/mostra_arquivo', methods=['POST'])
def arquivo_processado():

	filename = request.form['filename']
	tipo = request.form['tipo']
	print(filename, tipo)
	line_count = 0
	chaves = []
	linhas = []

	with open("uploads/" + filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=';')

		for row in csv_reader:
			if line_count == 0:
				print("total de colunas: ", len(row))
				print(f'Nomes das colunas: {", ".join(row)}')
				chaves = ", ".join(row)
			else:
				linhas.append(row)
			# print(row)
			line_count += 1

	print(f'Total de linhas processadas: {line_count}.')

	for lin in linhas:
		print(lin[:10])

	return render_template('arquivos.html', linhas=linhas)


@app.route('/arquivos')
def arquivos():
	lst_files = os.listdir(UPLOAD_FOLDER)
	print(lst_files)
	return render_template('arquivos.html', files=lst_files)
