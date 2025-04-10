# Mutual Fund Broker Web Application

This is a backend application built with FastAPI that allows users to register, login, add mutual fund investments, and track their portfolio. It integrates with the RapidAPI Mutual Fund NAV API.

---

## Features

- User registration & login
- Add and view portfolio investments
- Fetch fund families and schemes (via RapidAPI)
- Token-based authentication
- SQLite for persistence
- Ready for hourly portfolio updates

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/your-username/mutual-fund-broker.git
cd mutual-fund-broker

## Create and Activate a Virtual Environment

python -m venv env
env\Scripts\activate 

## Install Dependencies

pip install -r requirements.txt

##  Create .env File

RAPIDAPI_KEY=your_rapidapi_key_here
## host name can also be added.

## Initialize the Database

python init_db.py

## Run the Application

uvicorn main:app --reload

## To test in browser

Use http://localhost:8000/docs for the Swagger UI.

# Running Tests

pytest
