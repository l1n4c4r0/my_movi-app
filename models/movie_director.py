from sqlalchemy import Column, ForeignKey , Integer
 
from config import Base 
 
class Movie_direction(Base): 
     
    tablename = "movie_direction" 
    
    #primera data que es director
    id = Column(Integer, ForeignKey("director._id")) 
    mov_id = Column(Integer, ForeignKey("mov._id") )
    #movie_id tiene que ser de la segundo data movies