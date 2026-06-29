from sqlalchemy.orm import sessionmaker
from models import db

def get_db_session():
    """Create db connection"""
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()