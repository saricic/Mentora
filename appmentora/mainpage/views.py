from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm



def mainpage(request):
    template = loader.get_template('main.html')
    print(f"User authenticated: {request.user.is_authenticated}")
    return render(request, 'main.html')
def learnPage(request):
    return render(request, 'learn.html')

def chatButton(request):
    # Add logic for the chat button action
    return render(request, 'chat.html')

def loginbutton(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Perform login logic here
        pass
    return render(request, 'login.html', {'form': form})