# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.database import Base, engine

# # ✅ import routers correctly
# from app.routers.auth import router as auth_router
# from app.routers.portfolio import router as portfolio_router
# from app.routers.funds import router as funds_router

# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to Mutual Fund Broker API!"}

# # ✅ include routers
# app.include_router(auth_router)
# app.include_router(portfolio_router)
# app.include_router(funds_router)




from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth import router as auth_router
from app.routers.portfolio import router as portfolio_router
from app.routers.funds import router as funds_router
from app.database import Base, engine
# from app.main import app

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Mutual Fund Broker API!"}


# 👇 Make sure you include routers like this:
app.include_router(auth_router)
app.include_router(funds_router)
app.include_router(portfolio_router)
