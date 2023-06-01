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

    def update_actors_for_id(self, data:MovieCastModel):
        actor = self.db.query(MovieCastModel).filter(MovieCastModel.act_id == data.act_id).first()
        self.db.commit()
        return

    def update_movies_for_id(self, data:MovieCastModel):
        movie = self.db.query(MovieCastModel).filter(MovieCastModel.mov_id == data.mov_id).first()
        self.db.commit()
        return

    def delete_actors_for_id(self,id:int):
        self.db.query(MovieCastModel).filter(MovieCastModel.act_id == id).delete()
        self.db.commit()
        return

    def delete_movies_for_id(self,id:int):
        self.db.query(MovieCastModel).filter(MovieCastModel.mov_id == id).delete()
        self.db.commit()
        return