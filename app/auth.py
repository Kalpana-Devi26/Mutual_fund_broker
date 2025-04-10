from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from app.database import get_db
from app.models import user
from app.auth.schemas import UserCreate, UserLogin, Token

SECRET_KEY = "secretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix="/auth", tags=["Authentication"])

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/register", response_model=Token)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(user.User).filter(user.User.email == user_data.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_pw = pwd_context.hash(user_data.password)
    new_user = user.User(email=user_data.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    access_token = create_access_token(data={"sub": new_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(user.User).filter(user.User.email == user_data.email).first()
    if not db_user or not pwd_context.verify(user_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}