from pydantic import BaseModel, Field
from typing import Annotated, Optional

class Todo(BaseModel) :
    id: Annotated[Optional[str], Field(default=None, description='id of the todo')]
    title : Annotated[str, Field(..., description='title of the todo', max_length=50)]
    description : Annotated[Optional[str], Field(description='desc of the todo', max_length=150)]
    completed : Annotated[bool, Field(..., description='is the todo completed?')]