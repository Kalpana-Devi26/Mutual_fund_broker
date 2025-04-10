from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class PortfolioBase(BaseModel):
    fund_name: str
    amount_invested: float

class PortfolioOut(PortfolioBase):
    current_value: float