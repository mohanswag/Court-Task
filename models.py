from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class CaseLog(Base):
    __tablename__ = 'case_logs'
    id = Column(Integer, primary_key=True)
    case_type = Column(String)
    case_number = Column(String)
    filing_year = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    raw_response = Column(String)

engine = create_engine('sqlite:///cases.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def log_case_query(case_type, case_number, filing_year, raw_response):
    session = Session()
    entry = CaseLog(
        case_type=case_type,
        case_number=case_number,
        filing_year=filing_year,
        raw_response=raw_response
    )
    session.add(entry)
    session.commit()
    session.close()
