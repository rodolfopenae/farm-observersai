from pydantic import BaseModel, Field
from typing import Optional, Any, Dict
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Any, values: Dict[str, Any]):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema: dict, field: Optional[Any] = None) -> dict:
        schema.update(type="string")
        return schema


class DistinctionModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    body: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
