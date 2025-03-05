from django.urls import path
from .import views      #. means current folder. from current folder import views
# import views          # we dont do it this way bc views is a generic name, our project may have a depndancy to another library called views. with this syntax, python will imort that module instead of the one in our current folder because it will take priority.

# By convention we should define a variable called urlpatterns. spell exactly as seen here. set this equl to a list, and within this list we will map various urls to their view functions. to reference a url we need to import a path function

# path arguments
# - First Arg: String that specifies our url endpoint. Pass Empty string to represent the root of this app.
# For instance our app starts at /products. If the user sends a request to this endpoint they will be a the root of this app. but we could have more urls like /products/1/detail or /products/new or /products/trending. back to /products, if we take away /products we are left with nothing, thats why we use an empty string here
# - Second Arg: Specify our view function. its in our view.py module. so we will import that here. we are not calling the index function, we are only passing reference to it.
# remember when we import a module, that module acts as an object. so we can now do:
# "views." to access functions defined in that module


# our pyShop app also has a urls module. this is like the parent urls module in out django project. we need to tell django pyshop app about our products app so go to pyshop/urls

urlpatterns=[
    path('', views.index)       #map root url to index function in views module
]