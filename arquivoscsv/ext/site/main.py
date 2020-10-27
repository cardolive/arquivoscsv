from flask import request, render_template, flash, redirect
from werkzeug.utils import secure_filename
from flask import Blueprint
import csv
import os


bp = Blueprint("site", __name__)
ALLOWED_EXTENSIONS = {"csv"}

FILE_DIR = "files_upload"


@bp.route("/")
def index():
    return render_template("index.html")


def allowed_file(filename):
    """[list of allowed extensions of file]

    Args:
        filename ([type]): [str]

    Returns:
        [type]: [list]
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Carrega Arquivo
@bp.route("/carrega", methods=["GET", "POST"])
def upload_file():
    """receive file from form and save it

    Returns:
        [type]: [renderiza a pagina com o arquivo salvo]
    """
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
            filename = secure_filename(file.filename).lower()
            file.save(os.path.join(FILE_DIR, filename))
            # return redirect(url_for("uploaded_file", filename=filename))
    return render_template("upload.html")


@bp.route("/uploads/<filename>")
def show_file_by_name(filename):
    """[upload a file by name ]

    Args:
        filename ([type]): [str]

    Returns:
        [type]: [file]
    """
    # csv_to_dic(filename)
    return send_from_directory(FILE_DIR, filename)


@bp.route("/mostra_arquivo", methods=["POST"])
def open_file_lines():
    """open a file by name and send all lines, except the header (frist line)

    Returns:
        [type]: [list]
    """
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


# Lista arquivos carregados
@bp.route("/arquivos")
def files_list():
    """list all files .csv into the paste /uploads

    Returns:
        [type]: [description]
    """
    lst_files = os.listdir(FILE_DIR)
    print("lista de arquivos salvos: ", lst_files)
    # listando somente arquivos csv
    file_names = [fn for fn in lst_files if any(fn.endswith("csv") for ext in "csv")]
    return render_template("arquivos.html", files=file_names)
