# Documentaton of Django
In Django we create new project and in that project we add multiple apps.
MVT(Model View Template) Architecture of Django
 >In one project we create  multiple apps. Differance between project and APP in Django
  in project there are multiple apps in order to make project fully functional we need to have at least one app
   
  

### First install Django: 
Check weather you have install python and pip 
```
pip install django 
```

## To create a new project:
Terminal
```
django-admin startproject hello
```
hello project will be created `cd` into the project you made.

 
 ## To start Server:
```
  python manage.py runserver
  ```
 
 ## Basic requirement for website html,css,js
 1. html -Skeleton
 2. css- looks
 3. js - functions
  
 
 

  ## What is Model ,View , Template ?
  
  https://www.onlinetutorialspoint.com/django/django-mvt-basic-application-example.html
  
  1. Model - Where the data will be stored its information
  2. View  _ It take info from database and sen it template
  3. Template- HTML,CSS,JS
   ---
  In order to add urls we need to edit urls.py   
  > location: project folder
  
 
   
   
   
   # To make app :
 
      python manage.py startapp home

    
 * A new app will be added and a new folder will be created  name as home in the folder you will find there is no urls.py
   you have to make urls.py*
> Whenever the request will be made it will go to urls.py then it will move forward
  
  __________________________________
  ## The steps we need to do after making app 
  1. Add urls.py
  2. copy code from the project urls.py and paste the code in the app urls.py it should look like this
```
  from django.contrib import admin
  from django.urls import path
```

urlpatterns = [
> This line tells whenever some one will come with a path/admin the directe them to admin.site.urls

    path('admin/', admin.site.urls),

  
  ___________________________________________
  
 1. Add 'from django.urls import path, include'  to the main folder urls.py 
  
 2. Then add a path in urls patterns
     path ('',include('home.urls')),
  
 3. Then the app urls.py from home import views
 4. path("",views.index,name='home') add some thing like this in app urlpatterns
 5. Now We have to make a function in views.py import HttpResponse
     
      Create your views here.
def index(request):
    return HttpResponse("this is home page")
    
 ___________________________________________   

## Make 2 folders in the main folder static and templates

  1. **Static**: keeps all the file that has to displayed directly
  2. **Temaplates** : It keeps all the file like html css and js 
   To add static to the site add this to the setting.py to add the static file
   ```
  STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]
```
  

A new  folder will be created  name as home in the folder yo will find there is no urls.py
you have to make urls.py