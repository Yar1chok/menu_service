from src.repository.menu_repo import MenuRepo


class MenuProcessingService:

    def __init__(self, menu_repo: MenuRepo):
        self.menu_repo = menu_repo

    def get_menu_item(self, menu_item_id):
        return self.menu_repo.get_menu_item(menu_item_id)

    def add_menu_item(
            self, 
        name: str, 
        price: int,
        volume: int,
        ):
        return self.menu_repo.add_menu_item(name, price, volume)