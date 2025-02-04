# Entry point for the API calls.

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse 
from .models import Receipt, ReceiptResponse, PointsResponse
from .database import save_receipt, get_receipt, receipt_db
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

@app.exception_handler(HTTPException)
async def validation_handler(request, exc):
    if exc.status_code == 400:
        return JSONResponse(
            status_code = exc.status_code,
            content = {"detail": "Bad Request"},
        )
    return await request.app.validation_handler(request, exc)

@app.get("/")
async def root():
    if not receipt_db:
        return {"message": "No receipts have been processed yet."}
    
    all_receipts = []
    for r_id, receipt in receipt_db.items():
        points = calculate_points(receipt)
        all_receipts.append({
            "id": r_id,
            "retailer": receipt.retailer,
            "total": receipt.total,
            "purchaseDate": receipt.purchaseDate,
            "purchaseTime": receipt.purchaseTime,
            "points": points
        })
    
    return {"message": "Welcome to Fetch Rewards API", "receipts": all_receipts}