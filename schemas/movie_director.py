from pydantic import BaseModel

class MovieDirectorBase(BaseModel):
    movie_id: int
    director_id: int

class MovieDirectorCreate(MovieDirectorBase):
    pass

class MovieDirector(MovieDirectorBase):
    id: int

    class Config:
        orm_mode = True


#new