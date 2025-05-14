from pydantic import BaseModel, Field

from typing import Optional

from ...enums.error_code import ErrorCode

class Error(BaseModel):
    code: ErrorCode
    message: Optional[str] = Field(None)
    detail: Optional[str] = Field(None)