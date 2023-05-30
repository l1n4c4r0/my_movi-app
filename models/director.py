from sqlalchemy import Column, Integer, String

from config.database import Base


class Director(Base):
    
    tablename = "director"
    
id = Column( Integer, primary_Key= True)
dir_fname = Column(String)
dir_lmane = Column(String)
