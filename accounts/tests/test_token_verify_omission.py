from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
def test_missing_token_verification():
    client = APIClient()

    verify_response = client.post('/accounts/token/verify/', {})

    assert verify_response.status_code == 400
    assert 'token' in verify_response.data
    assert verify_response.data['token'][0] == 'This field is required.'