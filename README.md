# INICIA CLONANDO EL PROYECTO

```sh
git clone https://github.com/Folkwine/Curso_python_pip.git #HTTPS
git clone git@github.com:Folkwine/Curso_python_pip.git #SSH
```

# GAME PROJECT


Para correr el juego sigue las siguientes instrucciones en tu terminal:
```sh
cd game
python3 main.py
```


# APP PROJECT

```sh
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt 
python3 main.py
```


# WEB-SERVER

Para correr el server usando FastAPI tienes que:
```sh
cd web-server
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt 
uvicorn main:app --reload
```