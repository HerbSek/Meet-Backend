from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Union,List,Dict


class create_members(BaseModel):
    name: str
    year:str
    dev:bool 
    des:bool
    pm:bool
    core:bool
    mentor:bool
    major:str
    minor:str
    birthday:str
    home:str
    quote:str
    favorite_thing_1: str = Field(..., alias="favorite thing 1")
    favorite_thing_2: str = Field(..., alias="favorite thing 2")
    favorite_thing_3: str = Field(..., alias="favorite thing 3")
    favorite_dartmouth_tradition: str = Field(..., alias="favorite dartmouth tradition")
    fun_fact: str = Field(..., alias="fun fact")
    picture:str


class update_members(BaseModel):
    name:Optional [str]= None
    year: Optional[str] = None
    dev:Optional[bool] = None
    des:Optional[bool]= None
    pm:Optional[bool]= None
    core:Optional[bool]= None
    mentor:Optional[bool]= None
    major:Optional[str]= None
    minor:Optional[str]= None
    birthday:Optional[str]= None
    home:Optional[str]= None
    quote:Optional[str]= None
    favorite_thing_1: Optional[str] = Field(None, alias="favorite thing 1")
    favorite_thing_2: Optional[str]= Field(None, alias="favorite thing 2")
    favorite_thing_3: Optional[str] = Field(None, alias="favorite thing 3")
    favorite_dartmouth_tradition: Optional[str] = Field(None, alias="favorite dartmouth tradition")
    fun_fact :Optional[str] = Field(None, alias="fun fact")
    picture:Optional[str]= None














model_config = ConfigDict(arbitrary_types_allowed=True)

