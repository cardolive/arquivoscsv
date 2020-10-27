import pytest
from arquivoscsv.app import create_app


# pytest tests/ -v (verbose)
# pytest tests/ --fixtures

@pytest.fixture(scope="module")
def app():
	"""Instance of Main flask app"""
	return create_app()

@pytest.fixture(scope="module")
def script_loc(request):
    '''Return the directory of the currently running test script'''

    # uses .join instead of .dirname so we get a LocalPath object instead of
    # a string. LocalPath.join calls normpath for us when joining the path
    return request.fspath.join('..') 

