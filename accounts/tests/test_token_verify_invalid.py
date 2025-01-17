from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
def test_invalid_token_verification():
    client = APIClient()

    invalid_token = 'invalid_token'

    verify_response = client.post('/accounts/token/verify/', {
        'token': invalid_token
    })

    assert verify_response.status_code == 401
    assert 'detail' in verify_response.data
    assert verify_response.data['detail'] == 'Token is invalid or expired'