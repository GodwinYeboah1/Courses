from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

# Create your views here.
def index(req):
    context = {'courselist': Course.objects.all()}
    return render(req, "index.html",context)

def create(req):
    # i want to validate the data
    errors = Course.objects.validate(req.POST)
    # if error error out a message
    if len(errors):
        for key, value in errors.items():
            messages.error(req, value)
        return redirect('/')
    else:
    # if not save user 
        Course.objects.create_course(req.POST)
        
    return redirect('/')


def destory(req,id):
    if req.method == "GET":
        context = {'delete_course': Course.objects.get(pk=id)}
        return render(req,'delete_page.html', context)
    else:
        if req.method == "POST":
            delete_course = Course.objects.get(pk=id)
            delete_course.delete()
        return redirect('/')
