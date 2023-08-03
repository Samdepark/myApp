from django.contrib import admin
from Authentication.models import User

class UserAdmin(admin.ModelAdmin):
    list_display =['username', 'email',]
    

admin.site.register(User)
