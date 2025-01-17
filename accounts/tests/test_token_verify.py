from rest_framework.test import APIClient
import pytest
from accounts.models import User

@pytest.mark.django_db
def test_valid_token_verification():
    client = APIClient()

    user = User.objects.create_user(username='JINHO', password='12341234', nickname='Mentos')

    login_response = client.post('/accounts/login/', {
        'username': 'JINHO',
        'password': '12341234',
    })
    access_token = login_response.data['access']

    verify_response = client.post('/accounts/token/verify/', {
        'token': access_token
    })
    
    assert verify_response.status_code == 200
