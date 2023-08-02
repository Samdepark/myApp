from django.contrib import admin
from Authentication.models import user

class UserAdmin(admin.ModelAdmin):
    list_display =['username', 'email',]
    

admin.site.register(user)
