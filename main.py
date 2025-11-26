from fastapi import FastAPI,Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from . import models, database ,schemas
from sqlalchemy.orm import Session
import requests
import os

print(schemas.Stock)
app = FastAPI()

models.Base.metadata.create_all(bind = database.engine)

script_dir = os.path.dirname(__file__)
static_dir = os.path.join(script_dir, "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def read_root():
    return FileResponse(os.path.join(static_dir, "index.html"))

def get_db():
    db = database.SessionLocal()
    try: 
        yield db
    finally:
        db.close()


@app.get("/stock/{symbol}",response_model = schemas.Stock)
def get_stock(symbol: str,db:Session = Depends(get_db)):
    api_key = "82W90FO539C5LLIV"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}" # iss line pe kaam krna hai

    response = requests.get(url)
    data = response.json()

    print(f"API Response: {data}")

    if "Information" in data:
        raise HTTPException(status_code=429, detail="API rate limit exceeded. Please try again later.")

    if "Error Message" in data:
        raise HTTPException(status_code=404, detail=f"Invalid API call: {data['Error Message']}")

    if "Time Series (1min)" not in data:
        print(f"API Error: {data}")
        raise HTTPException(status_code=404, detail=f"Stock not found. API Response Keys: {list(data.keys())}")

    
    time_series = data["Time Series (1min)"]

    if not time_series:
        raise HTTPException(status_code=404, detail="No time series data available for this symbol")

    latest_time = list(time_series.keys())[0]
    latest_data = time_series[latest_time]
    latest_price = float(latest_data["4. close"])

    print(f"Latest data for {symbol}: {latest_time} - {latest_price}")



    stock = models.Stock(symbol=symbol, price= latest_price, date = latest_time)
    db.add(stock)
    db.commit()
    db.refresh(stock)

    return stock

@app.get("/stocks",response_model = list[schemas.Stock])
def get_all_stocks(db:Session = Depends(get_db)):
    stocks = db.query(models.Stock).all()
    return stocks