# Restaurant Kitchen Service Project

Django project for managing restaurant kitchen with cooks, dishes and dish types

## Check it out!

[Restaurant kitchen project deployed to Render](PASTE_LINK_HERE)

## Installation

Python3 must be already installed

```shell
git clone https://github.com/U-Ra-All/restaurant-kitchen-service.git
cd restaurant_kitchen_service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py runserver # starts Django Server
```

Create a file called .env in the same folder as the settings file. 
Make sure to have the following development-specific values in there.

```shell
SECRET_KEY = "Your_Super_Secret_Key"
```

Install dotenv to read the contents 
of this file into environment variables.

```shell
pip install python-dotenv
```

Edit the settings.py file to contain the following. 
Notice that I prepend the setting names with the APPNAME_ 
to avoid potential conflicting names.

```shell
from dotenv import load_dotenv
# Load sensitive environment-specific settings from .env file
# Does not override existing System variables by default.
# To override, use load_dotenv(override=True)
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

# ... rest of settings.py
```

## Features

* Authentication functionality for Cook/User
* Managing cooks, dishes and dish types directly from website interface
* Powerful admin panel for advanced managing
