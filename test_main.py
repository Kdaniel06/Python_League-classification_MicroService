from fastapi.testclient import TestClient
from testing_jsons import *
from main import app

client = TestClient(app)

# * Test the all teams sorted together
def test_positions():
    response = client.post("/positions/", json=testingTeams)
    
    # ? Verify code 200
    assert response.status_code == 200
    
    # ? Get the respond data
    response_data = response.json()
    
    # ? Verify matches
    assert response_data == sorted_all_together

# * Test the teams sorted grouped by zone
def test_positions_by_zone():
    response = client.post("/positions_by_zone/", json=testingTeams)
    
    # ? Verify code 200
    assert response.status_code == 200
    
    # ? Get the respond data
    response_data = response.json()
    
    # ? Verify matches
    assert response_data == sorted_by_zone