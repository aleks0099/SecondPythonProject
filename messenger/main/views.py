from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import SendMessageForm
from django.db import models
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

class Reg(View):
    template_name = 'registration/registration.html'

    def get(self, request):
        context = {
            'form': forms.UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

@login_required
def received(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'inbox.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('sent')
    else:
        form = SendMessageForm()
    return render(request, 'send_message.html', {'form': form})

@login_required
def sent(request):
    messages = Message.objects.filter(sender=request.user)
    return render(request, 'sent.html', {'messages': messages})


def message_detail(request, pk):
    message = Message.objects.get(pk=pk)
    return render(request, 'message_detail.html', {'message': message})