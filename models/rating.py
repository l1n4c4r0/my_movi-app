from sqlalchemy import Column, Integer, ForeignKey

from config.database import Base


class Rating(Base):
    
    __tablename__ = "rating"
    

    id = Column(Integer,primary_key = True)
    mov_id = Column(Integer , ForeignKey("movie.id"))
    rev_id = Column(Integer , ForeignKey("reviewer.id"))
    rev_starts = Column(Integer)
    num_o_ratings = Column(Integer) 