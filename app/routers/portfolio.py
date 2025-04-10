from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.portfolio import Portfolio
# from app.auth.schemas import PortfolioBase, PortfolioOut
from app.schemas import PortfolioBase, PortfolioOut

router = APIRouter(prefix="/portfolio", tags=["Portfolio"])

@router.post("/add")
def add_investment(investment: PortfolioBase, db: Session = Depends(get_db)):
    new_entry = Portfolio(**investment.dict(), current_value=investment.amount_invested, user_id=1)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@router.get("/")
def view_portfolio(db: Session = Depends(get_db)):
    return db.query(Portfolio).filter(Portfolio.user_id == 1).all()
