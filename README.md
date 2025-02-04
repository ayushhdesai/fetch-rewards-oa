# Receipt Processor API

A FastAPI-based web service for processing receipts and calculating reward points .

## Features
- **Submit a receipt** → `POST /receipts/process`
- **Retrieve receipt points** → `GET /receipts/{id}/points`

## Setup

### Option 1: Run with Docker (Recommended)
1. **Clone the repository**  
    ```bash
    git clone https://github.com/ayushhdesai/fetch-rewards-oa.git
    cd fetch-rewards-oa
    ```

2. **Build the Docker image**  
    ```bash
    docker build -t fastapi-receipt-processor .
    ```

3. **Run the Docker container**  
    ```bash
    docker run -d -p 8000:8000 fastapi-receipt-processor
    ```

### Option 2: Run Locally
1. **Clone the repository**  
    ```bash
    git clone https://github.com/ayushhdesai/fetch-rewards-oa.git
    cd fetch-rewards-oa
    ```

2. **Install dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**  
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

### Using Swagger UI
- Open: `http://127.0.0.1:8000/docs`
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/receipts/process' \
  -H 'Content-Type: application/json' \
  -d '{
        "retailer": "StoreX",
        "purchaseDate": "2024-02-01",
        "purchaseTime": "15:30",
        "total": "12.50",
        "items": [
            {"shortDescription": "ItemA", "price": "6.25"},
            {"shortDescription": "ItemB", "price": "6.25"}
        ]
      }'