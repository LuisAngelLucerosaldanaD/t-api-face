# Check ID Face API

## Creación y activación del entorno virtual

Este API hace uso del entorno virtual de que nos provee Python para el aislamiento de librerias y componentes

Inicialización del entorno virtual

````bash
python -m venv venv
````

Despues de generar el entorno virtual se debe de activar el entorno virutal

* Para sistema operativo Windows

````bash
.\env\Scritps\activate 
````

* Para sistemas operativos basados en Linux

````bash
./venv/Scripts/activate
````

## Instalación de librerias

Para instalar las librerias se debe primero generar el entorno virtual
y luego ejecutar el sigueinte comando

````bash
pip install -r requirements.txt
````