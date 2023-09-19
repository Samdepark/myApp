from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class  User(AbstractBaseUser):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Username', 'password']

    def __str__(self):
        return self.usernamesername
    
from django.conf import settings
from django.db import models
from django.shortcuts import reverse 
from django_countries.fields import CountryField

class Item(models.Model):
    title = models.CharField(max_length=150)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    # category= models.CharField(choices=CATEGORY_CHOICE, max_length = 4)
    # label = models.CharField(choices=LABEL_CHOICES, max_length =3)

    slug = models.SlugField()
    description= models.TextField()
    
    def __str__(self):
        return f"{self.item.quantity} of {self.item.title}"
    #Necesary for redirecting back to the sameproduct
    def get_absolute_url(self):
        return reverse("core:product", Kwargs={
            'slug':self.slug
        })
    def get_add_to_cart_url(self):
         return reverse("core:add-to-cart", Kwargs={
            'slug':self.slug
        })
    def get_remove_from_cart_url(self):
         return reverse("core:remove-from-cart", Kwargs={
            'slug':self.slug
        })
        


#orderItem model
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    order = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.IntegerField(default= 1)


    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    #get  the total item price in the cart
    def get_total_item_price(self):
        return self.quantity * self.item.price
    
    #get total discount price foor items in the cart
    def get_total_item_discount_price(self):
        return self.quantity * self.item.discount_price
    
    #get Amount saved on the discounted item
    def get_amount_saved(self):
        return self.get_total_item_price - self.get_total_item_discount_price
    
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_item_discount_price()
        return self.get_total_item_price()


#Order Model
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    items = models.ManyToManyField('Item', blank=True)

    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    ordered= models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        'BillingAddress', on_delete=models.SET_NULL, blank=True , null= True)
    
    def __str__(self):
        return self.user.username
#get the total price for all items in the cart
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
    
class BilingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=120)
    apartment_address = models.CharField(max_length=120)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=120)

    def __str__(self):
        return self.user.username