from typing import List
from dto import ChequeDTO, ProductDTOandMenuDTO
from dto import ProductDTO
from src.repository.menu_repo import MenuRepo
import peewee

class MenuProcessingService:
    class EntityDoesNotExist(Exception):
        def __init__(self, _model, *args) -> None:
            super().__init__(*args)
            self.model = _model
            
    class EntityNoMinimumLength(Exception):
        def __init__(self, _model, *args) -> None:
            super().__init__(*args)
            self.model = _model

    def __init__(self, menu_repo: MenuRepo):
        self.menu_repo = menu_repo

    def get_menu_item(self, menu_id):
        try:
            return self.menu_repo.get_menu_item(menu_id)
        except self.menu_repo.EntityDoesNotExist as e:
            raise self.EntityDoesNotExist(e.model)

    def add_menu_item(
        self, 
        name: str, 
        price: int,
        volume: int,
        ):
        try:
            return self.menu_repo.add_menu_item(name, price, volume)
        except self.menu_repo.EntityNoMinimumLength as e:
            raise self.EntityNoMinimumLength(e.model)

    def get_cheque_item(
            self,
            cheque: ChequeDTO
        ):
        products: List[ProductDTO] = cheque.product_list
        for product in products:
            try:
                model_menu = self.menu_repo.get_menu_item(product.real_id)
                return ProductDTOandMenuDTO(
                    real_id = product.real_id,
                    menu_item_id = product.menu_item_id,
                    amount = product.amount,
                    name = model_menu.name,
                    price = model_menu.price,
                    volume = model_menu.volume,
                )
            except self.menu_repo.EntityDoesNotExist as e:
                raise self.EntityDoesNotExist(e.model)
                

        