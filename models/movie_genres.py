from sqlalchemy import Column, Foreingkey, Integer 

from config.database import Base

class MovieGenres(Base):
    
    __tablename__ = "movie_genres"
    
    
    id = Column(Integer, primary_key = True)
    gen_id = Column(Integer, Foreingkey("genres.id"))
    movie_id = Column(Integer, Foreingkey("movie.id") )