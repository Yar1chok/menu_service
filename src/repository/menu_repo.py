from dto import MenuDTO
from src.models.menu_model import MenuModel


class MenuRepo:
    def __init__(
            self, 
            menu_model: MenuModel, 
            menu_dto: MenuDTO
        ) -> None:

        self.menu_model: MenuModel = menu_model
        self.menu_dto: MenuDTO = menu_dto

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


    def get_menu_item():
        pass