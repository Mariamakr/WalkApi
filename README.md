# WalkApi
https://github.com/Mariamakr/WalkApi


# 1 Create the api:
Create a folder 
Create venv
Activate
pip install django
pip install djangoframework
django-admin startproject walk .
django-admin startapp api
create urls.py inside api
create second path inside walk-urls.py
complete settings.py 
py manage.py migrate
py manage.py runserver
py manage.py createsuperuser
import router to api-urls.py

# 2 Create the models:

create class Place (which specifies the specific place the user will go)
create class Rating (where the users will rate the xp)
create a serializers.py
and then add the serializers we created into views.py using the viewset func from django
create router.register for fixing the urls levels

# 3 Testing with postman:
go to http://127.0.0.1:8000/api/places/
and to http://127.0.0.1:8000/api/ratings/

also test the usage of router e.x. http://127.0.0.1:8000/api/places/1/ for specific recordings

finally we can check if every method is functional (get, post, put , delete)

everything ok!

# 4 Custom create and update for ratings:
make the changes to views.py
create a try-except in which if there is not a rating it creates one.

test with Postman

# 5 Create optimization for ratings:
i want to display the avarage rating i have for a specific place .
I go to models and i insert a function for counting the ratings for the specific place
and then i include the number of ratings into the serializer
Then i do the classic method for average... where i check if i have 0 
and i insert the avg rating to serializer

# 6 Allow users to log in:
use token authentication fro rest_framework
setting.py -> rest_framework.authtoken
migrate
then i do to admin/ and create a token for admin


urls.py/walk include path with obtain auth token.

Here we can test to postman that ONLY if i put username and password to http://127.0.0.1:8000/auth (post) i get the token and then if i put Authorization adn as the value: Token the_token_provided i get the data i requested from http://127.0.0.1:8000/api/places/


Important!!
i must tell that the view will use user data so i 
dont have this error  "Rating.user" must be a "User" instance.

# 7 Create a User ViewSet based on that user:

Once i create UserSerializer and import the router inside the urls.py i can test to postman:
http://127.0.0.1:8000/api/users
it brinks the users

if i want to appear the normal password and not the hash i have to:

override the built-in function for create 

# 8 Login with a new User:
Secure the app 
setting.py : REST_FRAMEWORK ={
    'DEFAULT_PERMISSION_CLASSES':{
        'rest_framework.permission.IsAuthenticated'
    }
}
