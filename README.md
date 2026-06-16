# Students API

A simple REST API built with FastAPI for managing student records.

## Features

- FastAPI-based REST API
- Retrieve student information
- JSON response support
- Dockerized application
- Unit testing support
- CI/CD workflow integration

## Project Structure

.
├── .github/workflows/
├── Dockerfile
├── main.py
├── requirements.txt
└── test_main.py

## API Endpoints

### Home Endpoint

GET /

Response:

{
  "message": "Student API"
}

### Get Students

GET /students

Response:

[
  {
    "id": 1,
    "name": "Rahul"
  },
  {
    "id": 2,
    "name": "Amit"
  }
]

## Installation

### Clone Repository

git clone https://github.com/rathansai-dev/students-api.git

cd students-api

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

## Run Application

uvicorn main:app --reload

Server will start at:

http://127.0.0.1:8000

## API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

## Docker Setup

Build Image

docker build -t students-api .

Run Container

docker run -p 8000:8000 students-api

## Running Tests

pytest

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pytest
- Docker
- GitHub Actions

## Future Enhancements

- CRUD operations for students
- Database integration
- Authentication & Authorization
- Pagination and filtering
- Deployment to cloud platforms

## Author

Rathan Sai