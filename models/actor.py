from sqlalchemy import Column, Integer, String

from config.database import Base

class Actor():

    __tablename__ = "actor"

    act_id = Column(Integer, primary_key = True )
    act_fname = Column(String(20))
    act_lname = Column(String(20))
    act_gender = Column(String(1))