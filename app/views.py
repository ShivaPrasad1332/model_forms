from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *
def insert_topic(request):
    form=TopicForm()
    d={'form':form}
    if request.method=='POST':
          form_data=TopicForm(request.POST)
          if form_data.is_valid():
                form_data.save()
                return HttpResponse('model is saved by modelforms')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    form=WebpageForm()
    d={'form':form}
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if  form_data.is_valid():
            form_data.save()
            return HttpResponse('Webpage model is saved by modelforms')

    return render(request,'insert_webpage.html',d)


def insert_access(request):
    form=AccessForm()
    d={'form':form}
    if request.method=='POST':
        form_data=AccessForm(request.POST)
        if  form_data.is_valid():
            form_data.save()
            return HttpResponse('Access model is saved by modelforms')

    return render(request,'insert_access.html',d)
