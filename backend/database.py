from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL - creates a file called sql_app.db in the current directory
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Create SQLite engine. connect_args needed for SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    # Create a new database session
    db = SessionLocal()
    try:
        # Yield the session to the route that needs it
        yield db
    finally:
        # Ensure the session is closed after the request is complete
        # even if there's an error
        db.close()