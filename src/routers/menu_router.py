
import asyncio
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from src.service.data_service import DataService
from src.service.connection_service import ConnectionService
from src.app.http_exceptions import EntityDoesNotExistError, EntityNoMinimumLength
from depends import get_data_storage, get_menu_service, get_websocket_manager
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
    data_storage: DataService= Depends(get_data_storage)
):
    try:
        res = menu_processing_service.get_cheque_item(cheque)
        data_storage.save_data(res)
        return res
    except menu_processing_service.EntityDoesNotExist as e:
        if data_storage is not None:
            data_storage.save_data(None)
        raise EntityDoesNotExistError(e.model)
    
@menu_router.get("/get_saved_data")
def get_saved_data(data_storage: DataService = Depends(get_data_storage)):
    saved_data = data_storage.get_data()
    if saved_data is None:
        raise HTTPException(status_code=404, detail="No data saved yet")
    return {"saved_data": saved_data}

@menu_router.websocket("/get_saved_data_ws")
async def get_saved_data_websocket(
    websocket: WebSocket,
    connection_serivce: ConnectionService = Depends(get_websocket_manager),
    data_storage: DataService = Depends(get_data_storage)
):
    await connection_serivce.connect(websocket)
    last_sent_data = None
    try:
        while True:
            saved_data = data_storage.get_data()
            if saved_data != last_sent_data:
                if saved_data is None:
                    await connection_serivce.broadcast({"error": "No data saved yet"})
                else:
                    await connection_serivce.broadcast(saved_data.dict())
                last_sent_data = saved_data
            await asyncio.sleep(0.5) 
    except WebSocketDisconnect:
        connection_serivce.disconnect(websocket)

