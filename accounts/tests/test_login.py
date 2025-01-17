from rest_framework.test import APIClient
import pytest
from accounts.models import User

@pytest.mark.django_db
def test_login_with_tokens():
    client = APIClient()

    User.objects.create_user(username='JINHO', password='12341234', nickname='Mentos')

    response = client.post('/accounts/login/', {
        'username': 'JINHO',
        'password': '12341234',
    })

    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data
