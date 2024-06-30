from django.contrib import admin
from .models import Services, ServiceUser, Subscription


class ServiceUserAdmin(admin.ModelAdmin):
    search_fields = ['name','email']
    list_filter = ['gender']
admin.site.register(ServiceUser, ServiceUserAdmin)
admin.site.register(Services)
admin.site.register(Subscription)

# Register your models here.
