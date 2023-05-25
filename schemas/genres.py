from pydantic import BaseModel, Field
from typing import Optional


class Genres(BaseModel):
    id : Optional[int] = None
