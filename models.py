from sqlalchemy import create_engine, Column, Integer, String, Float, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import JSONB
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()
engine = create_engine(os.getenv('DATABASE_URL'))
Session = sessionmaker(bind=engine)


class School(Base):
    __tablename__ = 'schools'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    specialty = Column(String(200), nullable=False)
    contact = Column(String(200))
    address = Column(String(500))
    description = Column(Text)
    image = Column(String(500))  
    technical_sheet_url = Column(String(500))  

    def dto_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'specialty': self.specialty,
            'contact': self.contact,
            'address': self.address,
            'description': self.description,
            'image': self.image,
            'technicalSheetUrl': self.technical_sheet_url
        }

# Création des tables
def init_db():
    Base.metadata.create_all(engine) 