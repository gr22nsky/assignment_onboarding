from rest_framework.test import APIClient
import pytest
from accounts.models import User

@pytest.mark.django_db
def test_valid_refresh_token():
    client = APIClient()

    user = User.objects.create_user(username='JINHO', password='12341234', nickname='Mentos')
    login_response = client.post('/accounts/login/', {
        'username': 'JINHO',
        'password': '12341234',
    })
    refresh_token = login_response.data.get('refresh')

    response = client.post('/accounts/token/refresh/', {
        'refresh': refresh_token
    })

    assert response.status_code == 200
    assert 'access' in response.data
