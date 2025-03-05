from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# main page of our products app 
# by convention - use the word index for the main page of an app
# when we navigate to http://127.0.0.1:8000/products, our browser sends an http request to our webserver. django takes this request and sends it to our view function. thats why we need request parameter

# We need to tell django that whenever there is a request to /products call the index function
# We need to map the /products url to this function
# to do this add a new module 'urls.py' to products folder. naming of module is important. urls is a convention name that django framework defines, so we must follow this convention to structure our project.

def index(request): #with this request object we can find info about the client
    # return an http response object. we are creating an instance of the HttpResponse class
    return HttpResponse('Hello World')
