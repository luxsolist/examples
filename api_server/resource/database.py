from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+mysqldb://test:test@127.0.0.1:3306/example"
args = {
    "pool_size": 1,
    "max_overflow": 3,
    "pool_recycle": 120
}

engine = create_engine(DATABASE_URL, connect_args={"connect_timeout": 5}, **args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
