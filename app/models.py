from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    shortDesc : str
    price : str

class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: List[Item]
    total: str

class ReceiptResponse(BaseModel):
    id: str

class PointsResponse(BaseModel):
    points: int