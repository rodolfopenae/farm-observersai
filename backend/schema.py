from pydantic import BaseModel


class DistinctionResponse(BaseModel):
    body: str
