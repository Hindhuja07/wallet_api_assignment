# wallet_api_assignment
Wallet API Assignment
This project is a FastAPI-based Wallet Management API that provides functionality to create wallets, check balances, and perform credit/debit transactions. The project includes auto-generated API documentation with Swagger UI for easy testing.
🚀 Features
Create a wallet with a unique wallet_id.



Credit money to a wallet.



Debit money from a wallet (with balance check).


Retrieve wallet balance.


RESTful API with Swagger UI documentation.


Lightweight and easy to run locally.


🛠 Tech Stack

Python 3.10+


FastAPI (web framework)


Uvicorn (ASGI server)


Pydantic (data validation)


📂 Project Structurewallet_api_assignment/
│── main.py              # FastAPI entry point│── models.py            # Request/response models
│── wallet_service.py    # Core wallet logic│── requirements.txt     # Python dependencies
└── README.md            # Project documentation
⚙️ Installation & Setup
1️⃣ Clone the repositorygit clone https://github.com/<your-username>/wallet_api_assignment.git
cd wallet_api_assignment
2️⃣ Create a virtual environment
python -m venv venv
3️⃣ Activate the environment

Windows (PowerShell):


.\venv\Scripts\activate

Linux/MacOS:


source venv/bin/activate

4️⃣ Install dependenciespip install -r requirements.txt

5️⃣ Run the FastAPI serveruvicorn main:app --reload

🌐 Accessing the API
Once the server is running, open your browser:


Swagger UI (API docs): 👉 http://127.0.0.1:8000/docs


ReDoc (alternative docs): 👉 http://127.0.0.1:8000/redoc



Note: Accessing http://127.0.0.1:8000/ directly will show {"detail": "Not Found"} because the root path is not defined. Use /docs for Swagger.

📌 Example API Usage1️⃣ Create a Wallet
POST /wallets/
{  "wallet_id": "user123"
}

2️⃣ Credit Money
POST /wallets/user123/credit
{
  "amount": 500}

3️⃣ Debit Money
POST /wallets/user123/debit
{  "amount": 200
}
4️⃣ Check Balance
GET /wallets/user123
{  "wallet_id": "user123",
  "balance": 300}

✅ Expected Output
Root URL (http://127.0.0.1:8000/) → {"detail": "Not Found"} (this is correct).


Swagger UI (http://127.0.0.1:8000/docs) → Full API documentation where you can test requests interactively.


📦 Submission Notes

The project is designed to be run locally.


Reviewers can simply follow the setup steps, run uvicorn main:app --reload, and test APIs using Swagger UI.


No external database is required (in-memory storage used for simplicity).


✨ Done! You are now ready to use and test the Wallet API.
