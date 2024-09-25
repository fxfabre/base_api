from pydantic import BaseModel


class CustomModel(BaseModel):
    date: str
    message: str
