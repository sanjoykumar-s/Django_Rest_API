## Introduction
This is a Django_Rest_Api which can store informations about dogs.

## Installation
```
git clone https://github.com/asif17r/Django-Rest-Api
cd Django-Rest-Api
pip install -r requirements.txt
python manage.py runserver 
```

## Dog-List
The following endpoints are available for the Dog model:
```
- GET /api/dogs/: Get a list of all dogs
- POST /api/dogs/: Create a new dog
- GET /api/dogs/<id>/: Get details for a specific dog
- PUT /api/dogs/<id>/: Update a specific dog
- DELETE /api/dogs/<id>/: Delete a specific dog
```
## Breed-List
The following endpoints are available for the Breed model:
```
- GET /api/breeds/: Get a list of all breeds
- POST /api/breeds/: Create a new breed
- GET /api/breeds/<id>/: Get details for a specific breed
- PUT /api/breeds/<id>/: Update a specific breed
- DELETE /api/breeds/<id>/: Delete a specific breed
```
-----------------------------


**_## Special Thanks to Asifur Rahman to help me to create this API._**