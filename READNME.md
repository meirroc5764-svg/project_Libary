# System description
The system manages the library and receives requests from the client only via HTTP. The system will have several tables in the Database, each of which is responsible for a different aspect of the library.


# Code to create docker with MySql
docker run --name Libary-Project -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=Libary_db -p 3306:3306 -d mysql:8


# Folder structure
library-api/  
│  
├── app/  
│   ├── main.py  
│   ├── database/  
│   │   ├── db\_connection.py  
│   │   ├── book\_db.py  
│   │   └── member\_db.py  
│   ├── routes/  
│   │   ├── book\_routes.py  
│   │   ├── member\_routes.py  
│   │   └── report\_routes.py  
│   └── logs/  
│       └── app.log  
│  
├── README.md  
├── requirements.txt  
└── .gitignore


# Table structure

## table books
--------------------
- **id** = Primary Key, INT
-----------------------
- **title** =  Title of the book, non-empty column maximum 50 characters varchar(50)
---------------------
- **author** = Author's name, non-empty column, maximum 50 characters varchar(50)
------------------------
- **genre** = Allowed genre values:
Implemented — Fiction | Non-Fiction | Science | History | Other
As an ENUM column in the database, any other value returns an error,  Non-empty column,not null
------------------------------
- **is_available** = Is the book available for borrowing — FALSE Indicates borrowed, Non-empty column,not null
-------------------------------
- **borrowed_by_member_id** =  ID of the member who owns the book — NULL if available
================================

## table members
--------------------
- **id** = Primary key, INT
------------------
- **name** = Membername, non-emptycolumn,maximum 50  characters varchar(50)
------------------ 
- **email** = Email address — unique, non-empty column, not null
---------------------
- **is_active** = Is the member active — FALSE Cannot borrow, Non-empty column, not null
---------------------------
- **total_borrows** = Total number of questions — increments by 1 for each question, Non-empty column
------------------------------

# System rules
## rule 1
- **Creating a book** 
User sends genre/author/title — the system adds
is_available=True, borrowed_by=NULL
-------------------
## rule 2
- **genre**
must be a — Fiction / Non-Fiction / Science / History / Other  
Any other value returns an error
Must verify both in addition (POST) and in update (PATCH)
-------------------------------
## rule 3 
- **Creating a friend** 
User sends email/name — the system adds True=active_is,
total_borrows=0
-------------------
## rule 4
- **Email** 
 must be unique — if already exists returns an error
----------------------
## rule 5 
- **Inactive friend** 
if False=active_is — Cannot borrow a book
--------------------------
## rule 6 
- **Book is unavailable** 
Cannot borrow a book that has already been borrowed (False=available_is)
---------------------------
## rule 7 
- **Maximum Books**
A friend cannot hold more than 3 books at a time
----------------------------
## rule 8 
- **Returning a book** 
A book can only be returned if it is lent to the same friend who is returning it
------------------------------------


# Endpoints list

## Books

POST | /books | Create a book
-----------------
GET | /books | All books
----------------
GET | /books/{id} | Book by ID
-------------------------
PUT | /books/{id} | Update a book
-------------------
PUT | /books/{id}/borrow/{member_id} | Lend a book to a friend
-----------------------------
PUT | /books/{id}/return/{member_id} | Return a book to a friend
-----------------------------

## members
POST | /members | Create a friend
---------------------
GET | /members | All friends 
-------------------
GET  | /members/{id} | By friend
------------------------
PUT |/members/{id} | Update friend
---------------------------
PUT | /members/{id}/deactivate | Disable friend
-------------------------------
PUT | /members/{id}/activate |Activate friend
------------------------------------

## Reports
GET | /reports/summary | General Report 
GET | /reports/books-by-genre | Books by Genre
GET | /reports/top-member | Most Active Member

# System flow
The system waits for a request from the client; after receiving the request, depending on the request, the request is sent from the router to the function, which in turn opens the database and retrieves or returns information.


# Run instructions


## Create a container in docer

### type in cmd
docker run --name Libary-Project\
-e MYSQL_ROOT_PASSWORD=root \
-e MYSQL_DATABASE= Libary\
-p 3306:3306 \
-d mysql:8


## Install the settings from the requaimer.txt file
open terminal  - 
pip install py -m venv venv
venv\Scripts\activate
pip install requaimer.txt

## Get the code from Git
### ripo:
https://github.com/meirroc5764-svg/project_Libary#
### copy:
https://github.com/meirroc5764-svg/project_Libary.git

## open vs code or pycharm
Run the file main.py
first - create a database