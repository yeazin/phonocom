<h1 align="center"> PhonoCom Backend </h1><br>
<h6 align="Center">

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
 [![git](https://badgen.net/badge/icon/git?icon=git&label)](https://git-scm.com) [![Visual Studio](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://visualstudio.microsoft.com) 

</h6>

<br>

<h4 align="center">
<a href="https://github.com/yeazin/phonocom#-project-installation-"> Project Installation</a> | 
<a href="https://github.com/yeazin/phonocom#project-flow"> Project Flow </a>
</h4>

<br>


<h2 align="center"> Project Installation </h2>
<br>

#### Clone the repository using the following command

```bash
git clone https://github.com/yeazin/phonocom.git
# After cloning, move into the directory 
# having the project files 
```
#### Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python3 -m venv env
```
#### Activate the virtual environment

```bash

# Windows
env\Scripts\activate.bat

# Linux and Mac
source env/bin/activate

```
#### Install all the project Requirements

```bash

pip install -r requirements.txt

```
#### Apply migrations and create your superuser (follow the prompts)

```bash

# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser

```
#### Load inital data to database <br>
check here for more info for [Resource Data](https://github.com/yeazin/phonocom/tree/main/resource#-resource-data-) <br>
Inital Data : 

```bash

# load inital data
python manage.py loaddata resource/init.json

```

#### Run the development server

```bash
# run django development server
python manage.py runserver

```
Now we are good to Go . We can check the [127.0.0.1:8000](127.0.0.1:8000) <br> for The root API documention.
<br>

<h2 align="center">Project Flow</h2>