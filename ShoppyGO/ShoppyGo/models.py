from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings

# For Use Email 
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']  
    
    def __str__(self):
        return self.email
    
#Contact
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional field
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# For Nagative Pricing
def validate_positive_price(value):
    if value <= 0:
        raise ValidationError('Price must be a positive number.')
    
# Product Add to DB
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('mens', 'Mens'),
        ('womens', 'Womens'),
        ('style', 'Style'),
        ('skincare', 'Skincare'),
        ('luxe', 'Luxe'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2 , validators=[validate_positive_price])
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='mens')
    image = models.ImageField(upload_to='product_images/' , max_length=1000)
    prduct_discription = models.TextField(max_length=300 , default="Discription Not Given")
    date_added = models.DateTimeField(default=timezone.now)
    is_featured = models.BooleanField(default=False)
    
    def clean(self):
        # Count existing featured products excluding the current one if it's being updated
        if self.is_featured:
            existing_featured_count = Product.objects.filter(is_featured=True).exclude(pk=self.pk).count()
            if existing_featured_count >= 3:
                raise ValidationError("Only 3 featured products are allowed. Remove one to add another.")

    def save(self, *args, **kwargs):
        self.clean()  # Call validation before saving
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

#Add to Cart
class Cart(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , null=True , blank=True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES , default='S' ) 

    
    class Meta:
        unique_together = ('user', 'product' , 'size')


class OrderHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, default="M")
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product.name} - {self.ordered_at}"
    
