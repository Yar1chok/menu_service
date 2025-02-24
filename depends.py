from dto import MenuDTO
from src.models.menu_model import MenuModel
from src.repository.menu_repo import MenuRepo
from src.service.menu_processing_service import MenuProcessingService

menu_repo = MenuRepo(MenuModel, MenuDTO)
menu_service = MenuProcessingService(menu_repo)

def get_menu_service():
    return menu_service
