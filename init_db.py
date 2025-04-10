# init_db.py

from app.database import Base, engine
from app.models import user, portfolio

def initialize_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Database initialized.")

if __name__ == "__main__":
    initialize_db()
