from pydantic import BaseModel

class TestSchema(BaseModel):
    text: str

    class Config:
        orm_mode = True



class GoogleToken(BaseModel):
    token: str

    class Config:
        orm_mode = True


class UserDataSchema(BaseModel):
    id: str
    data: dict

    class Config:
        orm_mode = True