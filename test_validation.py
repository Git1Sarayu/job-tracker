from app import app

def test_add_without_company():
    client = app.test_client()
    response = client.post("/applications", json={"role": "Engineer"})
    assert response.status_code == 400

def test_add_without_role():
    client = app.test_client()
    response = client.post("/applications", json={"company": "TCS"})
    assert response.status_code == 400
    
def test_update_without_status():
    client = app.test_client()
    response = client.put("/applications/1", json={})
    assert response.status_code == 400