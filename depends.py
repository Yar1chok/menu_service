from dto import MenuDTO
from src.service.connection_service import ConnectionService
from src.repository.connection_repo import ConnectionRepo
from src.models.datastorage import DataStorage
from src.models.menu_model import MenuModel
from src.repository.menu_repo import MenuRepo
from src.service.menu_processing_service import MenuProcessingService

menu_repo = MenuRepo(MenuModel, MenuDTO)
menu_service = MenuProcessingService(menu_repo)

data_model = DataStorage()

connection_repo = ConnectionRepo()
connection_service = ConnectionService(connection_repo)

def get_menu_service():
    return menu_service

def get_data_storage():
    return data_model

def get_websocket_manager():
    return connection_service