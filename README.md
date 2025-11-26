# 🚀 **Stock Price Tracker** 📈

![Stock Price Tracker](https://img.shields.io/badge/Build-Passing-brightgreen?style=flat&logo=github)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)

A simple and fast **stock price tracker** built with **FastAPI**, **SQLAlchemy**, and **SQLite**. Fetches real-time stock prices from the **Alpha Vantage API** and stores the data in a database. Easily track and manage stock prices for any symbol!

---

## 📃 **Table of Contents**

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## ℹ️ **About**

This app allows users to track stock prices by pulling real-time data from the **Alpha Vantage API**. It provides the most recent stock data and stores it in a local **SQLite** database for future reference. You can access stock data via an easy-to-use API.

---

## ⚙️ **Features**

- Real-time stock price data via the **Alpha Vantage API** 📡
- Stores stock data in a **SQLite** database 💾
- Fast and lightweight web framework: **FastAPI** 🚀
- Simple and easy-to-use API endpoints for stock retrieval 📈

---

## 🛠️ **Tech Stack**

- **FastAPI** - Python web framework for building APIs 🚀
- **SQLAlchemy** - ORM for database management 🗄️
- **SQLite** - Lightweight database engine for local storage 🗃️
- **Alpha Vantage API** - Free API for real-time stock data 📊

  **Schemea/Directory/Path**
  finance-app/
├── app/
│   ├── __init__.py         # (ensure this exists)
│   ├── main.py             # FastAPI app is defined here
│   ├── models.py           # Your SQLAlchemy models
│   ├── database.py         # Database connection
│   ├── schemas.py          # Pydantic schemas
└── requirements.txt        # Dependencies


---

## 💻 **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/stock-price-tracker.git
   cd stock-price-tracker

2. **Set up a virtual environment**

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


3. **Install the dependencies**:

pip install -r requirements.txt


4. **Set up environment variables:**

Add your Alpha Vantage API Key to a .env file:

ALPHA_VANTAGE_API_KEY=your-api-key


5. **Run the app:**

uvicorn finance-app.app.main:app --reload


6. **Visit the app:**
Open your browser and go to http://127.0.0.1:8000 to see the app in action.

🌍 API Endpoints
GET /stock/{symbol}

Fetches the most recent stock price for the given symbol from Alpha Vantage and returns it.

Example Request:
GET /stock/AAPL

Example Response:
{
  "id": 1,
  "symbol": "AAPL",
  "price": 277.5,
  "date": "2025-11-25 19:59:00"
}

GET /stocks

Fetches all stocks stored in the database.

Example Request:
GET /stocks

Example Response:
[
  {
    "id": 1,
    "symbol": "AAPL",
    "price": 277.5,
    "date": "2025-11-25 19:59:00"
  },
  {
    "id": 2,
    "symbol": "GOOGL",
    "price": 1320.25,
    "date": "2025-11-25 19:59:00"
  }
]

**🏃 Usage**

Visit the API documentation: http://127.0.0.1:8000/docs to see all available endpoints.

Fetch real-time stock prices by calling the /stock/{symbol} endpoint.

Check the stocks stored in your local database using /stocks.

**👥 Contributing**

We welcome contributions! If you find any issues or have ideas to improve this project, feel free to open an issue or submit a pull request.

Steps to contribute:

Fork the repository

Create a new branch

Make your changes

Open a pull request with a detailed description of the changes

**📝 License**

This project is licensed under the MIT License - see the LICENSE
 file for details.

**📜 Acknowledgments**

Alpha Vantage API - For providing free access to real-time stock data.


FastAPI - For making web development fun and easy!
