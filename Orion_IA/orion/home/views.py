from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    usuario = ''
    senha = ''

    if request.method == 'POST':
        usuario = request.POST.get('user')
        senha = request.POST.get('password')

        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            login(request, user)
            
            if user.is_superuser:
                return redirect('chatbot')
            else:
                return redirect('index')

    return render(request, 'core/index.html')

@login_required
def chatbot(request):
    return render(request, 'core/chatbot.html')