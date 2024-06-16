from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate():
    response = client.post("/calculate", json={"expression": "3 4 +"})
    assert response.status_code == 200
    assert response.json() == {"expression": "3 4 +", "result": 7.0}

def test_get_operations():
    response = client.get("/operations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_operations_csv():
    response = client.get("/operations/csv")
    assert response.status_code == 200
    assert response.headers['content-type'] == 'text/csv'