from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from service import MovieDirectorService
from schemas import MovieDirector, MovieDirectorCreate


director_router = APIRouter()
movie_director_service = MovieDirectorService()

@director_router.get("/movie_directors/{movie_director_id}", response_model=MovieDirector)
def get_movie_director(movie_director_id: int, db: Session = Depends(get_db)):
    movie_director = movie_director_service.get_movie_director(db, movie_director_id)
    if movie_director:
        return movie_director
    else:
        raise HTTPException(status_code=404, detail="MovieDirector not found")

@director_router.post("/movie_directors", response_model=MovieDirector)
def create_movie_director(movie_director: MovieDirectorCreate, db: Session = Depends(get_db)):
    created_movie_director = movie_director_service.create_movie_director(db, movie_director)
    return created_movie_director
