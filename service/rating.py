from models.rating import Rating as RatingModel

class RatingService():
    def __init__(self, db):
        self.db = db
        
    def get_rating(self):
        result = self.db.query(RatingModel).all()
        return result
    
    def create_rating(self, rating : RatingModel):
        new_rating = RatingModel(
            movie_id = rating.mov_id
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
        rating.rating_title = data.rating_title
        
    