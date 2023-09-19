from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,DetailView,View
from django.utils import timezone
from .forms import CheckoutForm
from .models import Item, OrderItem, Order, BillingAddress

#items view
def products(request):
    context ={
        'items': Item.objects.all()
    }
    return render (request, "products.html", context)

#checkout page
class CheckoutView(View):
    def get(self, *argz, **kwargs):
        form = CheckoutForm
        context = {
            'form' : form
        }
        return render(self.request, "checkout.html", context)
    def post(self,*args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = order.objects.get(user = self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                #TODO: Add functionality for the field
                # same_shipping_address = form.cleaned_data.get("same_shipping_address")
                # save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')
                billing_address = BillingAddress(
                    user = self.request.user,
                    street_address = street_address,
                    apartment_address = apartment_address,
                    country = country,
                    zip = zip
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                #TODO:add a redirect to the selected payment address
                return redirect('Authentication:checkout')
            messages.warning(self.request, 'Failed checkout')
            return redirect('Authentication:checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, 'You dont have any Active Order')
            return redirect('Authentication:order-summary')
    

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, order=False)
            context = {
                'object': order
            }
            return render(self.request , 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, 'You dont have any Active Order')
            return redirect('/')
        


#homeView page
class HomeView(ListView):
    model = Item

    template_name = 'home.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"

#Adding items to the cart function
@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs= Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if item order is in proper order
        if order.items.filter(items__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, 'quantity updated')
        else:
             messages.info(request, 'item added to cart')
             order.items.add(order_item)
    else:
        order_date = timezone.now()
        order = Order.objects.create(user = request.user, 
                                         ordered_date = order_date)
        order.items.add(order_item)
        messages.info(request, 'Item added to Cart')
    return redirect("Authentication:product", slug=slug)

#delete items in the cart function
@login_required
def remove_from_cart(request, slug):
        item = get_object_or_404(Item, slug=slug)
        order_qs= Order.objects.filter(
            user=request.user, 
            ordered=False
            )
        if order_qs.exists():
            order = order_qs[0]
            #check if item order is in proper order
            if order.items.filter(items__slug=item.slug).exists():
                order_item = OrderItem.objects.filter(
                    item=item,
                    user=request.user,
                    ordered=False
                )[0]
                order.items.remove(order_item)
                messages.info(request, 'Item removed from cart')
                return redirect("core:order-summary")
            else:
                messages.info(request, 'Item not available in Cart')
                return redirect("core:product", slug=slug)
        else:
            messages.info(request, 'No Active Orders')
            return redirect("core:product", slug= slug)

@login_required
def remove_single_item_from_cart(request, slug):
        item = get_object_or_404(Item, slug=slug)
        order_qs= Order.objects.filter(
            user=request.user, 
            ordered=False
            )
        if order_qs.exists():
            order = order_qs[0]
            #check if item order is in proper order
            if order.items.filter(items__slug=item.slug).exists():
                order_item = OrderItem.objects.filter(
                    item=item,
                    user=request.user,
                    ordered=False
                )[0]
                if order_item.quantity > 1:
                    order_item.quantity -= 1
                    order_item.save()
                else:
                    order.items.remove(order_item)
                messages.info(request, 'Removed')
                return redirect("core:order-summary")
            else:
                messages.info(request, 'Item not available in Cart')
                return redirect("core:product", slug=slug)
        else:
            messages.info(request, 'No Active Orders')
            return redirect("core:product", slug=slug)