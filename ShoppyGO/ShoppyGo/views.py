from django.shortcuts import render
from .forms import  UserRegistrationForm , UserLoginForm , ContactForm, ProfileUpdateForm
from django.shortcuts import get_list_or_404 , redirect
from django.contrib.auth import login
from .models import Contact , Product , Cart , OrderHistory , CustomUser
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import rotate_token
from django.contrib import messages
from django.template.loader import render_to_string

def search(request):
    query = request.GET.get('query', '')  
    results = []  
    
    if query:
        results = Product.objects.filter(name__icontains=query) 
        
    results_data = [{
        'id': item.id,
        'name': item.name,
        'price': item.price,
        'image': item.image.url if item.image else '' 
    } for item in results]

    return JsonResponse({
        'results': results_data
    })

# Create your views here.
def Home(request):
    #latestt('id') ensures that we always fetch the latest (and only) settings record.
    products = Product.objects.all().filter(is_featured="True") 
    return render( request , 'home.html' , {'products' : products } )

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)  # Retrieve the product by ID
    
    return render(request, 'product_detail.html', {'product': product })

def shopAll(request):
    sort_by = request.GET.get('sort_by', 'low_to_high'  )
    
    if sort_by == 'high_to_low':
        products = Product.objects.all().order_by('-price')
    elif sort_by == 'date':
        products = Product.objects.all().order_by('-date_added')
    else:
        products = Product.objects.all().order_by('price')
         
    product_count = products.count() 
    
    return render ( request , 'shopAll.html' , { 'products':products ,'product_count' : product_count , 'sort_by': sort_by  } )

def category(request):
    return render(request , 'category.html'  )

def mens(request):
    sort_by = request.GET.get('sort_by', 'low_to_high'  )
    
    if sort_by == 'high_to_low':
        products = Product.objects.all().filter(category='mens').order_by('-price')
    elif sort_by == 'date':
        products = Product.objects.all().filter(category='mens').order_by('-date_added')
        # products = Product.objects.all().filter(category='mens').order_by('price')
    else:
        products = Product.objects.all().filter(category='mens').order_by('price')

    product_count = products.count() 
    
    return render(request , 'categories/mens.html' , { 'products' : products  , 'product_count' : product_count , 'sort_by': sort_by ,})

def womens(request):
    sort_by = request.GET.get('sort_by', 'low_to_high'  )
    
    if sort_by == 'high_to_low':
        products = Product.objects.all().filter(category='womens').order_by('-price')
    elif sort_by == 'date':
        products = Product.objects.all().filter(category='womens').order_by('-date_added')
    else:
        products = Product.objects.all().filter(category='womens').order_by('price')

    product_count = products.count() 
    
    return render(request , 'categories/womens.html' , { 'products' : products  , 'product_count' : product_count , 'sort_by': sort_by ,})

def style(request):
    sort_by = request.GET.get('sort_by', 'low_to_high'  )
    
    if sort_by == 'high_to_low':
        products = Product.objects.all().filter(category='style').order_by('-price')
    elif sort_by == 'date':
        products = Product.objects.all().filter(category='style').order_by('-date_added')
    else:
        products = Product.objects.all().filter(category='style').order_by('price')

    product_count = products.count() 
    return render(request , 'categories/style.html' , { 'products' : products  , 'product_count' : product_count , 'sort_by': sort_by ,})

def skin(request):
    sort_by = request.GET.get('sort_by', 'low_to_high'  )
    
    if sort_by == 'high_to_low':
        products = Product.objects.all().filter(category='skincare').order_by('-price')
    elif sort_by == 'date':
        products = Product.objects.all().filter(category='skincare').order_by('-date_added')
    else:
        products = Product.objects.all().filter(category='skincare').order_by('price')

    product_count = products.count() 
    return render(request , 'categories/skin.html' ,  { 'products' : products  , 'product_count' : product_count , 'sort_by': sort_by ,})

