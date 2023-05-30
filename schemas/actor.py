from pydantic import BaseModel, Field
from typing import Optional

class Actor(BaseModel):
    act_id : Optional[int] = None
    act_fname : str = Field(max_length=20, min_length=3, description="Firts name")
    act_lname : Optional[str] = Field(max_length=20, min_lentgth = 3, description="Last name")
    act_gender : str = Field(max_length = 1, description="id genero")

    class Config:
        schema_extra = {
            "example": {
                "act_id": 1,
                "act_fname": "Jose",
                "act_lname": "Fernamdez",
                "act_gender": "2"
            }
        }