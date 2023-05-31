from models.reviewer import Reviewer as ReviewerModel


class ReviewerService:
    def __init__(self, db):
        self.db = db

    def get_reviewer(self):
        result = self.db.query(ReviewerModel).all()
        return result

    def create_reviewer(self, reviewer: ReviewerModel):
        new_reviewe = ReviewerModel(rev_name=reviewer.rev_name.upper())
        self.db.add(new_reviewe)
        self.db.commit()
        self.db.refresh
        return

    def get_for_id(self, id: int):
        result = self.db.query(ReviewerModel).filter(ReviewerModel.id == id).first()
        return result

    def update_reviewe(self, data:ReviewerModel):
        reviewe = (
            self.db.query(ReviewerModel).filter(ReviewerModel.id == data.id).first()
        )
        reviewe.rev_name = data.rev_name
        self.db.commit()
        return

    def delete_reviewe(self, id: int):
        self.db.query(ReviewerModel).filter(ReviewerModel.id == id).delete()
        self.db.commit()
        return
