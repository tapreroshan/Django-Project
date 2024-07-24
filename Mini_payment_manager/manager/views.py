from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ServiceUser, Subscription, Services
from .forms import ServiceForm
# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'manager/register.html', {'form': form})

# User login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/users')
    else:
        form = AuthenticationForm()
    return render(request, 'manager/login.html', {'form': form})

# User logout view
def logout_view(request):
    logout(request)
    return redirect('/')

# List view for users
@login_required
def userlist(request):
    user = ServiceUser.objects.all()
    return render(request, 'manager/userlist.html', {'user': user})

# Detail view for a specific user
@login_required
def user_detail(request, id):
    user = ServiceUser.objects.get(pk=id)
    subscription = Subscription.objects.filter(user=user)
    return render(request, 'manager/userdetail.html', {'user': user, 'subscription': subscription})

# List view for services using class-based view
class ServiceListView(LoginRequiredMixin, ListView):
    model = Services
    template_name = 'manager/service_list.html'
    context_object_name = 'service'

# Detail view for a specific service
@login_required
def service_detail(request):
    services = Services.objects.all()
    return render(request, 'service_detail.html', {'service': services})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')  
    else:
        form = ServiceForm()
    return render(request, 'manager/add_service.html', {'form': form})