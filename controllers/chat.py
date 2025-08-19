from fastapi import APIRouter

chat_router = APIRouter(prefix='/chat')

@chat_router.post('/ask')
def ask():
    pass

@chat_router.post('/history/{chat_id}')
def get_history(chat_id:str):
    pass

