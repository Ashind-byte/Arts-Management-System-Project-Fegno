from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_control

from django.views.generic import TemplateView, RedirectView

from Events.models import Winner
from .forms import UserForm

@login_required
def home(request):

    return render(request,'index.html',)






def signup(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})




class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')



class MyLoginView(LoginView):

    template_name = 'adminlte/login.html'
    next_page = '/'

