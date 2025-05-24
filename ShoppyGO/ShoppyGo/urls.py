from django.urls import path 
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('' , views.Home , name='home' ),
    path('shopAll/' , views.shopAll , name='shopAll' ),
    path('category/' , views.category , name='category' ),
    path('about/' , views.about , name='about' ),
    path('contact/' , views.contact , name='contact' ),
    path('category/mens' , views.mens , name='mens' ),
    path('category/womens' , views.womens , name='womens' ),
    path('category/style' , views.style , name='style' ),
    path('category/skin' , views.skin , name='skin' ),
    path('category/luxw' , views.luxe , name='luxe' ),
    path('admin/logout/', LogoutView.as_view(next_page='/admin/login/'), name='admin_logout'),
    path("register/", views.register , name='register'), 
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('search/', views.search , name='search'), 
    path('cart/', views.cart_view, name='cart_view'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:id>/<str:action>/', views.update_cart, name='update_cart'),
    path("create-checkout-session/", views.create_checkout_session, name="create_checkout_session"),
    path("payment-success/", views.payment_success, name="payment_success"),
    path("payment-cancel/", views.payment_cancel, name="payment_cancel"),
    path('order-history/', views.order_history_view, name='order_history_view'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('update-profile/<int:id>', views.update_profile, name='update_profile'),
    path('gift/', views.gift_card, name='gift'),
]









