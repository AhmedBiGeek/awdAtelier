# notification microservice

Python / FastAPI microservice, **no database**, with Swagger documentation generated automatically.
It exposes one endpoint for now; the notification logic is a TODO for students (see [TODO.md](TODO.md)).

## Run
```bash
cd chemin\vers\notification

# 1. Créer et activer l'environnement virtuel (une seule fois)
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Installer les dépendances
python -m pip install -r requirements.txt

# 3. Lancer le microservice (Eureka doit tourner sur :8761)
python -m uvicorn app.main:app --reload --port 8084   # or: python -m app.main
```
- API: http://localhost:8084/api/notifications/hello
- Health: http://localhost:8084/health
- Info: http://localhost:8084/info
- Swagger UI: http://localhost:8084/swagger-ui
- OpenAPI JSON: http://localhost:8084/v3/api-docs
- ReDoc: http://localhost:8084/redoc

Port `8084`. Change with `PORT=9084` for a second Eureka instance.

## Endpoint
| Method | Path | Response |
|---|---|---|
| GET | /api/notifications/hello | `200 {"message": "hello I'm microservice notification"}` |
| GET | /health | `200 {"status":"UP"}` |
| GET | /info | `200` name + version |

## Tests
```bash
pip install -r requirements-dev.txt
pytest
```

## Structure
```
notification/
├── app/
│   ├── main.py                    FastAPI app + Swagger config
│   ├── schemas.py                 Pydantic models (validation + Swagger schemas)
│   └── routers/notification.py    /api/notifications routes (hello + TODO)
├── tests/test_hello.py
├── TODO.md                        work for students
├── requirements.txt / requirements-dev.txt
└── pytest.ini
```
