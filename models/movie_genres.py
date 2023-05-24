from sqlalchemy import Column, Foreingkey, Integer

from config.database import Base


class MovieGenres(Base):
    
    __tablename__ = "movie_genres"
    
    id = Column(Integer, Foreingkey("genres._id"))
    mov_id = Column(Integer, Foreingkey("movie.mov_id") )