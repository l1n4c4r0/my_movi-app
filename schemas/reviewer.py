from pydantic import BaseModel, Field
from typing import Optional


class Reviewer(BaseModel):
    id : Optional[int] = None
    rev_name : str = Field(max_length=35,min_length=2, description="Nombre de Critico")

    class Config: 
        schema_extra = {
            "example":{
                "id":2,
                "rev_name":"Jack Malvern"
            }
        }