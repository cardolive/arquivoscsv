import pytest
from arquivoscsv.app import create_app


# pytest tests/ -v (verbose)
# pytest tests/ --fixtures

@pytest.fixture(scope="module")
def app():
	"""Instance of Main flask app"""
	return create_app()

