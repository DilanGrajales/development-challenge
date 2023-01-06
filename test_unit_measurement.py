import requests
import pytest

base_url = 'https://dev-challenge.up.railway.app/unit-measure'


@pytest.fixture
def created_resource_id():
    data = {
        'unit_measure': 'TP',
        'name': 'Test Resource'
    }
    response = requests.post(f'{base_url}/', json=data)
    assert response.status_code == 200
    resource_id = response.json()['id']
    return resource_id


def test_create_resource():
    data = {
        'unit_measure': 'NTP',
        'name': 'New Test Resource'
    }
    response = requests.post(f'{base_url}/', json=data)
    assert response.status_code == 200


def test_read_resource(created_resource_id):
    response = requests.get(f'{base_url}/{created_resource_id}')
    assert response.status_code == 200
    assert response.json()['name'] == 'Test Resource'


def test_update_resource(created_resource_id):
    data = {
        'unit_measure': 'UTP',
        'name': 'Updated Test Resource'
    }
    response = requests.put(f'{base_url}/{created_resource_id}', json=data)
    assert response.status_code == 200
    response = requests.get(f'{base_url}/{created_resource_id}')
    assert response.json()['name'] == 'Updated Test Resource'


def test_delete_resource(created_resource_id):
    response = requests.delete(f'{base_url}/{created_resource_id}')
    assert response.status_code == 200
    response = requests.get(f'{base_url}/{created_resource_id}')
    assert response.status_code == 404
