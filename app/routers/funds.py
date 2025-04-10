from fastapi import APIRouter, HTTPException
import httpx
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter(prefix="/funds", tags=["Funds"])

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")  # Set this in your environment
RAPIDAPI_HOST = "mutual-fund-nav.p.rapidapi.com"  # Example host
BASE_URL = f"https://{RAPIDAPI_HOST}"

headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST
}

@router.get("/")
async def list_fund_houses():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/mf_list", headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch fund houses")
        return response.json()

@router.get("/{fund_house}/schemes")
async def list_schemes(fund_house: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/schemes?house={fund_house}", headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch schemes")
        return response.json()

# from fastapi import APIRouter


# router = APIRouter(prefix="/funds", tags=["Funds"])

# @router.get("/")
# def list_fund_houses():
#     return ["Fund House A", "Fund House B"]  # Placeholder

# @router.get("/{fund_house}/schemes")
# def list_schemes(fund_house: str):
#     return ["Scheme X", "Scheme Y"]  # Placeholder