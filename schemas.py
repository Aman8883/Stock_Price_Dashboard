from pydantic import BaseModel

class StockBase(BaseModel):
    
    symbol : str
    price : float
    date : str

class StockCreate(StockBase):
    pass

class Stock(StockBase):
    id :int

    class Config:
        from_attributes = True