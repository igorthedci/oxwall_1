import pytest
from oxwall_site import Oxwall


@pytest.fixture()
def app():
    app = Oxwall()
    yield app
    app.close()


@pytest.fixture()
def login_user(app):
    app.login('admin', 'pass')
    yield
    app.logout('admin')

@pytest.fixture()
def admin_user_old(app):
    return {'username': 'admin', 'password': 'Adm1n'}

@pytest.fixture
def admin_user():
    return User(username='admin', password='Adm1n')


