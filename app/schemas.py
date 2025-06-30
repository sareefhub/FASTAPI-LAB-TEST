from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    surname: str
    description: str
    price: float

class ItemCreated(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True
