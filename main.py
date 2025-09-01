from fastapi import FastAPI, HTTPException
from database import init_db, get_db
from schemas import WalletUpdate, TransactionOut
from crud import get_users, update_wallet, get_transactions

app = FastAPI(title="Wallet Management API")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/users")
def list_users():
    db = get_db()
    users = get_users(db)
    return users

@app.post("/wallet/update/{user_id}")
def update_user_wallet(user_id: int, payload: WalletUpdate):
    db = get_db()
    try:
        updated = update_wallet(db, user_id, payload.amount)
        return {"message": "Wallet updated successfully", "balance": updated}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/transactions/{user_id}", response_model=list[TransactionOut])
def fetch_transactions(user_id: int):
    db = get_db()
    txns = get_transactions(db, user_id)
    if not txns:
        raise HTTPException(status_code=404, detail="No transactions found")
    return txns
