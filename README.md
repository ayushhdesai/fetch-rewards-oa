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
    ```

    ```bash
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

4. **Check the running Docker container**  
    ```bash
    docker ps
    ```
    - Make sure port is not already allocated.

#### The server is now live and ready to be tested - 
- Open: `http://127.0.0.1:8000/`

### Option 2: Run Locally (Using Python)
1. **Clone the repository**  
    ```bash
    git clone https://github.com/ayushhdesai/fetch-rewards-oa.git
    ```

    ```bash
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

#### The server is now live - 
- Open: `http://127.0.0.1:8000/`

4. **Testing the manually written test cases on a new terminal**  
    ```bash
    python test_receipt_processor.py
    ```