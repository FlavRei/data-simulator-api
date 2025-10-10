Lancer l'API :
> poetry run uvicorn src.main:app --reload

Lancer les tests : 
> poetry run pytest

Lancer le container : 
> docker build -t data-simulator-api .
> docker run -p 8000:8000 data-simulator-api

Documentation de l'API :
> http://127.0.0.1:8000/docs

