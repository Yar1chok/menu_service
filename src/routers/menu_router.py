
from fastapi import APIRouter, Depends

from src.app.http_exceptions import EntityDoesNotExistError, EntityNoMinimumLength
from depends import get_menu_service
from dto import ChequeDTO
from src.service.menu_processing_service import MenuProcessingService

menu_router = APIRouter(
    prefix="/menu", 
    tags=["menu"]
)

@menu_router.get("/get_menu_item")
def get_menu_item(
    menu_id: int,
    menu_processing_service: MenuProcessingService = Depends(get_menu_service)
):
    try:
        return menu_processing_service.get_menu_item(menu_id)
    except menu_processing_service.EntityDoesNotExist as e:
        raise EntityDoesNotExistError(e.model)

@menu_router.post("/add_menu_item")
def add_menu_item(
    name: str,
    price: int,
    volume: int,
    menu_processing_service: MenuProcessingService = Depends(get_menu_service),
):
    try:
        return menu_processing_service.add_menu_item(name, price, volume)
    except menu_processing_service.EntityNoMinimumLength as e:
        raise EntityNoMinimumLength(e.model)


@menu_router.post("/get_cheque_item")
def get_cheque_item(
    cheque: ChequeDTO,
    menu_processing_service: MenuProcessingService = Depends(get_menu_service),
):
    return menu_processing_service.get_cheque_item(cheque)


