# Fayda CreditLink: Smart Loans for Health and Agriculture

## 👥 Contributors:
- Dawit Petros

## 📌 Project Synopsis:

### 🚨 Problem Statement:
Many Ethiopians lack access to formal loans. Farmers and patients especially need support, but banks don’t have reliable ways to evaluate their risk. There’s also risk of misuse with cash-based loans.

### 💡 Planned Solution:
This platform securely links each person’s **Fayda National ID** to their **bank account** using VeriFayda OIDC. It uses **AI analysis on transaction behavior** to assess eligibility for **non-cash loans**:
- Medical support (medicine, tests, surgery)
- Agriculture support (seeds, fertilizer, tools)

Users don’t receive cash—only approved **goods and services**. Payment goes directly to **hospitals or agri suppliers**. Repayments are made with interest, improving bank profitability and reducing misuse.

### 🎯 Expected Outcome:
A web app that:
- Authenticates users via Fayda
- Links bank data
- Analyzes risk with AI
- Enables loan requests for health/agriculture goods

### 🔗 Fayda’s Role:
- Identity verification via VeriFayda
- Secure login & KYC
- Ties individuals to banking and service activity

## 🧰 Tech Stack:
- **Frontend**: React.js (Tailwind CSS, Axios)
- **Backend**: Django (DRF - Django Rest Framework)
- **AI/ML**: Python (scikit-learn for credit scoring)
- **Auth**: VeriFayda OIDC (OAuth 2.0)
- **Database**: PostgreSQL
- **Bank APIs**: Simulated with Swagger or DRF mocks
- **Version Control**: GitHub

---

## 🚀 Getting Started

### Backend Setup
1. Clone the repo
   ```sh
   git clone <repo-url>
   cd faydalink
   ```
2. Create `.env` from `.env.example`
   ```sh
   cp faydalink_backend/.env.example faydalink_backend/.env
   # Or manually copy and fill in your secrets
   ```
3. Activate venv and install packages:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r faydalink_backend/requirements.txt
   ```
4. Run server:
   ```sh
   cd faydalink_backend
   python manage.py runserver
   ```

### Frontend Setup
1. Go to frontend directory
   ```sh
   cd faydalink_frontend
   ```
2. Install dependencies
   ```sh
   npm install
   ```
3. Start React app
   ```sh
   npm start
   ```

### Docker Setup
1. Add real `.env` in `faydalink_backend/`
2. Run:
   ```sh
   docker-compose up --build
   ```
3. Visit: `http://localhost:8000/api/verify-fin/?fin=3126894653473958`

---

## 📁 Project Structure

- faydalink_backend/ — Django backend (APIs, models, admin, .env, Docker)
- faydalink_frontend/ — React frontend (pages, components, routing, API)
- docker-compose.yml — Multi-service orchestration
- README.md — Docs and setup

---

## ⚠️ Git & Version Control
- `.gitignore` is set for both backend and frontend to avoid pushing secrets, build files, and dependencies.
- Always check `.env` and other sensitive files are not committed.

---

## 🧑‍💻 Contributing
- Fork, branch, and PR as usual.
- Backend: Django, DRF, PostgreSQL
- Frontend: React, Axios, Tailwind

---
