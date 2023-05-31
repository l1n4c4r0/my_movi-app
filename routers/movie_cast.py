from fastapi import APIRouter
from fastapi.responses import JSONResponse

from schemas.movie_cast import MovieCast 
from config.database import Session

movie_cast_router = APIRouter()


@movie_cast_router.get('/actors_for_id', tags=['actors'],status_code=200)
def get_actors_for_id(id:int):
    db = Session()
    result = MovieCastService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@movie_cast_router.get('/movies_for_id', tags=['movies'],status_code=200)
def get_movies_for_id(id:int):
    db = Session()
    result = MovieCastService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@movie_cast_router.post('/role', tags=['role'], status_code=201)
def create_role(role:MovieCast):
    db = Session()
    MovieCastService(db).create_role(role)
    return JSONResponse(content={'message':'role created sucessfull','status_code':201})

                            