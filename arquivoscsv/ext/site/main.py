from flask import request, render_template, flash, redirect
from werkzeug.utils import secure_filename
from flask import Blueprint
import csv
import os

bp = Blueprint("site", __name__)
ALLOWED_EXTENSIONS = {"csv"}

@bp.route("/")
def index():
    return render_template("index.html")


def allowed_file(filename):
        return (
            "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        )

@bp.route("/uploader", methods=["GET", "POST"])
def upload_file():
    """[summary]

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
            filename = secure_filename(file.filename)
            file.save(os.path.join(bp.config["UPLOAD_FOLDER"], filename))
            # return redirect(url_for("uploaded_file", filename=filename))
    return render_template("upload.html")