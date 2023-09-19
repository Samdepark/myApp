from django.contrib import admin
from Authentication.models import User

class UserAdmin(admin.ModelAdmin):
    list_display =['username', 'email',]
    

admin.site.register(User)
from .models import Item, OrderItem, Order

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
