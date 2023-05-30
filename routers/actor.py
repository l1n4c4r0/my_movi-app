from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from service.actor import ActorService
from schemas.actor import Actor as ActorSchema
from config.database import Session


actors_router = APIRouter()

@actors_router.get('/actors', tags=['actors'], status_code=200)
def get_actors():
    db = Session()
    result = ActorService(db).get_actors()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@actors_router.get('/actors_for_id', tags=['actors'], status_code=200)
def get_actors_for_id(id:int):
    db = Session()
    result = ActorService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@actors_router.post('/actors', tags=['actors'], status_code=201)
def create_actors(actors:ActorSchema):
    db = Session()
    ActorService(db).create_actors(actors)
    return JSONResponse(content={'message':'actor created sucessfull','status_code':201})

@actors_router.put('/actor{id}', tags=['actors'])
def update_actor(id:int, actor:ActorSchema):
    db = Session()
    result = ActorService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':'actor don´t gound','status_code':404})
    ActorService(db).update_actor(actor)
    return JSONResponse(content={'message':'actor update successfully', 'status_code':202}, status_code=200)


@actors_router.delete('/actor{id}',tags=['actors'])
def delete_actor(id:int):
    db = Session()
    result = ActorService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':'genre don´t gound', 'status_code':404})
    ActorService(db).delete_actor(id)
    return JSONResponse(content={'message':'gente delete sucessfully','status_code':200}, status_code=200)