from django.shortcuts import render

from django.views.generic import ListView
from .models import Services,ServiceUser,Subscription

# Create your views here.
class UserList(ListView):
    model = ServiceUser
    template_name = 'manager/userlist.html'
    context_object_name ='user'
def user_detail(request, id):
    user = ServiceUser.objects.get(pk=id)
    subscription = Subscription.objects.filter(user=user)
    return render(request, 'manager/userdetail.html',{'user':user,'subscription':subscription})
class s
