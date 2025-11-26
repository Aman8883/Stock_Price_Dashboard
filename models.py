from sqlalchemy import Column, Integer, String ,Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer , primary_key = True, index=True)
    symbol = Column(String, unique = True,index = True)
    price = Column(Float)
    date = Column( String)

    def __repr__(self):
        return f"<Stock(symbol= {self.symbol},price = {self.price},date = {self.date})>"