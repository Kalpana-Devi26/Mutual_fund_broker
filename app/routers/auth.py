from app.auth import router 
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/auth", tags=["Authentication"])