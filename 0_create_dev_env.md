# Set Up Development Environemnt 

## 1. Create a Project Directory
```bash 
$ mkdir -p ~/Projects/RESTful_API && cd ~/Projects/RESTful_API
$ git init
$ git remote add originhttps://github.com/ZCHAnalytics/RESTful-API.git
$ git status
```

![alt text](images/image.png)

## 2. Create a Virtual Environment

### Create and activate a new python environment
`$ python -m venv rest_api_env`
`$ source rest_api_env/Scripts/activate`

### Install dependencies 
`$ pip install flask`

### Write a short test app script (app.py)

```bash
from flask import Flask
app = Flask(__name__)

```
### Run the app 
`$ flask run`

![alt text](images/image-1.png)

## 3. Start a Flask app in 'development' mode

### Create .flaskenv file  

```
# Environment variable style arguments

FLASK_APP=app
FLASK_DEBUG=1
```
### Install `python-dotenv` to manage environment variables

`$ pip install python-dotenv`

### Create .env for environment variables not related to Flask 

### Create .gitignore files and add .env to .gitignore 

## 4. Python library to connect with PostgreSQL database

`$ pip install psycorg2-binary`

## 5. Update gitignore file 

check gitignore status befiore committing:


![alt text](images/image-8.png)

## 5. Organise the Project:

### Create a separate directory for images
```bash
mkdir images  
mv image*.png images/
mv image.png images/
```

### Update the image paths in Markdown files manually
