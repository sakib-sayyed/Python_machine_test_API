from django.contrib import admin
from .models import Clients,Projects

@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id','client_name','created_at','created_by']

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','client','created_at','created_by']
    

# Super user username = 'sakib'
# Super user Password = '1234'