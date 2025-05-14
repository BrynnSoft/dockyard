from pydantic import BaseModel

class TagList(BaseModel):
    name: str
    tags: list[str]