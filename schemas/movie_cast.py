from pydantic import BaseModel, Field
from typing import Optional

class MovieCast(BaseModel):
        act_id : int = Field(ac=1, description="foreignkey of actor")
        mov_id : int = Field(mo=10, description="foreignkey of movie")
        role : str = Field(max_length=30, min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    "act_id":4,
                    "mov_id":22,
                    "role": "scriptwriter"
                }
            }