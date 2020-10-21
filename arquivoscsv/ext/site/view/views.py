import csv
import os

from flask import (flash, redirect, render_template, request,
                   send_from_directory, url_for)
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {"txt", "csv"}


def init_app(app):
    """Factory de inicialização de extenções"""
    

    @app.route("/hello")
    def hello_world():
        return "Hello, World!"

    @app.route("/")
    def index():
        return render_template("index.html")

    def allowed_file(filename):
        return (
            "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        )

    @app.route("/uploader", methods=["GET", "POST"])
    def upload_file():
        if request.method == "POST":
            # check if the post request has the file part
            if "file" not in request.files:
                flash("Arquivo incompleto")
                return redirect(request.url)
            file = request.files["file"]
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == "":
                flash("Nenhum arquivo selecionado")
                return redirect(request.url)
            if file and allowed_file(file.filename):
                print("arquivo:", file.filename)
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                return redirect(url_for("uploaded_file", filename=filename))
        return render_template("upload.html")

    # salva o arquivo na pasta uploads
    @app.route("/uploads/<filename>")
    def uploaded_file(filename):
        # csv_to_dic(filename)
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

    @app.route("/mostra_arquivo", methods=["POST"])
    def arquivo_processado():
        filename = request.form["filename"]
        tipo = request.form["tipo"]
        print(filename, tipo)
        line_count = 0
        chaves = []
        linhas = []

        with open("uploads/" + filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")

            for row in csv_reader:
                if line_count == 0:
                    print("total de colunas: ", len(row))
                    print(f'Nomes das colunas: {", ".join(row)}')
                    chaves = ", ".join(row)
                else:
                    linhas.append(row)
                # print(row)
                line_count += 1

        print(f"Total de linhas processadas: {line_count}.")

        for lin in linhas:
            print(lin[:10])

        return render_template("arquivos.html", linhas=linhas)

    @app.route("/arquivos")
    def arquivos():
        lst_files = os.listdir(UPLOAD_FOLDER)
        print("lista de arquivos salvos: ", lst_files)
        # listando somente arquivos csv
        file_names = [
            fn for fn in lst_files if any(fn.endswith("csv") for ext in "csv")
        ]
        return render_template("arquivos.html", files=file_names)
