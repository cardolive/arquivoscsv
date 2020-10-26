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
    

def test_existe_pasta_upload(client):
    assert client.get("/arquivoscsv/uploads").status_code == 200
