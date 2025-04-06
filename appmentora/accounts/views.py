from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("loginbutton")
    template_name = "register.html"