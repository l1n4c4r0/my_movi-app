from pydantic import BaseModel, Field
from typing import Optional

class MovieDirector(BaseModel):
        id : Optional[int] = None
        dir_id : int = Field(ge=1, description="llave foranea de director")
        mov_id : int = Field(ge=1, description="id de la pelicula")

        class Config:
            schema_extra = {
                "example":{
                    "dir_id":2,
                    "mov_id":3
                }
            }