# Set Up Development Environemnt 

## 1. Create a Project Directory and initialise a Git repository 
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
- Install Flask freamework with `$ pip install flask`.

### Write a test app script (`app.py`)

```bash
from flask import Flask
app = Flask(__name__)

```
### Run the App 
`$ flask run`

![alt text](images/image-1.png)

## 3. Start Flask in Development Mode

### Create `.flaskenv` file  
- Configure development mode:

```
FLASK_APP=app
FLASK_DEBUG=1
```
### Install `python-dotenv` to manage environment variables

`$ pip install python-dotenv`

### Create `.env` file for environment variables not related to Flask 

### Create .gitignore file and add .env to .gitignore 

## 4. Install PostgreSQL connector

`$ pip install psycorg2-binary`

## 5. Update `.gitignore` file 

- Ensure the `.gitigmore` file is updated.

![alt text](images/image-8.png)

## 5. Organise the Project:

### Create a Directory for Images
Create a separate directory for images and move all image files to the new directory:
```bash
mkdir images  
mv image*.png images/
mv image.png images/
```

### Update the image paths in Markdown files manually
