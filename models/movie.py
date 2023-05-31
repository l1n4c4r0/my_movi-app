from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from config.database import Base


class Movie(Base):

    __tablename__ = "movie"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    time = Column(Float)
    ratings = relationship("Rating", back_populates = "movie")
    date_release = Column(String)
    release_contry = Column(String)
