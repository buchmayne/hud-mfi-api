from configparser import ConfigParser
from typing import List, Optional
from pydantic import BaseModel
from fastapi import Depends, FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

# database
def create_connection_obj():
    """Creates engine object from database.ini configuration"""
    filename = "database.ini"
    parser = ConfigParser()
    parser.read(filename)

    params = {k: v for k, v in parser.items("postgresql")}
    conn = create_engine(URL.create(**params))
    return conn


engine = create_connection_obj()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# models
class MFI(Base):
    __tablename__ = "mfifinal"

    state_alpha = Column(String, unique=False)
    state_code = Column(String, unique=False)
    county_code = Column(String, unique=False)
    geoid = Column(String, unique=True, primary_key=True)
    metro_area_name = Column(String, unique=False)
    county_name = Column(String, unique=False)
    mfi2021 = Column(Integer)
    mfi2020 = Column(Integer)
    mfi2019 = Column(Integer)
    mfi2018 = Column(Integer)
    mfi2017 = Column(Integer)
    mfi2016 = Column(Integer)
    mfi2015 = Column(Integer)
    mfi2014 = Column(Integer)
    mfi2013 = Column(Integer)
    mfi2012 = Column(Integer)
    mfi2011 = Column(Integer)
    mfi2010 = Column(Integer)
    mfi2009 = Column(Integer)
    mfi2008 = Column(Integer)
    mfi2007 = Column(Integer)
    mfi2006 = Column(Integer)
    mfi2005 = Column(Integer)
    mfi2004 = Column(Integer)
    mfi2003 = Column(Integer)
    mfi2002 = Column(Integer)
    mfi2001 = Column(Integer)
    mfi2000 = Column(Integer)


# crud
def get_county_by_fips_code(db: Session, geoid: str):
    return db.query(MFI).filter(MFI.geoid == geoid).all()


def get_county_by_name(db: Session, state_alpha: str, county_name: str):
    return (
        db.query(MFI)
        .filter(MFI.state_alpha == state_alpha, MFI.county_name == county_name)
        .all()
    )


def get_state_results_by_state_alpha(db: Session, state_alpha: str):
    return db.query(MFI).filter(MFI.state_alpha == state_alpha).all()


# schemas
class SchemaMFI(BaseModel):
    state_alpha: str
    geoid: Optional[str]
    county_name: Optional[str]
    state_code: str
    county_code: str
    metro_area_name: str
    mfi2021: int
    mfi2020: int
    mfi2019: int
    mfi2018: int
    mfi2017: int
    mfi2016: int
    mfi2015: int
    mfi2014: int
    mfi2013: int
    mfi2012: int
    mfi2011: int
    mfi2010: int
    mfi2009: int
    mfi2008: int
    mfi2007: int
    mfi2006: int
    mfi2005: int
    mfi2004: int
    mfi2003: int
    mfi2002: int
    mfi2001: int
    mfi2000: int

    class Config:
        orm_mode = True


# main
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "github.com/buchmayne/hud-mfi-api"}


@app.get("/state/{state_alpha}", response_model=List[SchemaMFI])
def read_mfi_data_by_state(state_alpha: str, db: Session = Depends(get_db)):
    return get_state_results_by_state_alpha(db, state_alpha=state_alpha)


@app.get("/state/{state_alpha}/county/{county_name}", response_model=List[SchemaMFI])
def read_mfi_data_by_county_name(
    state_alpha: str, county_name: str, db: Session = Depends(get_db)
):
    return get_county_by_name(db, state_alpha=state_alpha, county_name=county_name)


@app.get("/fips/{geoid}", response_model=List[SchemaMFI])
def read_mfi_data_by_fips(geoid: str, db: Session = Depends(get_db)):
    return get_county_by_fips_code(db, geoid=geoid)
