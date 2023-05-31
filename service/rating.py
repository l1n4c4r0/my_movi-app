from models.rating import Rating as RatingModel

class RatingService():
    def __init__(self, db):
        self.db = db
        
    def get_rating(self):
        result = self.db.query(RatingModel).all()
        return result
    
    def create_rating(self, rating : RatingModel):
        new_rating = RatingModel(
            mov_id = rating.mov_id,
            rev_id = rating.rev_id,
            rev_stars = rating.rev_stars,
            num_o_ratings = rating.num_o_ratings
        )
        self.db.add(new_rating)
        self.db.commit()
        self.db.refresh
        return
    
    def get_for_id(self, id : int):
        result = self.db.query(RatingModel).filter(RatingModel.id ==id).first()
        return result
    
    def update_rating(self,data:RatingModel):
        rating = self.db.query(RatingModel).filter(RatingModel.id == data.id).first()
        rating.movie_id = data.movie_id
        self.db.commit()
        return
    
    def delete_genre(self,id:int):
        self.db.query(RatingModel).filter(RatingModel.id == id).delete()
        self.db.commit()
        return