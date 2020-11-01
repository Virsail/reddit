# instagram

[virsail mbagaya](https://github.com/virsail)  
  
# Description  
This is a clone of  Instagram that allows users to upload their  images ,follow other users like others users pictures and leave comments ,users also sign up and get to search for their followers.

##  Live Link  
 View App site [View Site]()  
  
 
## User Story  
  
* Sign up and login to the application  
* Upload their pictures to the application
* Search for different users 
* See their profile with all their pictures they uploaded
* Follow other users and see their activities on my timeline.  
  

  
## Setup and Installation  
Clone the repository
##### Cloning the repository:  
 ``` git clone 
 https://github.com/Virsail/Instagram.git 
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
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 1.11.7](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Contact Information   
ericmbagaya@gmail.com 
  

### License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) 
* Copyright (c) 2020 **Virsail Mbagaya**