from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class Portfolio(Base):
    __tablename__ = "portfolios"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    fund_name = Column(String)
    amount_invested = Column(Float)
    current_value = Column(Float)