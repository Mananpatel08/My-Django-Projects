from .models import Cart

def cart_count(request):
    cart_items = []
    total_price = 0
    total_items = 0

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        total_items = sum(item.quantity for item in cart_items)

    return {
        "cart_items": cart_items,
        "total_price": total_price,
        "cart_item_count": total_items
        
    }
    
    
