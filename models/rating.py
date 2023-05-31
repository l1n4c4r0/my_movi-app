from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from models.reviewer import Reviewer


class Rating(Base):
    
    __tablename__ = "rating"
    

    id = Column(Integer,primary_key = True)
    mov_id = Column(Integer , ForeignKey("movie.id"))
    movie = relationship("Movie", back_populates = "ratings")
    rev_id = Column(Integer , ForeignKey("reviewer.id"))
    reviewer = relationship("Reviewer", back_populates = "ratings")
    rev_stars = Column(Integer)
    num_o_ratings = Column(Integer)