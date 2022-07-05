import datetime as dt
from typing import Optional

import pydantic as pd


class VoterSchemaBase(pd.BaseModel):
    name: str
    village: Optional[str] = None
    contact: Optional[str] = None
    notes: Optional[str] = None
    importance: Optional[str] = None


class VoterSchema(VoterSchemaBase):
    id: str
    date_delivered: dt.datetime
    contributed_by: str

    class Config:
        orm_mode = True
