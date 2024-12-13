from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

p_db_name = "postgres"
p_user = "postgres"
p_pass = ""
port = '5433'

SQLALCHEMY_DATABASE_URL = f"postgresql://{p_user}:{p_pass}@localhost:{port}/{p_db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        ("Database connection successful!!!!")
        yield db
    finally:
        db.close()
