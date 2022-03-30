# Build the REST API (using Django’s REST Framework) and background photo resizing. 
This is RESTAPI for webapp's that provides a file upload, save to database, enqueue background job and send response.

## Packages
- Django & Django Rest Framework: Project structure and the entirety of the REST API.
- Resque with Redis 
- ImageMagick and wand: Image processing (resizing).

## API's
- Record management
  - POST request on `/record/`: Create a new record.
  - GET request on `/record/`: List all the records.

## 3 Endpoints
1) User post a attribute along with photo, save to database, enqueue background job and send response.
2) Should return all records by ordered by date with resized photo.
3) All photos should be resized to be max 140x140px.

## Installation
- other libraries are listed in requirements.txt


Clone this repository to run in your local machine


### Install libraries

```
pip install -r requirements.txt
```

### Run code
```
cd bezen
python manage.py runserver
```