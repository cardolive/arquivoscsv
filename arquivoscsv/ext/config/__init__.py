
def init_app(app):
    app.config["SECRET_KEY"] = "atfpoli2020"
    app.config["UPLOAD_FOLDER"] = "/uploads"
    
    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
    
