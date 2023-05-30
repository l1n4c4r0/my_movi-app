from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from service.genres import GenresService
from schemas.genres import Genres
from config.database import Session

genres_router = APIRouter()


@genres_router.get('/genres_hello', tags=['genres'], status_code=200)
def get_genres_hello():
    """function to check the route"""
    return HTMLResponse('<h1>Hola desde la ruta de genres</h1>')


@genres_router.get('/genres', tags = ['genres'], status_code=200)
def get_genres():
    db = Session()
    result = GenresService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code = 200)


# funcion que trae todos los generos que esta en servicios
@genres_router.get('/genres', tags=['genres'], status_code=200)
def get_router(id: int):
    return JSONResponse(content={"message": "genre created successfully"})


# llamar una funcion que va a estar en el servicios
# @genres_router.post('/genres', tags='genres', status_code=201)
# def create_genres():
#     return JSONResponse(content={"message":"genre created successfully"})

@genres_router.post('/genres', tags=['genres'], status_code=201)
def create_genres(genres: Genres):
    db = Session()
    GenresService(db).create_genre(genres)
    return JSONResponse(content={"message": "genre created successfully", "status_code": 201})

# creamos un get que trae un solo genero por id


@genres_router.get('/genres_for_id', tags=['genres'], status_code=200)
def get_genres_id(id: int):
    db = Session()
    genre = GenresService(db).get_for_id(id)
    return JSONResponse(genre)


# para el genres delete debemos verificar que el id existe y despues ese genero lo eliminamos
# @genrens_router.detele('/genres/{genres_id}', tags=['genres'], status_code=204)
# def detele_genre_by_id(genres_id: int):
#     return JSONResponse (content= {"message": f"Genero con ID {genres_id} Elimiado correctamente"})

# Put
@genres_router.put('/genres{id}', tags=['genres'])
def update_genres(id: int, data: Genres):
    db = Session()
    result = GenresService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message": "genres don't found", "status code": 404})
    GenresService(db).update_genres(data)
    return JSONResponse(content={"message": "genre update successfully", "status_code": 202}, status_code=202)

# Detele


@genres_router.delete('/genres{id}', tags=['genres'])
def delete_genres(id: int):
    db = Session()
    result = GenresService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message": "genres dont found", "status code": 404})
    GenresService(db).delete_genres(id)
    return JSONResponse(content={"message": "genre delete successfully", "status_code": 200}, status_code=200)
