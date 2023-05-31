from models.movie_cast import MovieCast as MovieCastModel

class MovieCastService():
    def __init__(self,db):
        self.db = db

    def get_for_id(self,id:int):
        result = self.db.query(MovieCastModel).filter(MovieCastModel.act_id == id).first()
        return result
    
    def get_for_id(self,id:int):
        result = self.db.query(MovieCastModel).filter(MovieCastModel.mov_id == id).first()
        return result

    def create_role(self,movie_cast:MovieCastModel):
        new_role = MovieCastModel(
            role = movie_cast.role.upper()
        )
        self.db.add(new_role)
        self.db.commit()
        self.db.refresh
        return