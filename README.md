# Backend Development Challenge 


## Features
- FastAPI
- Postgres
- SQLAlchemy
- Railway

  ### API Endpoints
  1. UnitMeasurement (CRUD)
  2. Products (CRUD)
  3. Generate sales

  ### API Requests
  4. Get the sales of each product (Quantity and amount)
  5. Get the sales of all products (Quantity and amount)

## How to use and run

- Create `.env` file with the following variable: 

  ```
  DATABASE_URL=postgresql://{PGUSER}:{PGPASSWD}@{PGHOST}:{PGPORT}/{PGDBNAME}
  ```

- Create an activate a virtual environment on Linux/MacOS

  ```python
  python -m venv env
  source env/bin/activate
  ```

- Install packages with Pip using `pip install -r requirements.txt`

- Add `origins` to the `main.py` file

  ```
  [...]
  origins [
  	"..."
  ]
  ```

- Run using `uvicorn main:app --env-file=.env --reload`

- Go to `http://127.0.0.1:8000/docs` to use Endpoints
