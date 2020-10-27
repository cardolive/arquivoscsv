# pytest tests/ -v (verbose)
# pytest tests/ --fixtures



def test_app_is_created(app):
    assert app.name == "arquivoscsv.app"


def test_config_is_loaded(config):
    assert config["DEBUG"] is False    
    

def test_config_folder_is_set(config):
    assert config["UPLOAD_FOLDER"] == "/uploads"
    

def test_request_returns_404(client):
    assert client.get("/nao_existe").status_code == 404

 
def test_pagina_inicial(client):
    assert client.get("/").status_code == 200
    

def test_pagina_upload(client):
    assert client.get("/upload").status_code == 200
    
    
def test_pagina_arquivos(client):
    assert client.get("/arquivos").status_code == 200


def test_script_loc(script_loc):
    baseline = script_loc.join('uploads/empenhos.cvs')
    print(baseline)
