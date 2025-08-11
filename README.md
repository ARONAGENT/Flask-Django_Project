# Django-Flask Project: REST API Integration

[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![Flask](https://img.shields.io/badge/Flask-3.x-blue.svg)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.x-yellow.svg)](https://www.python.org/)
[![AWS MySQL](https://img.shields.io/badge/AWS-MySQL-orange.svg)](https://aws.amazon.com/rds/mysql/)
[![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-Cloud-brightgreen.svg)](https://www.mongodb.com/atlas)
[![REST API](https://img.shields.io/badge/REST-API-red.svg)](https://restfulapi.net/)
[![Microservices](https://img.shields.io/badge/Architecture-Microservices-purple.svg)](https://microservices.io/)

## 📋 Project Overview

This innovative project demonstrates a **hybrid microservices architecture** where **Django** serves as the main web application framework while **Flask** powers multiple REST APIs for database operations. The system integrates two different cloud databases - **AWS MySQL** for relational data and **MongoDB Atlas** for document-based storage, showcasing how modern applications can leverage both SQL and NoSQL databases simultaneously.

## 🏗️ Architecture Overview

```
┌─────────────────┐    HTTP Requests    ┌─────────────────┐
│                 │ ──────────────────► │                 │
│   Django Web    │                     │   Flask APIs    │
│   Application   │ ◄────────────────── │   (Port 5000,   │
│   (Port 8000)   │    JSON Responses   │    6000, 7000)  │
└─────────────────┘                     └─────────────────┘
         │                                        │
         │                                        │
         ▼                                        ▼
┌─────────────────┐                     ┌─────────────────┐
│                 │                     │                 │
│   Frontend UI   │                     │   Database      │
│   (Templates)   │                     │   Operations    │
└─────────────────┘                     └─────────────────┘
                                                 │
                        ┌────────────────────────┼────────────────────────┐
                        │                        │                        │
                        ▼                        ▼                        ▼
               ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
               │                 │    │                 │    │                 │
               │   AWS MySQL     │    │  MongoDB Atlas  │    │   Future DBs    │
               │   (Accounts)    │    │    (Films)      │    │   (Scalable)    │
               └─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🎬 Demo Video

https://github.com/user-attachments/assets/70c890dd-a8d6-4dad-9f9c-2f8645ca6225

*Complete demonstration of Django-Flask integration with dual database operations!*

## ✨ Key Features

### Core Functionality
- 🏦 **Account Management** - View and search bank accounts (AWS MySQL)
- 🎬 **Film Catalog** - Browse movie collection (MongoDB Atlas)
- 🔍 **Advanced Search** - Account lookup by account number
- 🌐 **REST API Integration** - Flask microservices for data operations
- 📱 **Responsive Design** - Modern web interface

### Technical Architecture
- **Microservices Pattern** - Separate Flask APIs for different databases
- **Multi-Database Support** - SQL and NoSQL in one application
- **Cloud Integration** - AWS RDS MySQL + MongoDB Atlas
- **RESTful Communication** - JSON-based API interactions
- **Scalable Design** - Easy to add new databases/services

## 🛠️ Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django** | 5.x | Main Web Framework |
| **Flask** | 3.x | REST API Microservices |
| **Python** | 3.x | Backend Language |
| **AWS MySQL** | 8.x | Relational Database |
| **MongoDB Atlas** | 7.x | NoSQL Database |
| **PyMongo** | 4.x | MongoDB Python Driver |
| **PyMySQL** | Latest | MySQL Python Driver |
| **Bootstrap** | 5.x | UI Framework |

## 🗄️ Database Schemas

### 1. Accounts Table (AWS MySQL)
```sql
CREATE TABLE accounts (
    accno INT PRIMARY KEY,
    accnm VARCHAR(20),
    acctype VARCHAR(15),
    balance FLOAT
);
```

**Sample Data:**
| accno | accnm | acctype | balance |
|-------|-------|---------|---------|
| 1001 | John Smith | Savings | 25000.50 |
| 1002 | Jane Doe | Current | 15000.75 |

### 2. Films Collection (MongoDB Atlas)
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

**Document Structure:**
| Field | Type | Description |
|-------|------|-------------|
| `title` | String | Movie title |
| `director` | String | Film director |
| `genre` | String | Movie genre |
| `language` | String | Film language |
| `rating` | Float | IMDb rating |
| `releaseYear` | Integer | Release year |

## 🔗 API Architecture

### Flask Microservices (Different Ports)

#### 1. **Accounts API (Port 5000 & 6000)**
```python
# Get all accounts
GET http://127.0.0.1:5000/accounts/alldata

# Search account by number  
GET http://127.0.0.1:6000/accounts/accno/{account_number}
```

#### 2. **Films API (Port 7000)**
```python
# Get all films
GET http://127.0.0.1:7000/films/all
```

### Django API Integration
```python
def allaccrest(request):
    """Fetch accounts from AWS MySQL via Flask API"""
    response = req.urlopen("http://127.0.0.1:5000/accounts/alldata")
    data = response.read()
    info = json.loads(data)
    context = {'info': info}
    return render(request, "Showallacc.html", context)

def allfilmsrest(request):
    """Fetch films from MongoDB Atlas via Flask API"""
    response = req.urlopen("http://127.0.0.1:7000/films/all")
    data = response.read()
    info = json.loads(data)
    context = {'info': info}
    return render(request, "Showallfilms.html", context)

def searchaccno(request):
    """Search specific account by account number"""
    if request.method == "POST":
        ano = request.POST.get("accno")
        response = req.urlopen(f"http://127.0.0.1:6000/accounts/accno/{ano}")
        data = response.read()
        info = json.loads(data)
        context = {'info': info}
    return render(request, "showAccInfo.html", context)
```

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.8+**
- **AWS Account** (for RDS MySQL)
- **MongoDB Atlas Account** (Free tier)
- **Git**
- **Code Editor** (VS Code recommended)

### Step-by-Step Installation

#### 1. **Clone the Repository**
```bash
git clone https://github.com/ARONAGENT/Flask-Django_Project.git
cd Flask-Django_Project
```

#### 2. **Create Virtual Environment**
```bash
# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux  
source venv/bin/activate
```

#### 3. **Install Dependencies**
```bash
pip install django
pip install flask
pip install pymongo
pip install pymysql
pip install flask-cors
pip install requests
```

#### 4. **Configure Database Connections**

**AWS MySQL Configuration:**
```python
# Flask API configuration
import pymysql

def get_mysql_connection():
    connection = pymysql.connect(
        host='your-aws-rds-endpoint.amazonaws.com',
        user='your-username',
        password='your-password',
        database='your-database-name',
        port=3306
    )
    return connection
```

**MongoDB Atlas Configuration:**
```python
# Flask API configuration
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://username:password@cluster.mongodb.net/database?retryWrites=true&w=majority"

def get_mongo_collection():
    client = MongoClient(MONGODB_URI)
    database = client['your_database']
    collection = database['films']
    return collection
```

#### 5. **Run the Applications**

**Terminal 1 - Start Flask APIs:**
```bash
# Start Flask microservices
python flask_accounts_api.py    # Port 5000
python flask_accounts_search.py # Port 6000  
python flask_films_api.py       # Port 7000
```

**Terminal 2 - Start Django Application:**
```bash
python manage.py runserver      # Port 8000
```

#### 6. **Access the Application**
Visit `http://127.0.0.1:8000/` to interact with the web interface.

## 📁 Project Structure
<img width="364" height="705" alt="image" src="https://github.com/user-attachments/assets/60627ef0-3479-470d-9ab7-016d2dc7b421" />

## 🔗 API Endpoints

### Django Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Home page |
| `GET` | `/allfimsrest/` | Display all films via Flask API |
| `GET` | `/allaccrest/` | Display all accounts via Flask API |
| `POST` | `/searchaccno/` | Search account by number |

### Flask API Endpoints
| Service | Port | Endpoint | Database | Purpose |
|---------|------|----------|----------|---------|
| Accounts API | 5000 | `/accounts/alldata` | AWS MySQL | Get all accounts |
| Search API | 6000 | `/accounts/accno/<id>` | AWS MySQL | Search by account number |
| Films API | 7000 | `/films/all` | MongoDB Atlas | Get all films |


## 👥 Authors & Contributors

- **[ARONAGENT](https://github.com/ARONAGENT)** - Project Creator & Maintainer

## 🙏 Acknowledgments

- **Django Community** - For the robust web framework
- **Flask Team** - For the lightweight API framework
- **AWS** - For reliable cloud database hosting
- **MongoDB Atlas** - For excellent NoSQL cloud services
- **PyMongo & PyMySQL Teams** - For excellent database drivers
- **Open Source Community** - For continuous inspiration

## 📞 Support & Contact

### Getting Help
- 📖 **Documentation**: Check this README first
- 🐛 **Bug Reports**: [Create an Issue](https://github.com/ARONAGENT/Flask-Django_Project/issues)
- 💡 **Feature Requests**: [Suggest Features](https://github.com/ARONAGENT/Flask-Django_Project/issues)
- 💬 **Questions**: [Start a Discussion](https://github.com/ARONAGENT/Flask-Django_Project/issues)

### Connect with the Developer
- **GitHub**: [@ARONAGENT](https://github.com/ARONAGENT)
- **LinkedIn**: [Connect for professional inquiries](https://www.linkedin.com/in/aronagent/)

## 🎯 Learning Outcomes

This project demonstrates:
- **Microservices Architecture** implementation
- **Multi-database integration** strategies
- **REST API design** and consumption
- **Cloud database** connectivity
- **Django-Flask hybrid** applications
- **SQL and NoSQL** database operations
---

⭐ **If you find this project helpful, please give it a star!** ⭐

*Built with ❤️ using Django, Flask, and modern cloud database technologies*
