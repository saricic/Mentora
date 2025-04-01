from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse






def mainpage(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def learnmorepage(request):
    template = loader.get_template('learn.html')
    return HttpResponse(template.render())

#def chatpage(request):
   # template = loader.get_template('chatbot.html')
   # return HttpResponse(template.render())


def clickButton(request):   
    if request.method == "POST":
        return redirect('chatpage')
    return render(request, 'chatbot.html')
    
# message works properly but the problem is about issuing the response to the
from django.http import JsonResponse
from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import render

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'hi hi hi'
        print(message)
        #return JsonResponse({'message': message, 'response': response})
 # please ensure this is executed for get requests.
    return render(request, 'chatbot.html', {'response': 'hi hi hi'})

