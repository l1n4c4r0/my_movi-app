from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from service.rating import RatingService
from schemas.rating import Rating
from config.database import Session

rating_router = APIRouter()

#Function to check the router
@rating_router.get('/ratings', tags = ['ratings'], status_code = 200)
def get_ratings_hello():
    return HTMLResponse('<h1>Hola desde la ruta de rating</h1>')


# @rating_router.get('/ratings', tags=['ratings'], status_code=200)
# def get_ratings():
#     db = Session()
#     result = RatingService(db).get_ratings()
#     return JSONResponse(content=jsonable_encoder(result), status_code=200)

# @rating_router.get('/ratings', tags = ['ratings'], status_code = 200)
# def get_router(id : int):
#    return JSONResponse(content = {"message":"rating created succesfully"})


#@rating_router.post('/ratings', tags=['ratings'], status_code=201)
#def crate_ratings(rating: Rating):
#    db = Session()
#    RatingService(db).create_rating(rating)
#    return JSONResponse(content={"message": "rating created succesfully", "status_code": 201})


#@rating_router.get('/rating_for_id', tags=['ratings'], status_code=200)
#def get_ratings_id(id: int):
#    db = Session()
#    rating = RatingService(db).get_for_id(id)
#    return JSONResponse(rating)


# @rating_router.put('/ratings/{id}', tags=['ratings'])
# def update_genres(id: int, data: Rating):
#     db = Session()
#     result = RatingService(db).get_for_id(id)
#     if not result:
#         return JSONResponse(content={"message": "gnere update succesfully", "status_code": 202})


# @rating_router.put('/ratings/{id}', tags=['ratings'])
# def update_genres(id: int, data: Rating):
#     db = Session()
#     result = RatingService(db).get_for_id(id)
#     if not result:
#         return JSONResponse(content={"message": "gnere update succesfully", "status_code": 202})

