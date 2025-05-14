from pydantic import BaseModel

from .error import Error

class ErrorResponse(BaseModel):
    errors: list[Error]