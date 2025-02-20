import pydantic

class MenuDTO(pydantic.BaseModel):
    name: str
    price: int
    volume: int
    
