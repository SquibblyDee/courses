from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

#  import our db
from .models import Course

def index(request):
    # Index page just pulls and returns a query
    query = Course.objects.values('id', 'name', 'desc', 'created_at')
    return render(request,'courses_app/index.html', {'query' : query})

def destroy(request, id):
    # Index page receives id and displays delete page
    query = Course.objects.filter(id=id)
    return render(request,'courses_app/destroy.html', {'query' : query})

def processdestroy(request, id):
    # Deletes the row of the id that is passed in as a var and print success massage to server 
    Course.objects.get(id=id).delete()
    return redirect('/')

def process(request, methods=['POST']):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Course.objects.basic_validator(request.POST)
    # check if the errors object has anything in it
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
            print("WEVE HIT AN ERROR")
        # redirect the user back to the form to fix the errors
        return redirect('/', id)
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the table to be updated, make the changes, and save
        #build our values for the name and email keys
        name = request.POST['name']
        desc = request.POST['desc']
        #write values to our User tables
        Course.objects.create(name=name, desc=desc)
        messages.success(request, "User table successfully updated")
        # redirect to a success route
        return redirect('/')

