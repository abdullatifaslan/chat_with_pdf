#  Chat PDF Files

The aim of the project is to read the texts in the pdf files and send them to the Gemini LLM model accordingly to get answers to certain questions.

## Requirements Tools

- Python 3.11
- Python virtual environment

## Requirement Steps
##### Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # For Windows -> venv\Scripts\activate
```
##### Install Requirement Libraries:

```bash
pip install -r requirements.txt
```

##### Environment Variables
Create .env file and add below informations:

```makefile
GEMINI_API_KEY=your_api_key
LOG_FILE = logs/app.log
```

### Start Application

```bash
uvicorn main:app --reload
```

### User Guide

##### 1. PDF Upload
###### Request Method : `POST`
###### Endpoint: `/v1/pdf`

###### Request
```bash
curl --location 'http://localhost:8000/v1/pdf' \
--form 'file=@"/C:/Users/{Username}/Downloads/SevenApps_Take_Home_Study_Case.pdf"'
```

###### Response

```json
{
    "message": "PDF uploaded successfully.",
    "file_id": "c993a901-6d38-497b-b789-5b9fd62242d9",
    "file_path": "storage/c993a901-6d38-497b-b789-5b9fd62242d9.pdf"
}
```

##### 2. Chat with PDF

###### Request Method : `GET`
###### Endpoint: `/v1/chat/{file_id}`
###### Parameter
- ```question```

###### Request

```bash
curl --location 'http://localhost:8000/v1/chat/c993a901-6d38-497b-b789-5b9fd62242d9?question=What%20is%20the%20main%20topic%20of%20this%20PDF%20'
```

###### Response

```json
{
    "answer": "The main topic of this PDF is linear classifiers in Python.  It covers topics such as dot products, prediction equations, the difference between the `fit` and `predict` methods in LogisticRegression, loss functions (including squared loss, 0-1 loss, and hinge loss), and how these concepts relate to linear classifiers.\n"
}
```

### Test Running

Go to main folder and run below command:

```bash
python -m unittest discover tests
```

