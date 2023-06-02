from fastapi import APIRouter, HTTPException
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder

from service.movie_director import MovieDirectorService
from schemas.movie_director import MovieDirector
from config.database import Session 

movie_director_router = APIRouter()

@movie_director_router.get('/director_for_id', tags = ['director'],status_code=200)
def get_director_for_id(id : int):
    db = Session ()
    result = MovieDirectorService (db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@movie_director_router.get("/movie_for_id",tags = ['movie'],status_code=200)
def get_movie_for_id(id : int):
    db = Session ()
    result = MovieDirectorService (db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

#@movie_director_router.post("/movie_director", tags= [MovieDirector])
#def create_movie_director(movie_director: MovieDirectorCreate, db: Session = Depends(get_db)):
#    created_movie_director = MovieDirectorService(db).create_movie_director(movie_director)
#    return created_movie_director

@movie_director_router.post('/director',tags=['director'], status_code=201)
def create_director(director:MovieDirector):
    db = Session()
    MovieDirectorService(db).create_director(director)
    return JSONResponse(content={"message":"director created successfully",'status_code':201})

@movie_director_router.put("/", response_model=MovieDirector)
def update_movie_director(id: int, movie_director: MovieDirector):
    db = Session()
    updated_movie_director = MovieDirectorService(db).update_movie_director(id, movie_director)
    if not updated_movie_director:
        raise HTTPException(status_code=404, detail="Movie director not found")
    return updated_movie_director

@movie_director_router.delete("/movie_directors/{id}", status_code=204)
def delete_movie_director(id: int):
    db = Session
    MovieDirectorService(db).delete_movie_director(id)
    return

#new