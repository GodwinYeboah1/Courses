from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(req):
    context = {'courselist': Course.objects.all()}
    return render(req, "index.html",context)

def create(req):
    newcourse = Course.objects.create(name=req.POST['name'], desc=req.POST['desc'])
    newcourse.save()
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
