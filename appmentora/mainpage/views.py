from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def mainpage(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def learnPage(request):
    return render(request, 'learn.html')

def chatButton(request):
    # Add logic for the chat button action
    return render(request, 'chat.html')
