from pydantic import BaseModel, Field
from typing import Optional

class MovieGenres(BaseModel):
    id : Field(ge=1, description="id de genres")
    mov_id :int = Field(ge=1, description="id de movie")

    class Config:
        schema_extra = {
            "example": {
                "id":2,
                "mov_id":3
            }
        }