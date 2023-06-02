from fastapi import HTTPException
from models.movie_director import Movie_direction as Movie_directorModel



class MovieDirectorService :
    def __init__(self, db) -> None : 
        self.db = db

    def get_Movie_director(self):
        result = self.db.query(Movie_directorModel).all()
        return result
        
    def get_for_id(self,id:int):
        result = self.db.query(Movie_directorModel).filter(Movie_directorModel.id == id).first()
        return result    
        
    def create_movie_director(self,movie_director: Movie_directorModel):
        new_movie_directior = Movie_directorModel(
        dir_id = movie_director.dir_id(),
        mov_id = movie_director.mov_id()     
        )
        self.db.add(new_movie_directior)
        self.db.commit()
        self.db.refresh
        return

    def update_movie_director(self,data: Movie_directorModel):
        movie_director = self.db.query(Movie_directorModel).filter(Movie_directorModel.id ==data.id).first()
        movie_director.dir_id = data.dir_id
        movie_director.mov_id = data.mov_id
        self.db.commit()
        return
    
    
    def delete_movie_director(self,id:int):
        self.db.query(Movie_directorModel).filter(Movie_directorModel.id == id).delete()
        self.db.commit()
        return

    

#new