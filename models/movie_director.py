from sqlalchemy import Column, ForeignKey , Integer
 
from config.database import Base 
 
class Movie_direction(Base): 
     
    tablename = "movie_direction" 
    
    #primera data que es director
    dir_id = Column(Integer, ForeignKey("director._id")) 
    mov_id = Column(Integer, ForeignKey("movie._id") )
    #movie_id tiene que ser de la segundo data movies
    
    #new