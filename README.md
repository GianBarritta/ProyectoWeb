# Project Web 🚀

_Website to manage orders, this application is made in order to practice with the Django framework._

## Starting 🚀

_These instructions will allow you to get a copy of the project running on your local machine for development and testing purposes._

Look **Deployment** to know how to deploy the project.


### Pre requirements 

_A series of step-by-step examples that tells you what to run to get a development environment running_

_Clone the repository_

```
git clone https://github.com/GianBarritta/ProyectoWeb.git && cd ProyectoWeb
```

_Create a virtual Python environment:_

```
python3 -m venv .venv
```

_Activate the virtual environment_

```
sorce .venv/bin/activate
```

### Installation 🔧

_What things do you need to install the software and how to install them_
_You can install the requirements.txt file recursively_
```
pip install requirements.txt
```

## Running the tests ⚙️

_Create database from models_

```
python3 manage.py makemigrations
python3 manage.py migrate
```

```
python3 manage.py runserver
```