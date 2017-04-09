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
```

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


Upload API
----------
1. HTTP Post API
- Server accepts http Post call to url /upload
- Robot xml file can be uploaded from front page (not yet implemented)
- Send file using curl: "curl -F file=@file_name server_ip:server_port/upload"

Send robot output file directly to a path defined in settings.py file ROBOT_OUTPUT_PATH via scp for example.
- Server expects to receive robot output xml with unique name. Server uses uuid.uuid4 to generate unique name when using HTTP API.
- Info file (json file) that has the status of the file parsing and name of the output file.
Example info file 4123d203-17f5-470d-ad02-66388596ac9a.json:
```
{"status": "received", "output": "4123d203-17f5-470d-ad02-66388596ac9a.xml"}
```
Send files to server:
```
scp robot_results/4123d203-17f5-470d-ad02-66388596ac9a.json robot_results/4123d203-17f5-470d-ad02-66388596ac9a.xml username@remotehost:ROBOT_OUTPUT_PATH
```

