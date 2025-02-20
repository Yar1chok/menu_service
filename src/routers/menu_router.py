
from fastapi import APIRouter, Depends

from depends import get_menu_service
from src.service.menu_processing_service import MenuProcessingService

menu_router = APIRouter(
    prefix="/menu", 
    tags=["menu"]
)

@menu_router.get("/get_menu_item")
def get_menu_item(
    menu_item_id: int,
    menu_processing_service: MenuProcessingService = Depends(get_menu_service)
):
    return menu_processing_service.get_menu_item(menu_item_id)

@menu_router.post("/add_menu_item")
def add_menu_item(
    name: str,
    price: int,
    volume: int,
    menu_processing_service: MenuProcessingService = Depends(get_menu_service),
):
    return menu_processing_service.add_menu_item(name, price, volume)