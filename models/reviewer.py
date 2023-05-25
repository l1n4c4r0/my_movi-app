from sqlalchemy import Column, Integer, String

from config.database import Base


class Reviewer(Base):
    
    __tablename__ = "reviewer"
    
id = Column( Integer , primary_Key= True)
rev_name = Column(String)
