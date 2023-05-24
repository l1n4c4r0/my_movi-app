from sqlalchemy import Column, Integer, String

from config.database import Base


class Genres(Base):
    
    __tablename__ = "genres"
    
id = Column( Integer , primary_Key= True)
gen_title = Column(String)