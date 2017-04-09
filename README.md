Robot Framework History
=======================
Robot Framework history is a tool that provides web service to record and
manage test automation history.

Requirements
------------
- Python3
- Django 1.10 or newer

How to setup development environment
-------------------------------------
It is recommended to use virtualenv so your installed python packages
doesn't interfere development for current project

Install virtualenv and take new environment to use
```
$ pip install virtualenv
$ virtualenv --python=python3 env
$ source env/bin/activate
```

Install Django
```
$ pip install django
```

To stop the current virtualenv sessions
```
$ deactivate

Visual Studio build
-------------------
Clone repository with repository name. The project name has to match the 
name of the development folder.

In visual studio add python tools.

1. Create new project
- Add existing project (same name as the repository)
- Customise the project type as Django project
2. Add new virtual environment
- From solution explorer under the project select add new virtual environment
from python environments
- All needed packages are automatically added
3. Test that project runs
- From project tab select run server
- Goto: http://127.0.0.1:8000/RFHistory/
- Hello message printed to browser