def luxe(request):
    sort_by = request.GET.get('sort_by', 'low_to_high'  )
    
    if sort_by == 'high_to_low':
        products = Product.objects.all().filter(category='luxe').order_by('-price')
    elif sort_by == 'date':
        products = Product.objects.all().filter(category='luxe').order_by('-date_added')
    else:
        products = Product.objects.all().filter(category='luxe').order_by('price')

    product_count = products.count() 
    return render(request , 'categories/luxe.html' ,  { 'products' : products  , 'product_count' : product_count , 'sort_by': sort_by ,})

def about(request):
    return render(request , 'about.html'  )

def contact(request):
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

                
    return render(request , 'contact.html' , {'form': form} )


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            rotate_token(request)
            user.save()
            return redirect('home')

    else:
        form = UserRegistrationForm()
    
    return render( request , 'registration/register.html' , {'form' : form} )
        
#add to cart
@login_required(login_url='/accounts/login/')
def add_to_cart(request, id):
    user = request.user
    product = get_object_or_404(Product, id=id)
    size = request.POST.get('size', 'M')  # Default to "M" if no size is selected
    quantity = int(request.POST.get('quantity', 1))  
    
    if request.user.is_authenticated:
        cart_item, created = Cart.objects.get_or_create(
            user = user, 
            product = product, 
            size = size,
            quantity = quantity
            )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))


def remove_from_cart(request, id):
    Cart.objects.filter(user=request.user, id=id).delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required(login_url='/accounts/login/')
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)

    total_price = sum(item.product.price * item.quantity for item in cart_items)
    total_items = sum(item.quantity for item in cart_items) 
         
    return render(request, 'cart.html', {
        "cart_items": cart_items, 
        "total_price": total_price , 
        "total_items": total_items ,
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })

def update_cart(request, id, action):
    cart_item = get_object_or_404(Cart, user=request.user, id=id)
    
    if action == "increase":
        cart_item.quantity += 1
    elif action == "decrease" and cart_item.quantity > 1:
        cart_item.quantity -= 1
    else:
        cart_item.delete()
        return redirect('cart_view')
    
    cart_item.save()
    return redirect('cart_view')




def clear_cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)

    if not cart_items.exists():
        messages.warning(request, "Your cart is already empty.")
        return redirect('cart_view')

    # Store orders in OrderHistory
    for item in cart_items:
        OrderHistory.objects.create(
            user=user,
            product=item.product,
            size=item.size,
            quantity=item.quantity,
            total_price=item.product.price * item.quantity,
        )

    # Clear the cart
    cart_items.delete()

    messages.success(request, "Your order has been placed successfully.")
    return redirect('order_history_view')  # Redirect to order history page


stripe.api_key = settings.STRIPE_SECRET_KEY
def create_checkout_session(request):
    cart_items = Cart.objects.filter(user=request.user)
    
    if not cart_items:
        return JsonResponse({'error': 'Your cart is empty'}, status=400)

    line_items = []
    for item in cart_items:
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.product.name,
                },
                'unit_amount': int(item.product.price * 100), 
            },
            'quantity': item.quantity,
        })
        

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url="http://127.0.0.1:8000/payment-success/",
        cancel_url="http://127.0.0.1:8000/payment-cancel/",
    )

    return JsonResponse({'session_id': session.id})


def payment_success(request):
    clear_cart(request)
    return render(request, "payment_success.html")

def payment_cancel(request):
    return render(request, "payment_cancel.html")

def order_history_view(request):
    orders = OrderHistory.objects.filter(user=request.user).order_by('-ordered_at')
    return render(request, 'order_history.html', {"orders": orders})


def profile(request, id):
    user = get_object_or_404(CustomUser, id=id)
    return render(request, 'profile.html', {"user": user})

def update_profile(request, id):
    user = get_object_or_404(CustomUser, id=id)

    # Ensure only the logged-in user can update their profile
    if user != request.user:
        return redirect("profile", id=user.id)  # Prevent unauthorized access

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile", id=user.id)  # Redirect to updated profile
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, 'update_profile.html', {"form": form, "user": user})

def gift_card(request):
    return render(request, 'gift.html')