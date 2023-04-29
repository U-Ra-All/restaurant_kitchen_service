# Restaurant Kitchen Service Project

Django project for managing restaurant kitchen with cooks, dishes and dish types

## Check it out!

[Restaurant kitchen project deployed to Render](https://restaurant-kitchen-project.onrender.com/)

## Installation

Python3 must be already installed

```shell
git clone https://github.com/U-Ra-All/restaurant_kitchen_service.git
cd restaurant_kitchen_service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver # starts Django Server
```

Create a file called .env in the same folder as the settings file. 
Make sure to have the following development-specific values in there.

```shell
SECRET_KEY = "Your_Super_Secret_Key"
```

You can use the following superuser (or create another one by yourself):

```shell
Login: admin.user
Password: 7QancRe2
```

## Features

* Authentication functionality for Cook/User
* Managing cooks, dishes and dish types directly from website interface
* Powerful admin panel for advanced managing
