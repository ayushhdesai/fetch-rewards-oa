from fastapi import FastAPI, HTTPException 
from .models import Receipt, ReceiptResponse, PointsResponse
from .database import save_receipt, get_receipt
from .utils import calculate_points

app = FastAPI()

@app.post("/receipts/process", response_model = ReceiptResponse)
def processing_receipt(r : Receipt):
    r_id = save_receipt(r)
    return ReceiptResponse(id = r_id)

@app.get("/receipts/{id}/points", response_model = PointsResponse)
def getting_points  (id: str):
    r = get_receipt(id)
    if not r:
        raise HTTPException(status_code=404, detail="Receipt not found")
    
    points = calculate_points(r)
    return PointsResponse(points = points)