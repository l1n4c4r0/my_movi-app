-from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder


from service.reviewer import ReviewerService
from schemas.reviewer import Reviewer
from config.database import Session


reviewer_router = APIRouter()


@reviewer_router.get("/reviewer", tags=["reviewer"], status_code=200)
def get_reviewer():
    db = Session()
    result = ReviewerService(db).get_reviewer()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@reviewer_router.get("/reviewer_for_id", tags=["reviewer"], status_code=200)
def get_reviewer_for_id(id: int):
    db = Session()
    result = ReviewerService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@reviewer_router.post("/reviewer", tags=["reviewer"], status_code=201)
def create_reviewer(reviewer: Reviewer):
    db = Session()
    ReviewerService(db).create_reviewer(reviewer)
    return JSONResponse(
        content={"message": "Reviewe created successfully", "status_code": 201}
    )


@reviewer_router.put("/reviewe{id}", tags=["reviewer"])
def update_reviewe(id: int, reviewer: Reviewer):
    db = Session()
    result = ReviewerService(db).get_for_id(id)
    if not result:
        return JSONResponse(
            content={"message": "reviewe don't gound", "status_code": 404}
        )
    ReviewerService(db).update_reviewe(reviewer)
    return JSONResponse(
        content={"message": "reviewe update successfully", "status_code": 202},
        status_code=200,
    )


@reviewer_router.delete("/reviewer{id}", tags=["reviewer"])
def delete_reviewe(id: int):
    db = Session()
    result = ReviewerService(db).get_for_id(id)
    if not result:
        return JSONResponse(
            content={"message": "reviewe don't gound", "status_code": 404}
        )
    ReviewerService(db).delete_reviewe(id)
    return JSONResponse(
        content={"message": "reviewe delete successfully", "status_code": 200},
        status_code=200,
    )
