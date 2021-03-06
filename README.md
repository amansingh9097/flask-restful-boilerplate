# flask-restful-boilerplate
A minimal boilerplate for creating RESTful services using Flask, SQLAlchemy and Flask-RestPlus. This boilerplate has swagger-UI) [for personal use]

<img src="swagger-ui.PNG">

## What it includes?
- capabilities of establishhing connection to any database using `SQLAlchemy`.
- a `service logger` for logging all the events, warnings, errors, etc.
- a placeholder for declaring all your `constants`.
- a placeholder for all your declared `database models`.
- entire codeset is config-driven.
- hosting of `swagger-UI` for your RESTful API's documentation.
- hosting `multiple namespaces` in the routes.
- a `custom response generator` for the payloads.

## Setting up:
- install all the requirements from `requirements.txt`<br>
```pip install -r requirements.txt```
- make necessary changes in `config.ini`
  - add `host` address (default="127.0.0.1")
  - add `port` address (default=5000)
  - set a `name` for the flask restful service (default="flask-minimal-boilerplate")
  - add the `database url` (default="postgresql://scott:tiger@localhost/sample_db")
- create a directory called **logs** in the current working directory. This is where all your log fiels will be stored.

## Directory structure:
```tree
├── src
│   ├── core
|   |   ├── db_connection.py
|   |   ├── models.py
│   ├── instance
|   |   ├── config.py
|   |   ├── flask_app.py
│   ├── misc
|   |   ├── constants.py
|   |   ├── db_misc_functions.py
|   |   ├── response_generator.py
|   |   ├── service_logger.py
│   ├── routes
|   |   ├── item_1
|   |   |   ├── item_1_route_1.py
|   |   ├── item_2
|   |   |   ├── item_2_route_1.py
│   ├── namespaces.py
├── config.ini
├── requirements.txt
├── run.py
```

## Running the program:
- after having setup everything above, run the program using 
```python
python run.py
```
