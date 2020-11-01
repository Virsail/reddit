# reddit

[virsail mbagaya](https://github.com/virsail)  
  
# Description  
A clone of Awwards website  that allows user to post a website and get ratings for it ,a user is also able to rate other websites from different users .You get to choose whether to visit the website of interest this application is built on Python and Django framework.

##  Live Link  
 View App site [View Site]()  
  
 
## User Story  
As a user I would like to:
* View posted projects and their details
* Post a project to be reviewed
* Rate or review other users' projects
* Search for a project 
* View projects overall score
* View my profile page   
  

  
## Setup and Installation  
Clone the repository from github 
##### Cloning the repository:  
 ``` git clone 
 https://github.com/Virsail/reddit.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd instagram then pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  

 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations insta
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### debug your model classes
```
python3.8 manage.py check 
this is the fastest way to debug/check your model classes
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 1.11.7](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* HTML
* CSS
* JS
  
  
## Contact Information   
ericmbagaya@gmail.com 
  

### License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) 
* Copyright (c) 2020 **Virsail Mbagaya**