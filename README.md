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
Now we are good to Go . We can check the [127.0.0.1:8000](http://127.0.0.1:8000) <br> for The root API documention.
<br>

<h2 align="center">Project Flow</h2>
<br>

#### Project Structure 
<br>

```bash 


    mainConfig (Root Config folder)/

        scripts (folder for custom scripts)/
            numbergenerate.py (
        settings/
            base.py (base settings)
            development ( development settings)
        models.py (init models file)
        urls.py (Root URL file)
        wsgi.py

    resource/ 
        init.json (init data)

    structure (All the APP will be under on it)/

        accounts/
            models (database folder)/        
            signals (signals folder)/
            views (Company Views folder)/
            test (Tesing Folder)/
            serializer.py (API file)
            urls.py (accounts URL file)
            admin.py

        company/
            models (database folder)/
            signals (signals folder)/
            views (Company Views folder)/
            test (Testing Folder)/
            serializer (API file)
            urls.py (company URL)
            admin.py

    .env
    .gitignore
    db
    requirements 
    

```
<br>


#### Customer  Module 
<br>

```bash 

    In Registration Customer 
        - Customer will be created with First Name , Last Name and Unique phone 
          Number generating on it. 
        - The Customer unique is their phone Number on the System
        - Customer will have a Wallet system based on their profile.
          So that they can buy plans from their wallet money.

```

#### Company Module 
<br>

```bash 

    Company Registration 
        - Company can be registered with their name 
        - Digitprefix ( example : 017,019,018)
        - Description 
        - ALL CRUD operations 

    Company Subscription 
        - Customer can register to any company.
        - Eeach time Customer register to a comapny , company will provide them 
          a Unque Phone number.
          (example : if a customer register with Grameen Phone Company then 
          the company will give the customer a grameen phone Number like - 0172453...  )


```
<br>

#### Plan Module 
<br>

```bash 

    Plan Registration 
        - Admin can add Plan to the system 
        - The fields are (plan name , Plan price , plan duration )
        - All CRUD operations included 
    
    Plan Subscription 
        - A customer can subscribe to any plan with only one unque 
        phone number , so there is no chance a customer can subscibe to 
        different plans with one number. Validation process is being implimented on the system. 
        - Customer cannot buy a plan unless they have enough money on their wallet. 
        - Wallet can refiled via payment method like sslCommerz/stripe . 
        - All CRUD operation included. 


```
<br>


#### Tracking Module 
<br>

```bash 

    - This modules is only for admin to track customer and their plans.
    - When a customer buy a plan a tracking with activated status will 
      generated in admin section with plan`s full details . 
    - And when a customer cancel a plan , a tracking with canceled status 
      will be generated in admin section also with plan`s full details.


```
<br>

#### Test Case 
<br>

```bash 

    All the URLs TestCase is inclued in each app testing folder

```
