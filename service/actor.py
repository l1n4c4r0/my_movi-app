from models.actor import Actor as ActorModel

class ActorService():
    def __init__(self,db):
        self.db = db


    def get_actors(self):
        result = self.db.query(ActorModel).all()
        return result
    

    def get_for_id(self,id:int):
        result = self.db.query(ActorModel).filter(ActorModel.act_id == id).first()
        return result
    
    def create_actors(self,actor:ActorModel):

        new_actor = ActorModel(
            act_fname = actor.act_fname.upper(),
            act_lname = actor.act_lname.upper(),
            act_gender = actor.act_gender.upper()
        )
        self.db.add(new_actor)
        self.db.commit()
        self.db.refresh
        return
    
    def update_actor(self, data:ActorModel):
        actor = self.db.query(ActorModel).filter(ActorModel.act_id == data.act_id).first()
        actor.act_fname = data.act_fname
        actor.act_lname = data.act_lname
        actor.act_gender = data.act_gender
        self.db.commit()
        return
    
    def delete_actor(self,id:int):
        self.db.query(ActorModel).filter(ActorModel.act_id == id).delete()
        self.db.commit()
        return