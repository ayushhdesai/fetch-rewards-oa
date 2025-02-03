from typing import Dict
from uuid import uuid4
from .models import Receipt

receipt_db: Dict[str, Receipt] = {}

def save_receipt(receipt: Receipt) -> str:
    receipt_id = str(uuid4())
    receipt_db[receipt_id] = receipt
    return receipt_id

def get_receipt(receipt_id: str) -> Receipt:
    return receipt_db.get(receipt_id)