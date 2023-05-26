from fastapi import APIRouter,Path,Query
from fastapi.responses import HTMLResponse
from fastapi.responses import  JSONResponse


genres_router = APIRouter()

@genres_router.get('/genres_hello', tags=['genres'], status_code=200)
def get_genres_hello():
    return HTMLResponse('<h1>Hola desde la ruta de genres</h1>')

@genres_router.get('/genres', tags=['genres'], status_code=200)
def get_genres():
    return JSONResponse(content={'message':'this are generes'})

@genres_router.post('/genres', tags=['genres'], status_code=201)
def create_genres():
    return JSONResponse(content={"message":"genre created succesfully"})