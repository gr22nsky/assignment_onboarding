from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
def test_login_invalid_credentials():
    client = APIClient()

    response = client.post('/accounts/login/', {
        'username': 'JINHO',
        'password': '1234',
    })
    assert response.status_code == 401
    assert 'error' in response.data