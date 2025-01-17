from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
def test_signup():
    client = APIClient()
    response = client.post('/accounts/signup/', {
        'username': 'JINHO',
        'password': '12341234',
        'nickname': 'Mentos'
    })
    assert response.status_code == 201
    assert response.data['username'] == 'JINHO'
    assert response.data['nickname'] == 'Mentos'