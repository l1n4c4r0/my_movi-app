from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas.movie_cast import MovieCast 
from service.movie_cast import MovieCastService
from config.database import Session

movie_cast_router = APIRouter()


@movie_cast_router.get('/actors_for_id', tags=['actors',"role"],status_code=200)
def get_actors_for_id(id:int):
    db = Session()
    result = MovieCastService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@movie_cast_router.get('/movies_for_id', tags=['movies',"role"],status_code=200)
def get_movies_for_id(id:int):
    db = Session()
    result = MovieCastService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@movie_cast_router.post('/role', tags=['role'], status_code=201)
def create_role(role:MovieCast):
    db = Session()
    MovieCastService(db).create_role(role)
    return JSONResponse(content={'message':'role created sucessfull','status_code':201})

@movie_cast_router.put('/actors{id}', tags=['actors',"role"])
def update_actors_for_id(id:int, act_id:MovieCast):
    db = Session()
    result = MovieCastService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':'actors don´t gound','status_code':404})
    MovieCastService(db).update_actors_for_id(actor)
    return JSONResponse(content={'message':'actors update successfully', 'status_code':202}, status_code=200)

@movie_cast_router.put('/movies{id}', tags=['movies',"role"])
def update_movies_for_id(id:int, mov_id:MovieCast):
    db = Session()
    result = MovieCastService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':'movies don´t gound','status_code':404})
    MovieCastService(db).update_movies_for_id(movie)
    return JSONResponse(content={'message':'movies update successfully', 'status_code':202}, status_code=200)

@movie_cast_router.delete('/actor{id}',tags=['actors',"role"])
def delete_actors_for_id(id:int):
    db = Session()
    result = MovieCastService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':'actors don´t gound', 'status_code':404})
    ActorService(db).delete_actors_for_id(id)
    return JSONResponse(content={'message':'actors delete sucessfully','status_code':200}, status_code=200)

@movie_cast_router.delete('/movies{id}',tags=['movies',"role"])
def delete_movies_for_id(id:int):
    db = Session()
    result = MovieCastService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':'movies don´t gound', 'status_code':404})
    MovieCastService(db).delete_movies_for_id(id)
    return JSONResponse(content={'message':'movies delete sucessfully','status_code':200}, status_code=200)

                            