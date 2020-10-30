
def init_app(app):
    app.config["SECRET_KEY"] = "atfpoli2020"
    app.config["UPLOAD_FOLDER"] = "arquivoscsv\\files_upload"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///atf.sqlite3'
    
    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True
    
