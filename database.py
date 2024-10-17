from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db_url = "mysql://root:Arhaanjamal@127.0.0.1:3306/fastapidemo"

engine = create_engine(db_url)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False,bind=engine)