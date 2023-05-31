from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base


class Rating(Base):
    
    __tablename__ = "rating"
    

id = Column(Integer, primary_key = True)
mov_id = Column( Integer , ForeingKey = ("mov_id"))
rev_id = Column( Integer , ForeingKey = ("rev_id"))
rev_stars = Column(Integer)
num_o_ratings = Column(Integer)