from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class APILog(Base):
    __tablename__ = "api_logs"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    response_time = Column(Float, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

engine = create_engine("sqlite:///monitor.db")
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)