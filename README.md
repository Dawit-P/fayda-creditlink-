
## FaydaLink

### Setup (Local)

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
   pip install -r requirements.txt
   ```
4. Run server:
   ```sh
   python manage.py runserver
   ```

### Docker Setup

1. Add real `.env` in `faydalink_backend/`
2. Run:
   ```sh
   docker-compose up --build
   ```
3. Visit: `http://localhost:8000/api/verify-fin/?fin=3126894653473958`
