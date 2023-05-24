from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base


class Rating(Base):
    
    __tablename__ = "rating"
    

id = Column(Integer, primary_key = True)
rev_id = Column( Integer , ForeingKey = ("rev_id"))
rev_starts = Column(Integer, Foreingkey =("rev_starts"))
num_o_ratings = Column(Integer, Foreingkey =("num_o_ratings"))