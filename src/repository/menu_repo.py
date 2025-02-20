from dto import MenuDTO
from src.models.menu_model import MenuModel
import json

class MenuRepo:
    def __init__(
            self, 
            menu_model: MenuModel, 
            menu_dto: MenuDTO
        ) -> None:

        self.menu_model: MenuModel = menu_model
        self.menu_dto: MenuDTO = menu_dto

    def get_menu_item(
            self,
            menu_item_id: int
    ):
        menu_item = self.menu_model.get(
                menu_item_id=menu_item_id
            )
        return MenuDTO(
            menu_item_id=menu_item.menu_item_id,
            name=menu_item.name,
            price=menu_item.price,
            volume=menu_item.volume
        )
    
    def add_menu_item(
        self, 
        name: str, 
        price: int,
        volume: int,
    ):
        return self.menu_model.insert(
            name=name,
            price=price,
            volume=volume,
        ).execute()
