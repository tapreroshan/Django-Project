from django.shortcuts import render

from django.views.generic import ListView
from .models import  ServiceUser,Subscription,Services
# from .forms import Subscription

# Create your views here.
class UserList(ListView):
    model = ServiceUser
    template_name = 'manager/userlist.html'
    context_object_name ='user'
def userlist(request):
    user = ServiceUser.objects.all()
    return render(request, 'manager/userlist.html', {'user':user})

def user_detail(request, id):
    user = ServiceUser.objects.get(pk=id)
    subscription = Subscription.objects.filter(user=user)
    return render(request, 'manager/userdetail.html',{'user':user,'subscription':subscription})
class ServiceListView(ListView):
    model = Services
    template_name = 'service_list.html'
    context_object_name ='service'
def service_detail(request):
    services= Services.objects.filter(type=type)
    services= Services.objects.all()
    return render(request, 'service_detail.html', {'service':services})