from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session
from service.movie_director import MovieDirectorService
from schemas.movie_director import MovieDirector, MovieDirectorCreate
from database import get_db

router = APIRouter()

@router.get("/movie_directors", response_model=list[MovieDirector])
def get_movie_directors(db: Session = Depends(get_db)):
    movie_directors = MovieDirectorService(db).get_movie_directors()
    return movie_directors

@router.get("/movie_directors/{id}", response_model=MovieDirector)
def get_movie_director(id: int, db: Session = Depends(get_db)):
    movie_director = MovieDirectorService(db).get_movie_director(id)
    if not movie_director:
        raise HTTPException(status_code=404, detail="Movie director not found")
    return movie_director

@router.post("/movie_directors", status_code=201, response_model=MovieDirector)
def create_movie_director(movie_director: MovieDirectorCreate, db: Session = Depends(get_db)):
    created_movie_director = MovieDirectorService(db).create_movie_director(movie_director)
    return created_movie_director

@router.put("/movie_directors/{id}", response_model=MovieDirector)
def update_movie_director(id: int, movie_director: MovieDirectorCreate, db: Session = Depends(get_db)):
    updated_movie_director = MovieDirectorService(db).update_movie_director(id, movie_director)
    if not updated_movie_director:
        raise HTTPException(status_code=404, detail="Movie director not found")
    return updated_movie_director

@router.delete("/movie_directors/{id}", status_code=204)
def delete_movie_director(id: int, db: Session = Depends(get_db)):
    MovieDirectorService(db).delete_movie_director(id)
    return

#new