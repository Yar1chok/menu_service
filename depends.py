from dto import MenuDTO
from src.service.data_service import DataService
from src.repository.data_repo import DataRepo
from src.service.connection_service import ConnectionService
from src.repository.connection_repo import ConnectionRepo
from src.models.menu_model import MenuModel
from src.repository.menu_repo import MenuRepo
from src.service.menu_processing_service import MenuProcessingService

menu_repo = MenuRepo(MenuModel, MenuDTO)
menu_service = MenuProcessingService(menu_repo)

data_repo = DataRepo()
data_service = DataService(data_repo)

connection_repo = ConnectionRepo()
connection_service = ConnectionService(connection_repo)

def get_menu_service():
    return menu_service

def get_data_storage():
    return data_service

def get_websocket_manager():
    return connection_service