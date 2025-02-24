# Django-Flask-Project: REST API Integration

## Overview
This project is a Django-based web application that integrates Flask as a REST API to perform database operations. It utilizes two cloud databases:
- **AWS MySQL** for `accounts` table.
- **MongoDB Atlas** for `films` collection.

The project demonstrates how Django fetches data from these databases using Flask-based REST APIs.

## 1. Database Structure
### **Accounts Table (AWS MySQL)**
This table stores account details and is hosted on AWS Cloud MySQL.

```sql
CREATE TABLE accounts (
    accno INT PRIMARY KEY,
    accnm VARCHAR(20),
    acctype VARCHAR(15),
    balance FLOAT
);
```

### **Films Collection (MongoDB Atlas)**
This collection stores film details and is hosted on MongoDB Atlas.

```json
{
    "title": "Inception",
    "director": "Christopher Nolan",
    "genre": "Sci-Fi",
    "language": "English",
    "rating": 8.8,
    "releaseYear": 2010
}
```

## 2. Using Flask (REST API) in Django Project
Django communicates with Flask-based REST APIs to perform database operations.
- **Accounts data** is retrieved from the MySQL cloud database via a Flask API.
- **Films data** is retrieved from the MongoDB Atlas database via another Flask API.

## 3. Step-by-Step Code Execution
### **views.py**
```python
from django.shortcuts import render
from urllib import request as req
import json

def home(request):
    return render(request, "index.html")

def allfilmsrest(request):
    # This API fetches films data from MongoDB Atlas
    response = req.urlopen("http://127.0.0.1:7000/films/all")
    data = response.read()
    info = json.loads(data)
    context = {'info': info}
    return render(request, "Showallfilms.html", context)

def allaccrest(request):
    # This API fetches account data from AWS MySQL
    response = req.urlopen("http://127.0.0.1:5000/accounts/alldata")
    data = response.read()
    info = json.loads(data)
    context = {'info': info}
    return render(request, "Showallacc.html", context)

def searchaccno(request):
    if request.method == "POST":
        ano = request.POST.get("accno")
        response = req.urlopen(f"http://127.0.0.1:6000/accounts/accno/{ano}")
        data = response.read()
        info = json.loads(data)
        context = {'info': info}
    return render(request, "showAccInfo.html", context)
```

### **urls.py**
```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('allfimsrest/', views.allfilmsrest),
    path('allaccrest/', views.allaccrest),
    path('searchaccno/', views.searchaccno)
]
```

## 4. Video Execution of the Project


https://github.com/user-attachments/assets/70c890dd-a8d6-4dad-9f9c-2f8645ca6225


To fully understand the project, watch the execution video that demonstrates:
- Fetching all films data from MongoDB.
- Fetching all account data from AWS MySQL.
- Searching for an account by account number.

## 5. Clone and Run the Project
### Step 1: Clone the Repository
```sh
git clone https://github.com/ARONAGENT/Flask-Django_Project.git
cd Django-Flask-Project
```

### Step 2: Install Dependencies
```sh
pip install django pymysql pymongo flask
```

### Step 3: Run Flask APIs
Start the Flask application handling database requests.
```sh
python flask_app.py
```

### Step 4: Run Django Application
```sh
python manage.py runserver
```

### Step 5: Access in Browser
Visit `http://127.0.0.1:8000/` to interact with the Django web application.

## Conclusion
This project showcases a hybrid approach to handling relational (SQL) and non-relational (NoSQL) databases using Flask-based REST APIs in a Django application.

