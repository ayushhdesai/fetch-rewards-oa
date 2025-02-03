# Test file for the live server.

import json
import requests

def test_receipt_processing():
    with open("examples/morning-receipt.json") as f:
        receipt1 = json.load(f)
    with open("examples/simple-receipt.json") as f:
        receipt2 = json.load(f)
    with open("examples/test1.json") as f:
        r1 = json.load(f)
    with open("examples/test2.json") as f:
        r2 = json.load(f)
    with open("examples/test3.json") as f:
        r3 = json.load(f)

    response = requests.post("http://127.0.0.1:8000/receipts/process", json=receipt1)
    assert response.status_code == 200
    receipt1_id = response.json()["id"]
    print(f"Uploaded receipt1 with id: {receipt1_id}")

    response = requests.get(f"http://127.0.0.1:8000/receipts/{receipt1_id}/points")
    assert response.status_code == 200
    points1 = response.json()["points"]
    print(f"Points for receipt1 (morning-receipt): {points1}")

    response = requests.post("http://127.0.0.1:8000/receipts/process", json=receipt2)
    assert response.status_code == 200
    receipt2_id = response.json()["id"]
    print(f"Uploaded receipt2 with id: {receipt2_id}")

    response = requests.get(f"http://127.0.0.1:8000/receipts/{receipt2_id}/points")
    assert response.status_code == 200
    points2 = response.json()["points"]
    print(f"Points for receipt2 (simple-receipt): {points2}")

    response = requests.post("http://127.0.0.1:8000/receipts/process", json=r1)
    assert response.status_code == 200
    receipt3_id = response.json()["id"]
    print(f"Uploaded receipt3 with id: {receipt3_id}")

    response = requests.get(f"http://127.0.0.1:8000/receipts/{receipt3_id}/points")
    assert response.status_code == 200
    points3 = response.json()["points"]
    print(f"Points for receipt3: {points3}")

    response = requests.post("http://127.0.0.1:8000/receipts/process", json=r2)
    assert response.status_code == 200
    receipt4_id = response.json()["id"]
    print(f"Uploaded receipt4 with id: {receipt4_id}")

    response = requests.get(f"http://127.0.0.1:8000/receipts/{receipt4_id}/points")
    assert response.status_code == 200
    points4 = response.json()["points"]
    print(f"Points for receipt4: {points4}")

    response = requests.post("http://127.0.0.1:8000/receipts/process", json=r3)
    assert response.status_code == 200
    receipt5_id = response.json()["id"]
    print(f"Uploaded receipt5 with id: {receipt5_id}")

    response = requests.get(f"http://127.0.0.1:8000/receipts/{receipt5_id}/points")
    assert response.status_code == 200
    points5 = response.json()["points"]
    print(f"Points for receipt5: {points5}")

if __name__ == "__main__":
    test_receipt_processing()