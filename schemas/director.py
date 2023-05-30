from pydantic import BaseModel, Field
from typing import Optional


class Director(BaseModel):
    id : Optional[int] = None
    dir_fname : str = Field(max_length=20,min_length=3, description= "full name of director")
    dir_lname : str = Field(max_length=10,min_length=3,description= "last name of director")
    
    class Config: 
        schema_extra = {
            "example":{
                "id":1,
                "dir_fname":"Steven Spielberg",
                "dir_lname":"Spielberg"
            }
        }