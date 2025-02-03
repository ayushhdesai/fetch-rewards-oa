from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse 
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

@app.exception_handler(HTTPException)
async def validation_handler(request, exc):
    if exc.status_code == 400:
        return JSONResponse(
            status_code = exc.status_code,
            content = {"detail": "Bad Request"},
        )
    return await request.app.validation_handler(request, exc)