from django.contrib import admin , messages
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser , Contact , Product , Cart , OrderHistory

# Register your models here.
admin.site.register(Contact)


class productAdmin(admin.ModelAdmin):
    list_display = ( "id", "name" , "price" , "category" , "date_added" , "is_featured" )
    list_filter = ('category' , 'price' , 'date_added' , "is_featured")

admin.site.register(Product , productAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ( "user" , "product" , "quantity" )
    list_filter = ("user", )

    
admin.site.register(Cart , CardAdmin)



admin.site.register(CustomUser )

admin.site.register(OrderHistory)