from pydantic import  BaseModel, Field
from typing import Optional 


class Rating(BaseModel):
        id : Optional[int] = None
        mov_id : int = Field(ge=1, description="foreign key of the movie")
        rev_id : int = Field(ge=1, description="foreign key of reviewer")
        rev_stars : int = Field(ge=1, description="foreign key of the number of stars")
        num_o_ratings : int = Field(ge=1, description="numbers and ratings")


        class Config:
            schema_extra = {
                "example":{
                    "mov_id":2,
                    "rev_id":3,
                    "rev_stars":4,
                    "num_o_ratings":5
                }
            }
    
    