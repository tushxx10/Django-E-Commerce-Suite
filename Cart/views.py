from django.shortcuts import render, get_object_or_404, redirect 
from Products.models import Product  #importing product from Products model
from .models import Cart, CartItem
from django.views.decorators.http import require_POST
from django.http import JsonResponse

#for extra request we add @require POST which means it only accepts HTTP POST request
@require_POST

def cart_add(request, product_id):   #defining a method names cart_add
    cart_id = request.session.get('cart_id')

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
    else:
        cart = Cart.objects.create()        
        request.session['cart_id'] = cart.id

    product = get_object_or_404(Product, id=product_id)    

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:cart_item.quantity += 1

    cart_item.save()

    response_date = {
        "success":True,
        "message": f'Added {product.name} to cart' 
    }

    return JsonResponse(response_date)


# creating another method defining cart_detail

def cart_detail(request):
        cart_id = request.session.get('cart_id')
        cart=None

        if cart_id:
             cart = get_object_or_404(Cart, id=cart_id)
        if not cart or not  cart.items.exists():
             cart=None     

        return render(request, "cart/detail.html", {"cart":cart})   

def cart_remove(request, product_id):
     cart_id = request.session.get('cart_id')
     cart = get_object_or_404(Cart, id=cart_id)
     item = get_object_or_404(CartItem, id=product_id, cart=cart)
     item.delete()

     return redirect("cart:cart_detail")