"""
Unit tests for first end-point
"""

import json
import pytest
from ..app import create_app


@pytest.fixture
def client():
    """
    Test fixture for api client
    :return: yields a test client
    """
    app = create_app()

    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as api_client:
            yield api_client


def test_first_status_code(client):
    """
    Test the api HTTP status code
    :param client: An app test client from the fixture
    :return: None
    """
    response = client.get('/api/v1.0/first')
    assert response.status_code == 200


def test_first_data(client):
    """
    Test the data from a call to the first end-point
    :param client: An app test client from the fixture
    :return: None
    """
    response = client.get('/api/v1.0/first')
    data = json.loads(response.text)
    assert data['name'] == 'Jane'
