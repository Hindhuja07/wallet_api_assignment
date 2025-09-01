from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    phone: str

class WalletUpdate(BaseModel):
    amount: float

class TransactionOut(BaseModel):
    id: int
    user_id: int
    amount: float
    type: str
    timestamp: str
